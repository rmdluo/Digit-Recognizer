# digit-recognizer
This predicts handwritten digits. For example, if there is a handwritten 2, it will predict it is a 2. Note that it is not perfect and will not always predict correctly. This is simply me learning convolutional neural networks (CNNs).

# How to use
Download all of the files  
Unzip numbers.zip and data.zip  
Setup python (see below)  
Run digit_recognizer_model.py  
Now you can run number_recognizer.py or digit_recognizer.py which can predict user submitted numbers (examples in numbers.zip)  

# Python setup
Download the python 3 distribution from https://www.python.org/downloads/  
Download the anaconda distribution from https://www.anaconda.com/distribution/
pip install numpy  
pip install tensorflow  
pip install keras  
pip install mlxtend  
Note that Python 3.7 and above no longer support tensorflow

# digit_recognizer_model.py
This sets up the model using a CNN with 4 Conv2D layers and 2 Dense layers.  
Note that this takes a long time to set up (it took around an hour for me).  

# digit_recognizer.py
This only works with one digit.  
This prompts the user for a filename.  
The file should be in the numbers folder so that it can be found.  

# number_recognizer.py
This works with only two digit numbers.  
This works similarly to digit_recognizer.py.  
It splits it into two digits and then predicts both of the digits.  
The file should be in the numbers folder so that it can be found.  
