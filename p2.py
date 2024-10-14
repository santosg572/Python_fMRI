import dicom2nifti
import nibabel as nib
import nilearn as nil
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import os
import numpy as np

def despliegaIMG(img = 0):
  plt.imshow(img, cmap='bone')
  plt.show()  
 
def corr(x=0, y=0):
  x = np.array(x)
  y = np.array(y)
  xm = np.mean(x)
  ym = np.mean(y)
  sxy = np.sum((x - xm)*(y - ym))
  x2 = np.sqrt(np.sum((x-xm)**2))
  y2 = np.sqrt(np.sum((y-ym)**2))
  return sxy / (x2 * y2)

def CorrVecindades(i0=0, k0=0):
  global IMGB
  global brain_vol_data
  global X
  
  IMGB[i0, k0] = 1
  for i in range(i0-1, i0+2):
    for k in range(k0-1,k0+2):
       if IMGB[i, k] == 0:
         y = brain_vol_data[i, 22, k, :]
         r = corr(y, X)
         if  r > .3:
           print(i,k)
           CorrVecindades(i, k)
  

brain_vol = nib.load('fmri.nii')

print(type(brain_vol))

print(brain_vol.header)

brain_vol_data = brain_vol.get_fdata()
print(type(brain_vol_data))

print(brain_vol_data.shape)

i0 = 22
j0 = 22
k0 = 18

# despliega imagen

del1 = 1
img = brain_vol_data[:, j0, :, 0]
print(img.shape)

img[i0-del1:i0+del1, k0-del1:k0+del1] = 0
#despliegaIMG(img)

IMGB = np.zeros(img.shape)

X = brain_vol_data[i0, j0, k0, :]

CorrVecindades(i0, k0)

