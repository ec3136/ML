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

    
def find_patches(self, class_num, num_patches):
        '''
        Function that samples slices with evenly distributed classes
        INPUT: 
        (1) list 'training_images': all train data images to choose from
        (2) int 'class_num': class to sample from choice of {0, 1, 2, 3, 4}
        (3) tuple 'patch_size': dimesions of patches to be generated, defaults 
        65 x 65
        OUTPUT: num_samples patches from class 'class_num' randomly selcted 
        '''

        h, w = self.patch_size[0], self.patch_size[1]
        patches, labels = [], np.full(num_patches, class_num, 'float')
        print('Finding patches of class {}...'.format(class_num))

        
        ct = 0
        while ct < num_patches:
          im_path = random.choice(self.train_data)
          fn = os.path.basename(im_path)
          label = io.imread('Labels/' + fn[:-4] + 'L.png')

          resample if class_num not in selected slice
          while len(np.argwhere(label == class_num)) < 10:
               im_path = random.choice(self.train_data)
               fn = os.path.basename(im_path)
               label = io.imread('Labels/' + fn[:-4] + 'L.png')

          if len(np.argwhere(label == class_num)) < 10:
            continue 

            # select centerpix (p) and patch (p_ix)
            img = io.imread(im_path).reshape(5, 240, 240)[:-1].astype('float')
            p = random.choice(np.argwhere(label == class_num))
            p_ix = (p[0]-(h/2), p[0]+((h+1)/2), p[1]-(w/2), p[1]+((w+1)/2))
            patch = np.array([i[p_ix[0]:p_ix[1], p_ix[2]:p_ix[3]] for i in img])

            # resample it patch is empty or too close to edge
            while patch.shape != (4, h, w) or len(np.unique(patch)) == 1:
                p = random.choice(np.argwhere(label == class_num))
                p_ix = (p[0]-(h/2), p[0]+((h+1)/2), p[1]-(w/2), p[1]+((w+1)/2))
                patch = np.array([i[p_ix[0]:p_ix[1], p_ix[2]:p_ix[3]] for i in img])
            if patch.shape != (4, h, w) or len(np.argwhere(patch == 0)) > (h * w):
                continue
            
              patches.append(patch)
            ct += 1
        return np.array(patches), labels
