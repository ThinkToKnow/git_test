import torch
import torchvision

model = torchvision.models.resnet18()
inputs = torch.rand((100,3,32,32))
outputs = model(inputs)
:
