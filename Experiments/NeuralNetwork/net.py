import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np
import globals
from dataloader import loadWav, writeWav
from data import WavFile
from os import walk

# D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
D_in, D_out = globals.INPUT_VECTOR_SIZE, 1

loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 1e-4
iteration = 1

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv1d(64,64,1)
        self.conv2 = nn.Conv1d(64,32,1)
        self.conv3 = nn.Conv1d(32,1,1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        return x[0][0]

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

def predict(data, train=True, filename=''):
    global iteration
    # Get Input and target from data
    inputVector = torch.Tensor(data[0]).type(torch.FloatTensor)
    target = torch.FloatTensor([data[1]])
    
    # Encapsulate in PyTorch Variable
    x = Variable(inputVector)
    y = Variable(target, requires_grad=False)

    # Run input through model and compute loss
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    if iteration % 100 == 0 and False:
        print(iteration if train else '', filename, loss.data[0])

    # If training then backwards propagate, otherwise save prediction for output
    if train:
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        iteration += 1

    return y_pred.data[0]

def main():
    getFiles = lambda x : ([ '%s/%s' % (x,  l) 
        for l in list(walk(x))[0][2] if l.endswith('.wav')])

    raw = getFiles('./dataset')
    processed = getFiles('./dataset/processed')
    for file, pFile in zip(raw, processed):
        CurrentData = WavFile(file, processedPath=pFile)
        for i in range(CurrentData.len()):
            predict(CurrentData.format(i), filename=file)
            if iteration % globals.OUTPUT_FREQUENCY == 0 :
                doTest(iteration)
                torch.save(model.state_dict(), 
                    './model_checkpoints/%d.model' % iteration)

main()
