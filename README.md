# dogBreedclassifier
The model is trained to determine the breed of different dogs. The model is trained using the weights of the MobileNet model and classify dogs amongs 120 different classes.

Steps to train the model from the start:
  1.Download the following dataset - http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar
  2.Open the generateDataset.py file and update the path variable. The python file will split the data into train and validdation dataset
  3. Open train_Model.pynb jupyter notebook and run the program. The jupyter notebook will generate the mode.h5 and model.json file.
  4. Open testModel.pynb to test the newly trained model.

Note - if you change the path or filename, update the corresponding variables in each jupyter notebook.

Steps to use my trained model (~0.80 accuracy)
  1. Put model.h5 , model.json and testModel.pynb and class_label.txt file in a smae folder (Do Not Rename the file)
  2. Open testModel.pynb and update the imageFile to the path of your test image.
  3. Run the program. The predicted breed of the dog would be printed on the terminal.
