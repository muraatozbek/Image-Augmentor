import Augmentor
#importing Augmentor for useage
p = Augmentor.Pipeline("/path/to/images/folder/foto")
#path file of photos that we want to make Augmentation
p.rotate(probability=1.0, max_left_rotation=5, max_right_rotation=10)
#probability means what probability of photos that we want to make this function
#if probability=1,means apply all photos this function if probability=0 dont 
#apply any photos this function
p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
p.flip_left_right(probability=0.4)
p.flip_top_bottom(probability=0.8)
p.rotate90(probability=0.1)
p.black_and_white(probability=0.3, threshold=128)

p.sample(25) #how many similar images you want


