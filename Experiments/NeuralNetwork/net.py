import torch
from torch import nn, autograd, optim
from torch.nn import functional as F
from dataloader import loadWav
from dataloader import getDatasets

input_size = 352800
hidden_size = 800
num_classes = 352800
learning_rate = 0.001

class Model(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.h1 = nn.Linear(input_size, hidden_size)
        self.h2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = x.clamp(-1, 0)
        x = self.h1(x)
        x = F.tanh(x)
        x = self.h2(x)
        x = F.log_softmax(x)
        return x

def train():
    model = Model(input_size=input_size, hidden_size=hidden_size, num_classes=num_classes)
    opt = optim.Adam(params=model.parameters(), lr=learning_rate)
    
    # For file in datasets
        # for chunk in file
            # train 100 times on chunk

    #  File in format [ [ [raw equal sized chunks], [raw equal sized chunks] ] ]
    for file in getDatasets():
        for chunk in file:
            raw = torch.from_numpy(chunk[0]).type(torch.FloatTensor)
            processed = torch.from_numpy(chunk[1]).type(torch.FloatTensor)

            input = autograd.Variable(raw)
            target = autograd.Variable(processed).long()
            for i in range(100):
                out = model(input)
                print(out)
                _, pred = out.max(1)
                print('target', str(target.view(1, -1)).split('\n')[1])
                print('pred', str(pred.view(1, -1)).split('\n')[1])
                loss = F.nll_loss(out, target)
                print('loss', loss.data[0])

        model.zero_grad()
        loss.backward()
        opt.step()

train()

