import numpy as np
import pickle
from sklearn.metrics import classification_report
from tensorflow.keras.models import load_model
import joblib



print('----------------------SOTA----------------------')
with open('sota/cnn_descr.txt', 'r') as f:
    content = f.read()

print('Classification Report textCNN description:')
print(content)
# ---------------------------------------------------------------
with open('sota/BigruCNN_descr.txt', 'r') as f:
    content = f.read()

print('Classification Report Bigru textCNN description:')
print(content)

# ---------------------------------------------------------------

with open('sota/cnn_terms.txt', 'r') as f:
    content = f.read()

print('Classification Report textCNN terms:')
print(content)
# ---------------------------------------------------------------
with open('sota/BigruCNN_terms.txt', 'r') as f:
    content = f.read()

print('Classification Report Bigru textCNN terms:')
print(content)