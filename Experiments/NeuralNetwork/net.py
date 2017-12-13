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

loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 1e-3
iteration = 1

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv = nn.Sequential(
                nn.Conv1d(64, 32, 1, stride=4), nn.ReLU(),
                nn.MaxPool1d(1), nn.ReLU())
        self.lin = nn.Sequential(
                nn.Linear(32, 16), nn.ReLU(),
                nn.Linear(16, 1))
                
    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        x = self.lin(x)
        return x

model = Model()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

def testOutput(milestone):
    global iteration
    backup = iteration
    iteration = 1
    fname = './model_outputs/test.wav'
    pname = './model_outputs/testoutput.wav'
    CurrentData = LazyDataset(loadWav(fname), procData=loadWav(pname) )
    output = []
    for i, b in enumerate(CurrentData.sequentialSampler()):
        pred = train(b, training=False, filename='testing')
        pred = [ p[0] for p in pred ] 
        output += pred
    outputName = './model_outputs/%d.wav' % milestone
    writeWav(np.array(output), outputName)
    spectogram(outputName)
    iteration = backup


def train(data, training=True, filename=''):
    global iteration

    # Get Input and target from data
    inputVector = data[0]
    target = data[1]
    
    # Encapsulate in PyTorch Variable
    x = Variable(inputVector)
    y = Variable(target, requires_grad=False)

    # Run input through model and compute loss
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    if iteration % 100 == 0 and True:
        print(iteration if train else '', filename, loss.data[0])

    # If training then backwards propagate, otherwise save prediction for output
    if training:
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    iteration += 1

    return y_pred.data

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

    CurrentData = loadData()
    for i, data in enumerate(CurrentData.randomSampler()):
        train(data)
        if iteration % globals.OUTPUT_FREQUENCY == 0 :
            testOutput(iteration)
            torch.save(model.state_dict(), 
                './model_checkpoints/%d.model' % iteration)
main()
