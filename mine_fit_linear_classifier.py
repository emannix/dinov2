# PYTHONPATH=. python dinov2/run/eval/linear.py \
#     --config-file dinov2/configs/eval/vits14_pretrain.yaml \
#     --pretrained-weights pretrained/dinov2_vits14_pretrain.pth \
#     --output-dir eval/linear \
#     --train-dataset ImageNet:split=TRAIN:root=/home/unimelb.edu.au/nbloomfield/Desktop/phd-data/imagenet_subsets/imagenette2/:extra=extra/ \
#     --val-dataset ImageNet:split=VAL:root=/home/unimelb.edu.au/nbloomfield/Desktop/phd-data/imagenet_subsets/imagenette2/:extra=extra/ \
#     --nodes 1 --ngpus 1
