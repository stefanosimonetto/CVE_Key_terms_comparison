#!/bin/bash
set -e
python main_comparison/cve_core/inference.py
python main_comparison/cve_all_terms/inference.py

python main_comparison/cve_core_consequences/inference.py
python main_comparison/cve_core_contextual/inference.py
python main_comparison/cve_descr_repl_subj/inference.py
python main_comparison/cve_description/inference.py

python bert_phi_comparison/bert/inference.py
python bert_phi_comparison/phi/inference.py
