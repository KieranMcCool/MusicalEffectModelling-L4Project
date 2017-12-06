#!/usr/bin/env python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np
import globals
from dataloader import loadWav, writeWav
from data import WavFile, batchify
from os import walk

loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 1e-4
iteration = 1

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()

        self.conv = nn.Sequential(
                nn.BatchNorm1d(64),
                nn.Conv1d(64, 64, 1), nn.ReLU(), nn.Dropout(),
                nn.Conv1d(64,32, 1),  nn.ReLU(), nn.Dropout())
        self.fc = nn.Sequential(
                nn.Linear(32, 16), 
                nn.Linear(16, 1))

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

model = Model()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

def doTest(i):
    fname = './model_outputs/test.wav'
    CurrentData = WavFile(fname, './model_outputs/testoutput.wav')
    output = [] 

    for j in range(CurrentData.len()):
        output += [ predict(CurrentData.format(j), filename=fname, train=False)]

    output = np.array(output)
    writeWav(globals.SAMPLE_RATE, output, './model_outputs/%d.wav' % i)

def train(data, training=True, filename=''):
    global iteration
    # Get Input and target from data
    inputVector = torch.Tensor(data[0])
    target = torch.Tensor([data[1]])
    
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
    getFiles = lambda x : ([ '%s/%s' % (x,  l) 
        for l in list(walk(x))[0][2] if l.endswith('.wav')])

    raw = getFiles('./dataset')
    processed = getFiles('./dataset/processed')
    # Iterate over files and processed files
    for file, pFile in zip(raw, processed):
        CurrentData = WavFile(loadWav(file), procData=loadWav(pFile))
        for i in range(CurrentData.len() - globals.BATCH_SIZE):
            data = batchify([CurrentData.getSample(z)
                for z in range(i, 
                    i + globals.BATCH_SIZE if i + globals.BATCH_SIZE < CurrentData.len() else i)])

            train(data, filename=file)
            if iteration % globals.OUTPUT_FREQUENCY == 0 :
                doTest(iteration)
                torch.save(model.state_dict(), 
                    './model_checkpoints/%d.model' % iteration)
main()
