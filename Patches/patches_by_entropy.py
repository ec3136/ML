def patches_by_entropy(self, num_patches):
        '''
        Finds high-entropy patches based on label, allows net to learn 
        borders more effectively.
        INPUT: int 'num_patches': defaults to num_samples, enter in quantity
        it using in conjunction with randomly sampled patches.
        OUTPUT: list of patches (num_patches, 4, h, w) selected by highest
        entropy
        '''
        patches, labels = [], []
        ct = 0
        while ct < num_patches:
            im_path = random.choice(training_images)
            fn = os.path.basename(im_path)
            label = io.imread('Labels/' + fn[:-4] + 'L.png')

            # pick again if slice is only background
            if len(np.unique(label)) == 1:
                continue

            img = io.imread(im_path).reshape(5, 240, 240)[:-1].astype('float')
            l_ent = entropy(label, disk(self.h))
            top_ent = np.percentile(l_ent, 90)

            # restart if 80th entropy percentile = 0
            if top_ent == 0:
                continue

            highest = np.argwhere(l_ent >= top_ent)
            p_s = random.sample(highest, 3)
            for p in p_s:
                p_ix = (p[0]-(h/2), p[0]+((h+1)/2), p[1]-(w/2), p[1]+((w+1)/2))
                patch = np.array([i[p_ix[0]:p_ix[1], p_ix[2]:p_ix[3]]
                                  for i in img])
                # exclude any patches that are too small
                if np.shape(patch) != (4,65,65):
                    continue
                patches.append(patch)
                labels.append(label[p[0],p[1]])
            ct += 1
            return np.array(patches[:num_samples]), 
                   np.array(labels[:num_samples])


if __name__ == '__main__':
    pass
