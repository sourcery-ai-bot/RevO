import torch
from torch import nn
import logging
import time
import os
import dist
from models.backbone import resnet_backbone
from torch.utils.data import DataLoader
import numpy as np
from torchvision.models import resnet18
from metrics import Accuracy
from callbacks import *


def get_timestamp():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())


def create_model(cfg: dict):
    # TODO
    return resnet18()


def create_optimizer(cfg: dict, model: torch.nn.Module):
    # TODO
    return torch.optim.Adam(params=filter(lambda x: x.requires_grad, model.parameters()))


def create_loss(cfg: dict):
    # TODO
    return nn.CrossEntropyLoss()


def create_train_dataloader(cfg: dict):
    # TODO
    dataset = []
    for _ in range(20):
        sample = {'input': np.random.randn(3, 224, 224), 'target': np.random.randint(low=1, high=5)}
        dataset.append(sample)

    return DataLoader(dataset, batch_size=2)


def create_val_dataloader(cfg: dict):
    # TODO
    return create_train_dataloader(cfg)


def create_metrics(cfg):
    # TODO
    return Accuracy


def create_callbacks(cfg, trainer):
    # TODO
    trainer.register_callback((10, MetricCallback))
    trainer.register_callback((10, ValidationCallback))
    trainer.register_callback((10, SaveCheckpointCallback))
