import os
import os.path as osp
import argparse
import sys
import math
import numpy as np

# def ArgumentParser():
#     parser = argparse.ArgumentParser(description='generate txt file')
#     parser.add_argument('--dataset', choices=['mouss_seq1', 'mbari_seq0', 'habcam_seq0'])
#     return parser.parse_args()

def generate_txt(dataset, fnames = None):
    DIR = osp.join('/home/pwhuang/data/VOCdevkit', dataset, 'ImageSets')
    if not osp.exists(DIR):
        os.mkdir(DIR)
    if not osp.exists(osp.join(DIR, 'Main')):
        os.mkdir(osp.join(DIR, 'Main'))

    if fnames == None:
        fnames = os.listdir(DIR.replace('ImageSets', 'Annotations'))
        fnames = [fname.replace('.xml', '') for fname in fnames]
        if 'Thumbs.db' in fnames:
            fnames.remove('Thumbs.db')

    length = len(fnames)
    print('\n=============== [file statistic] ===============')
    print("destination: {}".format(DIR))
    print('training: {}'.format(math.floor(length * 0.8)))
    print('testing: {}'.format(length - math.floor(length * 0.8)))

    np.random.seed(5)
    np.random.shuffle(fnames)

    with open(os.path.join(DIR, 'Main', 'train.txt'), 'w') as f:
        up_bound = math.floor(length * 0.8)
        f.write('\n'.join(fnames[:up_bound]))

    with open(os.path.join(DIR, 'Main', 'val.txt'), 'w') as f:
        low_bound = math.floor(length * 0.8) 
        # up_bound = math.floor(length * 0.8)
        f.write('\n'.join(fnames[low_bound:]))

    with open(os.path.join(DIR, 'Main', 'trainval.txt'), 'w') as f:
        up_bound = math.floor(length * 0.8)
        f.write('\n'.join(fnames))

    with open(os.path.join(DIR, 'Main', 'test.txt'), 'w') as f:
        low_bound = math.floor(length * 0.8)
        f.write('\n'.join(fnames[low_bound:]))

if __name__ == "__main__":
    generate_txt(sys.argv[1])

