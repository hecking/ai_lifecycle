import ctd_path
import sys
sys.path.append(ctd_path.cracktip_dir)

import torch
from src.deep_learning import nets

def load_model(size, dropout_prob):
    # Model Setup
    model = nets.ParallelNets(in_ch=2, out_ch=1, init_features=size, dropout_prob=dropout_prob)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    return model