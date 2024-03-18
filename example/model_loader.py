import sys
PATH_TO_CRACKTIP_PROJECT = 'C:/Users/heck_ti/Documents/explainable-crack-tip-detection'
sys.path.append(PATH_TO_CRACKTIP_PROJECT)

import torch
from src.deep_learning import nets

def load_model(size, dropout_prob):
    # Model Setup
    model = nets.ParallelNets(in_ch=2, out_ch=1, init_features=size, dropout_prob=dropout_prob)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    return model