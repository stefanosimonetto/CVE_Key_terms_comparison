import json
with open('manual_terms_review/expert_review.json', 'r') as file:
    data = json.load(file)

i=0
for item in data:
    if item["incompleteness"]["llama"]["core_terms"]["present"]==True :
            if item["incompleteness"]["llama"]["core_terms"]["word_present"]=="prod/vers" :
                i+=1

print("Llama subject core_terms presence:",i*100/len(data ))
i=0
for item in data:
    if item["incompleteness"]["gpt"]["core_terms"]["present"]==True :
            if item["incompleteness"]["gpt"]["core_terms"]["word_present"]=="prod/vers" :
                i+=1

print("GPT subject core_terms presence:",i*100/len(data ))

# --------------------------------

i=0
for item in data :
    if item["hallucinations"]["llama"]["core_terms"]["word"]!=""or item["hallucinations"]["llama"]["contextual_terms"]["word"]!="" or item["hallucinations"]["llama"]["consequences_terms"]["word"]!="":
        i+=1
print("Llama hallucination percentage:",i/len(data )*100)

i=0
for item in data :
    if item["hallucinations"]["gpt"]["core_terms"]["word"]!=""or item["hallucinations"]["gpt"]["contextual_terms"]["word"]!="" or item["hallucinations"]["gpt"]["consequences_terms"]["word"]!="":
        i+=1
print("GPT hallucination percentage:",i/len(data )*100)


# ----------------------------
i=0
for item in data :
    if item["incompleteness"]["llama"]["core_terms"]["present"]==True or item["incompleteness"]["llama"]["contextual_terms"]["present"]==True or item["incompleteness"]["llama"]["consequences_terms"]["present"]==True:
        if (item["incompleteness"]["llama"]["core_terms"]["word_present"]!="vuln" 
            and item["incompleteness"]["llama"]["consequences_terms"]["word_present"]!="vuln" 
            and item["incompleteness"]["llama"]["contextual_terms"]["word_present"]!= "vuln"
            and item["incompleteness"]["llama"]["core_terms"]["word_present"]!="prod/vers"
            and item["incompleteness"]["llama"]["consequences_terms"]["word_present"]!="prod/vers" 
            and item["incompleteness"]["llama"]["contextual_terms"]["word_present"]!="prod/vers" 
            and (item["incompleteness"]["llama"]["core_terms"]["word_missing"]!="" 
              or item["incompleteness"]["llama"]["consequences_terms"]["word_missing"]!="" 
              or item["incompleteness"]["llama"]["contextual_terms"]["word_missing"]!=""
              or (item["incompleteness"]["llama"]["core_terms"]["word_present"]!=""  
                  or item["incompleteness"]["llama"]["consequences_terms"]["word_present"]!="" 
                  or item["incompleteness"]["llama"]["contextual_terms"]["word_present"]!= ""  ))): 
                    i+=1

print("Llama completeness:",100-(i*100/len(data )))
i=0
for item in data :
    if item["incompleteness"]["gpt"]["core_terms"]["present"]==True or item["incompleteness"]["gpt"]["contextual_terms"]["present"]==True or item["incompleteness"]["gpt"]["consequences_terms"]["present"]==True:
        if (item["incompleteness"]["gpt"]["core_terms"]["word_present"]!= "vuln"  
            and item["incompleteness"]["gpt"]["consequences_terms"]["word_present"]!= "vuln"   
            and item["incompleteness"]["gpt"]["contextual_terms"]["word_present"]!= "vuln"   
            and item["incompleteness"]["gpt"]["core_terms"]["word_present"]!="prod/vers"   
            and item["incompleteness"]["gpt"]["consequences_terms"]["word_present"]!="prod/vers"  
            and item["incompleteness"]["gpt"]["contextual_terms"]["word_present"]!="prod/vers"  
            and (item["incompleteness"]["gpt"]["core_terms"]["word_missing"]!="" 
            or item["incompleteness"]["gpt"]["consequences_terms"]["word_missing"]!=""
            or item["incompleteness"]["gpt"]["contextual_terms"]["word_missing"]!="" 
            or (item["incompleteness"]["gpt"]["core_terms"]["word_present"]!="" 
                or item["incompleteness"]["gpt"]["consequences_terms"]["word_present"]!=""  
                or item["incompleteness"]["gpt"]["contextual_terms"]["word_present"]!=""  ))): 
                    i+=1

print("GPT completeness:",100-(i*100/len(data )))

# ----------------------------
i=0
for item in data :
    if item["inconsistency"]["gpt"]["core_terms"]["present"]==True :
                i+=1
print("gpt core consistency:",100-(i/len(data)*100))

i=0
for item in data :
    if item["inconsistency"]["llama"]["core_terms"]["present"]==True :
                i+=1
print("llama core consistency:",100-(i/len(data)*100))


i=0
for item in data :
    if item["inconsistency"]["gpt"]["contextual_terms"]["present"]==True :
                i+=1
print("gpt contextual consistency:",100-(i/len(data)*100))

i=0
for item in data :
    if item["inconsistency"]["llama"]["contextual_terms"]["present"]==True :
                i+=1
print("llama contextual consistency:",100-(i/len(data)*100))


i=0
for item in data:
    if item["inconsistency"]["gpt"]["consequences_terms"]["present"]==True :
                i+=1
print("gpt conseq' consistency:",100-(i/len(data)*100))

i=0
for item in data:
    if item["inconsistency"]["llama"]["consequences_terms"]["present"]==True :
                i+=1
print("llama conseq consistency:",100-(i/len(data)*100))