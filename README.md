# Deep Learning API using Flask

### Implementation of a convolutional neural network using Keras-Tensorflow, data augmentation and transfer learning (VGG16 neural network), development of an API in Flask and deployment on Heroku Cloud. The neural network allows to classify if there is a brain tumor in magnetic resonance images

# What is transfer learning?
### Transfer learning is a machine-learning method where the application of knowledge obtained from a model used in one task can be reused as a foundation point for another task. 

### In this project a famous NN called VGG16 is used, the VGG16 network was trained with the ImageNet dataset that containing more thann 14 million high-resolution images beloging to 1000 differents lebels. Transfer Learning in our context was implemented with the use of the feature learning layers of VGG16 network, which was trained to classify a different problem than magnetic resonance of the brain. 

### Finaly, in the VGG16 structure, the 3 fully connected layers have been replaced by layers of 256, 128 and 2 neurons. 

# Dataset
### The dataset used is Brain Tumor Detection 2020 which is available on Kaggle (https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection)


