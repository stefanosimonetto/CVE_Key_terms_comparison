import gdown

def download_file_from_google_drive(id, destination):
    url = f"https://drive.google.com/uc?id={id}"
    gdown.download(url, destination, quiet=False)

if __name__ == "__main__":
    file_ids = [
        '1hJfBpSZM3PVEMhZOfEqlAwIO-Esh0oUR',
        '1EnSCcDFH3NsFR_9v3ASlkvu4iV91UQ67',
        '1wKFze8g-nbPCSTpneSWDGh0dFOfrI65k',
        '1Lu350RIYg7Y9k0Fdax5WXFV0aohBbVGI',
        '1ecaKbYF1FzpTWHhFM-Kh3FOVtuMp4cyC',
        '1qiAzRM1wrD-XDWXDrlvMAQwrXOlRHy3T',
        '1Puf21VWSx5BhvlvlrTSjxm2bBD5YRpda',
        '16Bta2lYcaoJJKt_LzMbgA_yaLNvmc_KT',
        '134iKdIK1-z7mgyFP9f3dl7cUqk33m2Ao'

    ]
    destinations = [
        'bert_phi_comparison/bert/bert_comparison_test.pickle',
        'bert_phi_comparison/phi/phi_terms_comp_test.pickle',
        'main_comparison/cve_core_contextual/test_core_cont.pickle',
        'main_comparison/cve_core_consequences/test_core_cons.pickle',
        'main_comparison/cve_core/test.pickle',
        'main_comparison/cve_all_terms/test_terms.pickle',
        'main_comparison/cve_descr_no_subj/test_no_subj.pickle',
        'main_comparison/cve_descr_repl_subj/test_repl_subj.pickle',
        'main_comparison/cve_description/test.pickle'
        
    ]

    for file_id, destination in zip(file_ids, destinations):
        download_file_from_google_drive(file_id, destination)
