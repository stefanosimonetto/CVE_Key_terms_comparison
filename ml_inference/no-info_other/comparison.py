import numpy as np
import json
from sklearn.metrics import classification_report

with open('no-info_other/comparison_results_other_noinfo.json', 'r') as file:
    final_comparison_list = json.load(file)

y_test = np.array([item['CNA_cwe'] for item in final_comparison_list])
y_pred_original_descr = np.array([item['cwe_guessed_from_terms'] for item in final_comparison_list])

# Generate and print the classification report
print("Classification Report (no-info, other) from terms:\n", classification_report(y_test, y_pred_original_descr, digits=4))

    
y_test = np.array([item['CNA_cwe'] for item in final_comparison_list])
X_descr = np.array([item['Description'] for item in final_comparison_list])


y_pred_original_descr = np.array([item['cwe_guessed_from_descr'] for item in final_comparison_list])

# Generate and print the classification report
print("Classification Report (no-info, other) from descr:\n", classification_report(y_test, y_pred_original_descr, digits=4))
