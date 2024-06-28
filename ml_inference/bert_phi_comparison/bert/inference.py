import pickle
import numpy as np
from sklearn.metrics import classification_report
import joblib
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model

# Load the saved model
best_model = load_model('bert_phi_comparison/bert/best_model_terms.h5')
# Save the best model
with open('bert_phi_comparison/bert/bert_comparison_test.pickle', 'rb') as f2:
    unbalanced = pickle.load(f2)

X_test = np.array([item['cve_terms_bert_mean'] for item in unbalanced if item['cwe'] != 'None'])
y_test = np.array([item['cwe'] for item in unbalanced if item['cwe'] != 'None'])

# best_model=joblib.load('best_model_terms.joblib')
label_encoder_train=joblib.load('bert_phi_comparison/bert/label_encoder_train_terms.joblib')

# Make predictions on the test set
y_pred_probs = best_model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

y_pred_original = label_encoder_train.inverse_transform(y_pred)

print("Classification Report BERT terms (Table6):\n", classification_report(y_test, y_pred_original, digits=4))

X_test = np.array([item['cve_description_bert_mean'] for item in unbalanced if item['cwe'] != 'None'])
y_test = np.array([item['cwe'] for item in unbalanced if item['cwe'] != 'None'])

best_model=joblib.load('bert_phi_comparison/bert/best_model_descr.h5')
label_encoder_train=joblib.load('bert_phi_comparison/bert/label_encoder_train_descr.joblib')

# Make predictions on the test set
y_pred_probs = best_model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

y_pred_original = label_encoder_train.inverse_transform(y_pred)

print("Classification Report BERT descriptions (Table6):\n", classification_report(y_test, y_pred_original, digits=4))