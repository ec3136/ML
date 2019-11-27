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

    def center_n(self, n, patches):
        '''
        Takes list of patches and returns center nxn for each patch.
        Use as input for cascaded architectures.
        INPUT   (1) int 'n': size of center patch to take (square)
                (2) list 'patches': list of patches to take subpatch of
        OUTPUT: list of center nxn patches.
        '''
        sub_patches = []
        for mode in patches:
            subs = np.array([patch[(self.h/2) - (n/2):(self.h/2) + ((n+1)/2),
                                   (self.w/2) - (n/2):(self.w/2) + ((n+1)/2)] 
                                    for patch in mode])
            sub_patches.append(subs)
            
        return np.array(sub_patches)
