
# Following is the ink to download the dataset
# http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar
# download the image data and update the path variable to the downloaded dataset


# this code will take a single folder dataset ad will split it into train and validation datset
# ratio can be changed to .8,.1,.1 to split the data into train validation and test instead

import split_folders
split_folders.ratio('Path_to_Dataset', output="Output_path", seed=1337, ratio=(.8, .2)) # default values

