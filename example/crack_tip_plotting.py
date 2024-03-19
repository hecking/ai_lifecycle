import ctd_path
import sys
sys.path.append(ctd_path.cracktip_dir)

import numpy as np
from scipy import ndimage
from src.utils.plot import plot_prediction
from src.utils.utilityfunctions import calculate_segmentation

# Simple crack tip prediction by taking the mean of all segmented pixels for each area
def plot_predictions(preditions, background, interp_size, title): 
    crack_tip_seg = calculate_segmentation(preditions)

    is_crack_tip = np.where(preditions >= 0.5, 1, 0)
    labels, num_of_labels = ndimage.label(is_crack_tip)

    crack_tip_means = []
    for seg_label in range(1, num_of_labels + 1):
        seg = np.where(labels == seg_label, 1, 0)
        tips = calculate_segmentation(seg).numpy()
        crack_tip = np.mean(tips, axis=0)
        crack_tip_means.append(crack_tip)
    crack_tip_means = np.asarray(crack_tip_means, dtype=np.float32).reshape(-1, 2)

    # Plot and save
    print('Data will be plotted...')

    plot_prediction(background=background,
                    interp_size=interp_size,
                    crack_tip_prediction=crack_tip_means,
                    crack_tip_seg=crack_tip_seg,
                    f_min=0,
                    f_max=0.68,
                    title=title,
                    label='Von Mises strain [%]')