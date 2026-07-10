# Evaluating Robust Retrieval Pipelines

**An undergraduate engineering thesis investigating the robustness of Information Retrieval (IR) pipelines against query variations.**

## Overview

Modern search engines increasingly rely on Pretrained Language Models (PLMs) to rank documents. However, these models are typically benchmarked against a single standard query. This repository contains the code and evaluation pipelines for my thesis, which asks: *How brittle are these advanced ranking architectures when users ask the exact same question in a slightly different way?*

By generating adversarial and semantic query variations on industry-standard datasets, this project demonstrates that state-of-the-art models can silently fail, suffering an approximate **45% drop** in retrieval effectiveness when processing non-standard queries that maintain exact semantic meaning.

## Key Features

* **Query Variation Generation:** Includes logic for LLM-driven paraphrasing and lexical/morphological perturbations (e.g., lemmatization, character deletion to mimic typos).
* **Evaluation Pipeline:** Scripts to evaluate generated variations across a spectrum of IR models:
* *Traditional:* BM25, RM3
* *Neural:* KNRM, Conv-KNRM
* *PLMs:* BERT, EPIC, T5


* **Data Wrangling:** Processing and cleaning query variations utilizing `ir_datasets` and `pandas` on the **MS MARCO** and **ANTIQUE** datasets.
* **Resilient Execution:** Engineered specifically for Google Colab, featuring continuous state checkpointing and serialization to Google Drive to seamlessly recover from session timeouts during heavy GPU workloads.

## Repository Structure

* `notebooks/` - Jupyter notebooks containing the query generation, perturbation logic, and evaluation loops.
* `scripts/` - Data pipeline utilities for downloading, chunking, and memory-optimizing MS MARCO/ANTIQUE indexes.
* `results/` - Aggregated CSVs tracking query provenance (misspellings, naturality, paraphrasing) and quantifying model performance degradation.

## Getting Started

This project was designed to be executed in Google Colab to leverage free GPU compute for the deep learning models.

1. Clone this repository or copy the notebooks directly into your Google Drive.
2. Open the evaluation notebooks in Google Colab.
3. Ensure you mount your Google Drive to maintain state and save checkpoints during model evaluation:
```python
from google.colab import drive
drive.mount('/content/gdrive/')

```


4. Install the required data handling dependencies:
```bash
pip install pandas ir_datasets

```



## Author

Developed as part of a Bachelor of Engineering (Honours) in Computer Systems / Electrical and Electronic Engineering at the University of Queensland.

*The full thesis document and extended analysis are available upon request.*