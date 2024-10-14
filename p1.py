import dicom2nifti
import nibabel as nib
import nilearn as nil
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import os

brain_vol = nib.load('fmri.nii')

print(type(brain_vol))

print(brain_vol.header)

brain_vol_data = brain_vol.get_fdata()
print(type(brain_vol_data))

print(brain_vol_data.shape)

imgVol = brain_vol_data[:,:,:,0]

img = imgVol[:,22,:]

i0 = 22
j0 = 18
del1 = 1
img[i0-del1:i0+del1, j0-del1:j0+del1] = 0
plt.imshow(img, cmap='bone')
#plt.axis('off')
plt.show()
