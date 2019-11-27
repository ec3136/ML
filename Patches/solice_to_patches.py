import numpy as np

class Patch(obejct):
  def __init__(self, patck_size, train_data, num_samples):
    '''
    This class if for creating patches and subpatches from training data
    to use as input for segmentation models.
    Inut: 
    1. tuple 'patch_size': size (in voxels) of patches for extract
    2. list 'train_data': list of filepaths to all training data 
    3. int 'num_samples': number of patches to collect from training data 
    '''
    self.patch_size = patch_size
    self.num_samples = num_samples 
    self.train_data = train_data 
    self.h = self.patch_size[0]
    self.w = self.patch_size[1]

    
def slice_to_patches(self, filename):
        '''
        Converts an image to a list of patches with a stride length of 1. 
        Use as input for image prediction.
        INPUT: str 'filename': path to image to be converted to patches
        OUTPUT: list of patched version of imput image.
        '''
        slices = io.imread(filename).astype('float').reshape(5,240,240)[:-1]
        plist=[]
        for slice in slices:
            if np.max(img) != 0:
                img /= np.max(img)
            p = extract_patches_2d(img, (h,w))
            plist.append(p)
        return np.array(zip(np.array(plist[0]), np.array(plist[1]), 
                            np.array(plist[2]), np.array(plist[3])))