import torch
import numpy as np
import globals
from torch.autograd import Variable
from dataloader import loadWav, writeWav
from data import WavFile
from os import walk

# D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
D_in, H, D_out = globals.INPUT_VECTOR_SIZE, 150, 1

loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 1e-4
iteration = 1

model = torch.nn.Sequential(
          torch.nn.Linear(D_in, H),
          torch.nn.ReLU(),
          torch.nn.Linear(H, D_out),
        )

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

def doTest(i):
    CurrentData = WavFile('test.wav', None)
    output = [] 

    for j in range(CurrentData.len()):
        output += [ predict(CurrentData.format(j), train=False)]
    output = np.array(output)
    writeWav(globals.SAMPLE_RATE, output, '%d.wav' % i)

def predict(data, train=True, filename=''):
    global iteration
    # Get Input and target from data
    inputVector = torch.from_numpy(data[0]).type(torch.FloatTensor)
    target = torch.FloatTensor([data[1]])
    
    # Encapsulate in PyTorch Variable
    x = Variable(inputVector)
    y = Variable(target, requires_grad=False)

    # Run input through model and compute loss
    y_pred = model(x)
    loss = loss_fn(y_pred, y)

    
    # If training then backwards propagate, otherwise save prediction for output
    if train:
        print(iteration, filename, loss.data[0])
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

main()
