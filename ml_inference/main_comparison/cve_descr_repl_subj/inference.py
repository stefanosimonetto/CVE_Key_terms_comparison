import pickle
import numpy as np
from sklearn.metrics import classification_report
import joblib
from keras.models import load_model

# Load the saved model
best_model = load_model('main_comparison/cve_descr_repl_subj/CWE_classes.h5')

# Load the label encoder
label_encoder_train = joblib.load('main_comparison/cve_descr_repl_subj/label_encoder_train.joblib')

# Load the test data
with open('main_comparison/cve_descr_repl_subj/test_repl_subj.pickle', 'rb') as f2:
    unbalanced = pickle.load(f2)

X_test = np.array([item['cve_description_replaced_subject_ada_embedding'] for item in unbalanced if item['cwe'] != 'None'])
y_test = np.array([item['cwe'] for item in unbalanced if item['cwe'] != 'None'])

# Make predictions on the test set
y_pred_probs = best_model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

# Convert the predicted labels back to their original form
y_pred_original = label_encoder_train.inverse_transform(y_pred)

# Generate and print the classification report
print("Classification Report CVE descrption with replaced subject (Table3):\n", classification_report(y_test, y_pred_original, digits=4))
