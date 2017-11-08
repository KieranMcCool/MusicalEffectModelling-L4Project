import torch
from torch.autograd import Variable
from dataloader import getDatasets

# [ [ [file1drychunks], [file1wetchunks] ], [file2drychunks], [file2wetchunks] ... ]
data = getDatasets()

inputSize = len(data[0][0][0])

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 1, inputSize, 100, inputSize

loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 1e-4

model = torch.nn.Sequential(
          torch.nn.Linear(D_in, H),
          torch.nn.ReLU(),
          torch.nn.Linear(H, D_out),
        )

iteration = 0

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for files in data:
  for i in range(len(files[0])):
    # For chunk in files
    dry = torch.from_numpy(files[0][i]).type(torch.FloatTensor)
    wet = torch.from_numpy(files[1][i]).type(torch.FloatTensor)

    x = Variable(dry)
    y = Variable(wet, requires_grad=False)

    # iterate over chunks
    for t in range(50):

      y_pred = model(x)

      loss = loss_fn(y_pred, y)
      print(iteration, loss.data[0])
      optimizer.zero_grad()
      #model.zero_grad()
      loss.backward()
      optimizer.step()

      iteration += 1