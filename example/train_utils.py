PATH_TO_CRACKTIP_PROJECT = 'C:/Users/heck_ti/Documents/explainable-crack-tip-detection'
import sys
sys.path.append(PATH_TO_CRACKTIP_PROJECT)

import torch
import numpy as np
from torch.nn import MSELoss
from src.deep_learning.loss import DiceLoss
from src.deep_learning import evaluate

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
dice_loss = DiceLoss()
mse_loss = MSELoss()

def compute_loss(model_output, labels):
    return dice_loss(model_output[0], labels[0]) + 100 * mse_loss(model_output[1], labels[1])

def validate_model(model, val_loader):
    model.eval()
    deviation = 0
    reliability = 0
    num_batches = 0
    for i, (inputs, labels) in enumerate(val_loader):
        inputs = inputs.to(device)
        labels = labels[0].to(device)      
        
        outputs = model.forward(inputs)
        deviations = evaluate.get_deviation(outputs[0].to('cpu'),
                                                        labels.to('cpu'))
        deviation += np.sum(deviations)
        reliability += evaluate.get_reliability(outputs[0].to('cpu'),
                                                           labels.to('cpu'))
        num_batches = i + 1
    
    return deviation / num_batches, reliability / num_batches