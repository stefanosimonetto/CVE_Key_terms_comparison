import pickle
import numpy as np
from sklearn.metrics import classification_report
import joblib
from sklearn.preprocessing import LabelEncoder
# Save the best model
with open('phi_terms_comp_test.pickle', 'rb') as f2:
    unbalanced = pickle.load(f2)

X_test = np.array([item['cve_terms_phi'] for item in unbalanced if item['cwe'] != 'None'])
y_test = np.array([item['cwe'] for item in unbalanced if item['cwe'] != 'None'])

best_model=joblib.load('best_model_terms.joblib')
label_encoder_train=joblib.load('label_encoder_train_terms.joblib')

# Make predictions on the test set
y_pred_probs = best_model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

y_pred_original = label_encoder_train.inverse_transform(y_pred)

print("Classification Report phi-2:\n", classification_report(y_test, y_pred_original, digits=4))