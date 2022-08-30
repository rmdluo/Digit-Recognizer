# digit-recognizer
This predicts handwritten digits. For example, if there is a handwritten 2, it will predict it is a 2. Note that it is not perfect and will not always predict correctly.

# How to use
Download all of the files
Unzip numbers.zip and data.zip  
Setup python (see below)  
In the command line, navigate to the digit recognizer folder.
Run digit_recognizer_model.py with python digit_recognizer_model.py (or just use the model that comes in the zip file)
Now you can run number_recognizer.py or digit_recognizer.py which can predict user submitted numbers (examples in numbers.zip)
Note that the numbers have to be put into a numbers folder

# Python setup
Download the python 3 distribution from https://www.python.org/downloads/  

pip install numpy  
pip install tensorflow  
pip install keras  
pip install mlxtend  
pip install opencv-python

# digit_recognizer_model.py
This sets up the model using a CNN.  
Note that this takes a long time to set up (it took around 15 minutes for me).  

# digit_recognizer.py
This only works with one digit.  
This prompts the user for a filename.  
The file should be in the numbers folder so that it can be found.  

# number_recognizer.py
This works with only two digit numbers.  
This works similarly to digit_recognizer.py.  
It splits it into two digits and then predicts both of the digits.  
The file should be in the numbers folder so that it can be found.  
