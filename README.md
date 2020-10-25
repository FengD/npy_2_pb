# npy_2_pb

## Description
This file is used to transform the npy file to pb file.
And I create this file especially for the [Squeezeseg project](https://github.com/BichenWuUCB/SqueezeSeg).
The author of SqueezeSeg transform the kitti data to [lidar_2d](https://www.dropbox.com/s/pnzgcitvppmwfuf/lidar_2d.tgz?dl=0) as he mentioned in his [paper](https://arxiv.org/abs/1710.07368). This dataset contains LiDAR point-cloud projected to a 2D spherical surface. Refer to our paper for details of the data conversion procedure.

And I create the script in the project to transform his `.npy` file type to the `.pb` file type which could be used in tensorflow.

## Dependencies
* tensorflow
* numpy
* glob

## Tips
For the line 22, if you meet the error below:
```
AttributeError: module 'tensorflow' has no attribute 'reset_default_graph'
```
Flow this [link](https://blog.csdn.net/robot_123/article/details/103131567)

Just change
```
import tensorflow as tf
```
to
```
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
```
