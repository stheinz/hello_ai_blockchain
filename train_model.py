import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models

# Pre-trained model (ResNet18)
model = models.resnet18(weights='IMAGENET1K_V1')  # Update to use weights instead of pretrained
num_ftrs = model.fc.in_features

# Update the fully connected layer to match the number of classes in the dataset
model.fc = nn.Linear(num_ftrs, 10)  # Assuming the FakeData dataset has 10 classes

transform = transforms.Compose([transforms.Resize(256),
                                transforms.CenterCrop(224),
                                transforms.ToTensor()])

# Create a FakeData dataset with 10 classes
train_dataset = datasets.FakeData(size=1000, transform=transform, num_classes=10)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
model.train()
for epoch in range(5):
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        if epoch % 1 == 0:
            print(f'Epoch [{epoch + 1}/5], Loss: {loss.item():.4f}')