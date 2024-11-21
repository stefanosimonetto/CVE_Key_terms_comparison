import pickle
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# Load the pickle file
with open('main_comparison/gpt_api_calls/updated_test_gpt_baseline_final.pickle', 'rb') as file:
    data = pickle.load(file)

# Initialize lists for predictions and ground truth labels
true_cwe = []
predicted_cwe = []

# Extract the cwe and guessed_cwe from the data, filtering out None values
for item in data:
    if item['cwe'] is not None and item['guessed_cwe'] is not None:
        true_cwe.append(item['cwe'])
        predicted_cwe.append(item['guessed_cwe'])

# Initialize LabelEncoder
le = LabelEncoder()

# Fit and transform the text labels
all_labels = list(set(true_cwe + predicted_cwe))  # Get all unique labels
le.fit(all_labels)

# Convert text labels to integers
true_cwe_encoded = le.transform(true_cwe)
predicted_cwe_encoded = le.transform(predicted_cwe)

# Define target names from the encoder
target_names = le.classes_

# Generate the classification report
report = classification_report(true_cwe_encoded, predicted_cwe_encoded, target_names=target_names, zero_division=0, digits=4)
print("ChatGPT (API call):")

print(report)