import pickle
import numpy as np
from sklearn.metrics import classification_report
import joblib
from keras.models import load_model
# Load the saved model
best_model =  load_model('main_comparison/cve_all_terms/CWE_classes_class.h5')

# Load the label encoder
label_encoder_train = joblib.load('main_comparison/cve_all_terms/label_encoder_train_class.joblib')

# Load the test data
with open('main_comparison/cve_all_terms/test_terms.pickle', 'rb') as f2:
    unbalanced = pickle.load(f2)

X_test = np.array([item['cve_terms_ada_embedding'] for item in unbalanced if item['cwe_class'] != 'None'])
y_test = np.array([item['cwe_class'] for item in unbalanced if item['cwe_class'] != 'None'])

# Make predictions on the test set
y_pred_probs = best_model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

# Convert the predicted labels back to their original form
y_pred_original = label_encoder_train.inverse_transform(y_pred)

# Generate and print the classification report
print("Classification Report Key terms classes (Table4):\n", classification_report(y_test, y_pred_original, digits=4))