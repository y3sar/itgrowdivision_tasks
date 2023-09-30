from model import CNN
from data_prep import testloader
import torch
import torch.nn as nn
import wandb

wandb.init(project="mnist-cnn", entity="y3sar")

# Test the model with the test set
net = CNN()
criterion = nn.CrossEntropyLoss()
net.load_state_dict(torch.load('mnist_cnn_model_state.pth'))
net.eval()  
correct = 0
total = 0
test_loss = 0.0

with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        loss = criterion(outputs, labels)
        test_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = correct / total
print(f'Test Accuracy: {accuracy * 100:.2f}%')

wandb.log({"Test Accuracy": accuracy})
wandb.log({"Test Loss": test_loss / len(testloader.dataset)})
wandb.finish()  
