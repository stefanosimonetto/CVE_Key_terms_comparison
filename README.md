# CVE Key Terms Comparison

## Description
In this project, we investigate the extent to which key information can be extracted from CVE descriptions and how this improves the identification of related weaknesses. The primary challenge lies in the unstructured nature of CVE descriptions and their specificity toward the product and version affected by the vulnerability. We present a novel approach that automates the extraction of key terms representative of CVEs using a pipeline involving ChatGPT. By leveraging careful prompt engineering, we eliminate the need for expert involvement, making the process efficient and scalable.

The main question we answer in this work is: "Which parts of a CVE description contain the most useful information to automate mapping CVEs to their corresponding CWEs?" We analyze and compare various strategies for extracting key parts from CVE descriptions (e.g., complete description, key terms only, description without the subject) to determine their effectiveness in accurately associating the CVE key information with the relevant CWE.

## Running the Artifact
To test the artifact, follow these steps (note that creating the Docker container will take time because the dataset is large):

```sh
git clone https://github.com/stefanosimonetto/CVE_Key_terms_comparison.git

cd ml_inference

docker build -t test_inference .

docker run test_inference

```

## dataset availability
The complete dataset is available and can be accessed at: https://drive.google.com/drive/folders/13i4sKSNiHIWU0mQ_MVe1lansIHt-1xKJ?usp=drive_link

# NOTE: If you want to train the models with the same dataset, the results may slightly differ due to the randomness in the initialization of the neural network.


