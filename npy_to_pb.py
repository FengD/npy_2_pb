import tensorflow as tf
import numpy as np
import glob
import os

if not os.path.exists('./data/pb'):
    os.makedirs('./data/pb')

val_files = [val_files.rstrip('\n') for val_files in open('./data/ImageSet/val.txt')]

val_file_list = ""
for f in val_files:
	in_path = os.path.join('./data/lidar_2d/', f + '.npy')
	out_path = os.path.join('./data/pb/', f + '.pb')

	ar_path = os.path.join('data/airunner/test/', f + '.pb')

	val_file_list += ar_path + '\n'

	lidar = np.load(in_path).astype(np.float32, copy=False)[np.newaxis]

	tf.reset_default_graph()
	tf.constant(lidar)

	graph_def = tf.get_default_graph().as_graph_def()
	with tf.gfile.GFile(out_path, 'wb') as pbf:
		pbf.write(graph_def.SerializeToString())

with open('./data/pb/val.txt', 'w+') as f:
	f.write(val_file_list)