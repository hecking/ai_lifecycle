import ctd_path
import sys
PATH_TO_CRACKTIP_PROJECT = ctd_path.cracktip_dir
sys.path.append(PATH_TO_CRACKTIP_PROJECT)

import os
import torch
from torchvision.transforms import Compose
from src.dataprocessing import transforms
from src.dataprocessing.dataset import CrackTipDataset
from src.dataprocessing.datapreparation import import_data
from src.dataprocessing.interpolation import interpolate_on_array
from src.dataprocessing import preprocess

# Set parameters and paths
####################################################################################################
# Data

ORIGIN = os.path.join(PATH_TO_CRACKTIP_PROJECT, 'data', 'S_160_4.7', 'interim')

DATA_PATH_TRAIN_INPUT = os.path.join(ORIGIN, 'lInputData_right.pt')
DATA_PATH_TRAIN_LABEL = os.path.join(ORIGIN, 'lGroundTruthData_right.pt')

DATA_PATH_VAL_INPUT = os.path.join(ORIGIN, 'lInputData_left.pt')
DATA_PATH_VAL_LABEL = os.path.join(ORIGIN, 'lGroundTruthData_left.pt')

def load_data():
    trsfs = {'train': Compose([transforms.EnhanceTip(),
                               transforms.RandomCrop(size=[120, 180], left=[10, 30]),
                               transforms.RandomRotation(degrees=10),
                               transforms.Resize(size=224),
                               transforms.RandomFlip(),
                               transforms.InputNormalization(),
                               transforms.CrackTipNormalization(),
                               transforms.ToCrackTipsAndMasks()
                               ]),
             'val': Compose([transforms.EnhanceTip(),
                             transforms.InputNormalization(),
                             transforms.CrackTipNormalization(),
                             transforms.ToCrackTipsAndMasks()
                             ])}

    train = CrackTipDataset(inputs=DATA_PATH_TRAIN_INPUT, labels=DATA_PATH_TRAIN_LABEL,
                                         transform=trsfs['train'])
    
    val = CrackTipDataset(inputs=DATA_PATH_VAL_INPUT, labels=DATA_PATH_VAL_LABEL,
                                       transform=trsfs['val'])

    return train, val

def load_instance(experiment, sample_num, side, exists_target=False):
    sizes = {
            'S_950_1.6': 450,  # mm
            'S_160_4.7': 70,
            'S_160_2.0': 70
    }
    size = sizes[experiment] if experiment in sizes else None
    data_path = os.path.join(PATH_TO_CRACKTIP_PROJECT, 'data', experiment, 'raw')
    
    entry = experiment + '_AllDataPoints_' + str(sample_num) + '.txt'
    # Read nodemap
    input_data, ground_truth_data = import_data(nodemaps={sample_num: entry},
                                                data_path=data_path,
                                                side=side,
                                                exists_target=exists_target)
    
    # Interpolate input data on arrays of pixel size 256x256
    interp_size = size if side == 'right' else size * -1

    interp_coors, interp_disps, interp_eps_vm = interpolate_on_array(input_by_nodemap=input_data,
                                                                     interp_size=interp_size)

    # Preprocess input
    disps = interp_disps[entry + '_' + side]
    input_ch = torch.tensor(disps, dtype=torch.float32)
    input_ch = preprocess.normalize(input_ch).unsqueeze(0)

    background = interp_eps_vm[entry + '_' + side] * 100
    return input_ch, background, interp_size, ground_truth_data