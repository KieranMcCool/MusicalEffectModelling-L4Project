#!/usr/bin/env python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from spectogram import spectogram
import numpy as np
import globals
from dataloader import loadWav, writeWav
from data import LazyDataset
from os import walk
from random import randrange

learning_rate = 1e-3

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        
        # Model Architecture
        self.conv = nn.Sequential(
            nn.BatchNorm1d(1),
            nn.Conv1d(1, 128, 1, dilation=1), nn.ReLU(),
            nn.Conv1d(128, 64, 1, dilation=2), nn.ReLU(), 
            nn.Conv1d(64, 32, 1, dilation=4), nn.ReLU(), 
            nn.MaxPool1d(1), nn.ReLU())
        self.lin = nn.Sequential(
            nn.Linear(32 * globals.INPUT_VECTOR_SIZE, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU(), 
            nn.Linear(256, 100), nn.ReLU(), 
            nn.Linear(100, 1))

        self.iteration = 1
        self.optimizer = torch.optim.Adam(self.parameters(), lr=learning_rate)
        self.loss_fn = torch.nn.MSELoss(size_average=False)

        if torch.cuda.is_available():
            self = self.cuda()

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        x = self.lin(x)
        return x

    def train(self, data, training=True, filename=''):
        global iteration

        # Get Input and target from data
        if torch.cuda.is_available():
            inputVector = data[0].cuda()
            target = data[1].cuda()
        else:
            inputVector = data[0].cuda()
            target = data[1].cuda()

        # Encapsulate in PyTorch Variable
        x = Variable(inputVector)
        y = Variable(target, requires_grad=False)

        # Run input through model and compute loss
        y_pred = self(x)
        loss = self.loss_fn(y_pred, y)

        if self.iteration % 100 == 0 and True:
            print(self.iteration if training else '', filename, loss.data[0])

        # If training then backwards propagate, otherwise save prediction for output
        if training:
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        self.iteration += 1

        return y_pred.data

    def fileOutput(self, inputFile, outputFile, testFile=None):
        backup = self.iteration
        self.iteration = 1
        CurrentData = LazyDataset(loadWav(inputFile), 
                procData=loadWav(testFile) if testFile != None else None) # test file used to calculate loss if that's important to you (optional)
        output = []
        for i, b in enumerate(CurrentData.sequentialSampler()):
            pred = self.train(b, training=False, filename=inputFile)
            pred = [ p[0] for p in pred ] 
            output += pred
        writeWav(np.array(output), outputFile)
        spectogram(outputFile)
        self.iteration = backup

def main():
    def loadData():
        getFiles = lambda x : ([ '%s/%s' % (x,  l) 
            for l in list(walk(x))[0][2] if l.endswith('.wav')])

        dryFiles = getFiles('./dataset')
        wetFiles = getFiles('./dataset/processed')

        dryData = []
        wetData =  []

        # Iterate over files and processed files
        for file, pFile in zip(dryFiles, wetFiles):
           dryData = dryData  + list(loadWav(file))
           wetData = wetData + list(loadWav(pFile))
        return LazyDataset(np.array(dryData), np.array(wetData))
    def doCheckPoint(model, name):
        model.fileOutput('./model_outputs/test.wav', "./model_outputs/%d.wav" %  name, testFile='model_outputs/testoutput.wav')
        torch.save(model.state_dict(), './model_checkpoints/%d.model' % name)

    model = Model()
    CurrentData = loadData()
    for i, data in enumerate(CurrentData.randomSampler()):
        model.train(data)
        if model.iteration % globals.OUTPUT_FREQUENCY == 0:
            doCheckPoint(model, model.iteration)
    doCheckPoint(model, 'final')
main()
