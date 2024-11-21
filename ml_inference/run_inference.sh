#!/bin/bash
set -e

python main_comparison/gpt_api_calls/inference.py
python main_comparison/cve_core/inference.py
python main_comparison/cve_all_terms/inference.py
python main_comparison/cve_core_consequences/inference.py
python main_comparison/cve_core_contextual/inference.py
python main_comparison/cve_descr_repl_subj/inference.py
python main_comparison/cve_description/inference.py

python main_comparison/cve_all_terms/inference_class.py
python main_comparison/cve_description/inference_class.py

python bert_phi_comparison/bert/inference.py
python bert_phi_comparison/phi/inference.py

python manual_terms_review/keybert_yake.py
python manual_terms_review/llama_gpt.py

python sota/inference.py
python no-info_other/comparison.py
