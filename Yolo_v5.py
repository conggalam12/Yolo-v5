


!nvidia-smi

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from matplotlib import pyplot as plt 
import cv2 as cv

fig,ax = plt.subplots(2,2,figsize=(10,5))
image = cv.imread("/content/drive/MyDrive/Data/Data_Biensoxe/train/images/0000_00532_b.jpg")
ax[0][0].imshow(image)
image = cv.imread("/content/drive/MyDrive/Data/Data_Biensoxe/train/images/0000_02187_b.jpg")
ax[0][1].imshow(image)
image = cv.imread("/content/drive/MyDrive/Data/Data_Biensoxe/train/images/0109_01594_b.jpg")
ax[1][0].imshow(image)
image = cv.imread("/content/drive/MyDrive/Data/Data_Biensoxe/train/images/0109_04995_b.jpg")
ax[1][1].imshow(image)
fig.show()

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Data/Data_Biensoxe

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5  # clone repo
# %cd yolov5
# %pip install -qr requirements.txt  # install dependencies

import torch
print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

# Create .yaml file 
import yaml

data_yaml = dict(
    train = '/content/drive/MyDrive/Data/Data_Biensoxe/train',
    val = '/content/drive/MyDrive/Data/Data_Biensoxe/val',
    nc = 1,
    names = ['Bienso']
)

# Note that I am creating the file in the yolov5/data/ directory.
with open('data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov5

!wandb disabled
!python train.py --img 1000 --batch 16 --epochs 15--data data.yaml --weights yolov5n.pt

img = cv.imread("runs/train/exp7/val_batch2_pred.jpg")
plt.figure(figsize=(15, 15))
plt.imshow(img)
