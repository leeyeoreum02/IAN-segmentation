import torch
from torch import nn


class ModelFactory(nn.Module):
    def __init__(self, model_name, num_classes, in_ch, emb_shape=None):
        super(ModelFactory, self).__init__()
        self.model_name = model_name
        self.num_classes = num_classes
        self.in_ch = in_ch
        self.emb_shape = emb_shape

    def get(self):
        if self.model_name == 'DeepLabV3':
            from .deeplabv33d import DeepLabV3_3D
            return DeepLabV3_3D(self.num_classes, self.emb_shape, self.in_ch, 'resnet18_os8')
        else:
            raise ValueError(f'Model {self.model_name} not found')