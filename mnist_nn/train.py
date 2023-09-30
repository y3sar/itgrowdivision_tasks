from model import CNN
import torch
import torch.nn as nn
import torch.optim as optim
from data_prep import trainloader
import wandb

wandb.init(project="mnist-cnn", entity="y3sar")

net = CNN()

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# Train for 5 epochs
for epoch in range(5):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data

        optimizer.zero_grad()

        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 2000 == 1999:  # print every 2000 mini-batches
            print(f'[{epoch + 1}, {i + 1}] loss: {running_loss / 2000:.3f}')
            wandb.log({"Training Loss": running_loss / 2000})
            running_loss = 0.0

print('Finished Training')

torch.save(net.state_dict(), 'mnist_cnn_model_state.pth')