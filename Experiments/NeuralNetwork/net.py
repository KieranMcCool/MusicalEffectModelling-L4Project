#!/usr/bin/env python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from spectogram import spectogram
import numpy as np
import globals
from dataloader import loadWav, writeWav, one_hot_decode
from data import LazyDataset
from os import walk
from random import randrange

learning_rate = 1e-4
CUDA = True

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.iteration = 1

    def train(self, data, training=True, filename=''):
        global iteration

        # Get Input and target from data
        if torch.cuda.is_available() and CUDA:
            inputVector = data[0].cuda()
            target = data[1].cuda()
        else:
            inputVector = data[0]            
            target = data[1]

        # Encapsulate in PyTorch Variable
        x = Variable(inputVector)
        y = Variable(target, requires_grad=False).squeeze()

        # Run input through model and compute loss
        y_pred = self(x).squeeze()
        loss = self.loss_fn(y_pred, y)

        if self.iteration % 100 == 0 and True:
            print(self.iteration if training else '', filename, loss.data[0])
            if self.iteration % 200 == 0 and True:
                print('\ttarget = %s prediction = %s' % (y.shape, y_pred.shape))
                print('\ttarget = %s prediction = %s\n' % (y.data[0], y_pred.data[0]))

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
            pred = self.train(b, training=False, filename=inputFile).squeeze().tolist()
            output += pred
        writeWav(np.array(output), outputFile)
        spectogram(outputFile)
        self.iteration = backup

class LSTMModel(Model):
    def __init__(self):
        super(LSTMModel, self).__init__()
        # Model Architecture
        self.lstm1 = nn.LSTM(globals.INPUT_VECTOR_SIZE, 800, 8)
        self.fc = nn.Sequential(
                nn.Linear(800,1))

        self.optimizer = torch.optim.Adam(self.parameters(), lr=learning_rate)
        self.loss_fn = torch.nn.MSELoss(size_average=False)

        if torch.cuda.is_available() and CUDA:
            self = self.cuda()

    def forward(self, x):
        x = self.lstm1(x)
        x = x[0]
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

class ConvModel(Model):
    def __init__(self):
        super(ConvModel, self).__init__()
        # Model Architecture
        ivs = globals.INPUT_VECTOR_SIZE
        ovs = 2**16
        self.conv = nn.Sequential(
            nn.Conv1d(64, 800, 1), nn.ReLU(),
            nn.Conv1d(800, 800, 1), nn.ReLU(),
            nn.Conv1d(800, 700, 1), nn.ReLU(),
            nn.Conv1d(700, 500, 1), nn.ReLU(),
            nn.Conv1d(500, 250, 1), nn.ReLU(),
            nn.Conv1d(250, 100, 1), nn.ReLU(),
            nn.MaxPool1d(1))
        self.fc = nn.Sequential(
            nn.Linear(100, 50), nn.ReLU(),
            nn.Linear(50, 25), nn.ReLU(),
            nn.Linear(25, 10), nn.ReLU(),
            nn.Linear(10, 1))

        self.optimizer = torch.optim.Adam(self.parameters(), lr=learning_rate)
        self.loss_fn = torch.nn.MSELoss(size_average=False)

        if torch.cuda.is_available() and CUDA:
            self = self.cuda()

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

class LinearModel(Model):
    def __init__(self):
        super(LinearModel, self).__init__()
        # Model Architecture
        self.lin1 = nn.Sequential(nn.Linear(1, 64), nn.ReLU(),
                nn.Linear(64, 32), nn.ReLU(),
                nn.Linear(32, 16), nn.ReLU(),
                nn.Linear(16, 1))

        self.optimizer = torch.optim.Adam(self.parameters(), lr=learning_rate)
        self.loss_fn = torch.nn.MSELoss(size_average=False)

        if torch.cuda.is_available() and CUDA:
            self = self.cuda()

    def forward(self, x):
        x = self.lin1(x)
        return x

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
        model.fileOutput('./model_outputs/test.wav', "./model_outputs/%d output.wav" %  name, testFile='model_outputs/processed/test.wav')
        torch.save(model.state_dict(), './model_checkpoints/%d.model' % name)

    model = ConvModel()
    CurrentData = loadData()
    for i, data in enumerate(CurrentData.randomSampler()):
        model.train(data)
        if model.iteration % globals.OUTPUT_FREQUENCY == 0:
            doCheckPoint(model, model.iteration)
    doCheckPoint(model, -1)
main()
