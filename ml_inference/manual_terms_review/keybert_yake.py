import json
with open('manual_terms_review/expert_review.json', 'r') as file:
    data = json.load(file)

i=0
for item in data:
    if item["extracted_keywords_keybert_subject_present"]==True :
                i+=1
print("Subject present in keybert keyword extraction:",i/len(data)*100)

i=0
for item in data:
    if item["extracted_keywords_yake_subject_present"]==True :
                i+=1
print("Subject present in yake keyword extraction:",i*100/len(data))

i=0
for item in data:
    if item["keybert cwe"]==True :
                i+=1
print("Info about CWE present in keybert keyword extraction:",i/len(data)*100)

i=0
for item in data:
    if item["yake cwe"]==True :
                i+=1
print("Info about CWE present in yake keyword extraction:",i*100/len(data))