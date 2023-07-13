from dinov2.data.datasets import ImageNet
from pdb import set_trace as pb

root = '/home/unimelb.edu.au/nbloomfield/Desktop/phd-data/imagenet_subsets/imagenette2/'
extra = 'extra/'

for split in ImageNet.Split:
    dataset = ImageNet(split=split, root=root, extra=extra)
    dataset.dump_extra()

