# Comparative Study of Artefacts in Modern AI-Generated Video Using MLLMs

**MSc Cyber Security Dissertation (COMP7300)**  
**University of Kent**

**Author:** Shantanu Uday Vedante  
**Supervisor:** Prof. Shujun Li

---

## Abstract

This repository contains the code, experimental pipeline, metadata, and analysis framework for my MSc Cyber Security dissertation investigating artefacts in AI-generated videos using multiple Multimodal Large Language Models (MLLMs).

The study compares visual and temporal artefacts produced by:

- **Open-weight text-to-video models**
  - LTX-2.3
  - HunyuanVideo
  - Wan 2.7

against

- **Commercial state-of-the-art generators**
  - Kling 3.0
  - Veo 3.1
  - Runway Aleph 2.0

The generated videos are analysed using four independent MLLMs:

- Claude Opus 4.7
- Gemini 2.0 Flash
- Qwen2.5-VL
- LLaVA-1.6

The objective is to evaluate artefact detection consistency, explanation quality, and the suitability of MLLMs for future AI-generated media forensic pipelines.

---

# Table of Contents

- [Project Overview](#project-overview)
- [Research Questions](#research-questions)
- [Methodology](#methodology)
- [Repository Structure](#repository-structure)
- [Project Timeline](#project-timeline)
- [Installation](#installation)
- [Usage](#usage)
- [Experimental Pipeline](#experimental-pipeline)
- [Results](#results)
- [Reproducibility](#reproducibility)
- [Ethical Considerations](#ethical-considerations)
- [Citation](#citation)
- [Acknowledgements](#acknowledgements)

---

# Project Overview

Modern AI video generators have improved rapidly, yet generated videos still contain subtle spatial and temporal artefacts.

This dissertation investigates whether Multimodal Large Language Models can reliably identify these artefacts and whether different MLLMs agree on their presence and severity.

The work compares both open-source and commercial video generators under a unified evaluation framework.

---

# Research Questions

### RQ1

What visual and temporal artefact profiles emerge when multiple MLLMs analyse videos produced by different modern generation models, and how do these profiles compare between open-weight and commercial models?

### RQ2

To what extent do different MLLMs agree in their identification and severity assessment of artefacts across generation sources?

### RQ3

How does the detection accuracy and explanation quality of multiple MLLMs vary across generation sources, and what implications does this have for MLLM-based forensic pipelines?

---

# Methodology

The project consists of five main stages.

```
Text Prompt
      │
      ▼
Video Generation
(Open-weight Models)
      │
      ▼
Commercial Sample Collection
      │
      ▼
Video Pre-processing
(Frame Extraction)
      │
      ▼
MLLM Analysis
(Claude, Gemini, Qwen, LLaVA)
      │
      ▼
Artefact Extraction
      │
      ▼
Statistical Analysis
      │
      ▼
Dissertation Results
```

---

# Repository Structure

```
msc-deepfake-detection/
│
├── corpus/
│   ├── videos/
│   ├── metadata/
│   ├── mllm_outputs/
│   └── results/
│
├── code/
│   ├── generation/
│   ├── preprocessing/
│   ├── analysis/
│   └── utils/
│
├── dissertation/
│
├── logbook/
│
├── supervisor_communication/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Project Timeline

| Phase | Duration |
|---------|----------|
| Environment Setup | 15–21 July |
| Video Generation | 22–28 July |
| MLLM Analysis | 29 July – 4 August |
| Statistical Analysis | 5–11 August |
| Writing & Corpus Preparation | 12–20 August |
| Corpus Submission | 21 August |
| Dissertation Writing | 22 August – 4 September |

---

# Installation

Clone the repository.

```bash
git clone https://github.com/coderx0319/msc-deepfakedetection.git

cd msc-deepfake-detection
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Usage

## Generate Videos

```bash
python code/generation/generate_ltx.py

python code/generation/generate_hunyuan.py

python code/generation/generate_wan.py
```

---

## Extract Frames

```bash
python code/preprocessing/extract_frames.py
```

---

## Run MLLM Analysis

```bash
python code/analysis/run_claude.py

python code/analysis/run_gemini.py

python code/analysis/run_qwen.py

python code/analysis/run_llava.py
```

---

## Generate Figures

```bash
python code/analysis/statistics.py
```

---

# Experimental Pipeline

The complete workflow is:

1. Prompt selection
2. AI video generation
3. Commercial sample collection
4. Metadata recording
5. Frame extraction
6. MLLM inference
7. Artefact categorisation
8. Statistical comparison
9. Agreement analysis
10. Dissertation reporting

---

# Results

Experimental outputs will be stored in:

```
corpus/results/
```

including

- Statistical summaries
- Confusion matrices
- Agreement metrics
- Severity distributions
- Visualisations
- Tables used in the dissertation

---

# Reproducibility

Each experiment includes:

- Prompt used
- Generator version
- Model parameters
- Generation settings
- Random seed (where available)
- Metadata
- MLLM output
- Processing scripts

Complete reproduction instructions are documented within each subdirectory.

---

# Ethical Considerations

This research complies with University of Kent research ethics requirements.

- Open-weight models are used under their respective licences.
- Commercial samples are collected exclusively from publicly available user-posted demonstrations.
- No deceptive or malicious use of generated media is involved.
- The repository is intended solely for academic research into AI-generated media forensics.

---

# Citation

If you use this repository in your research, please cite:

```bibtex
@mastersthesis{vedante2026mllmvideo,
  author = {Shantanu Uday Vedante},
  title = {Comparative Study of Artefacts in Modern AI-Generated Video Using MLLMs},
  school = {University of Kent},
  year = {2026},
  type = {MSc Dissertation}
}
```

---

# Acknowledgements

This work was completed as part of the MSc Cyber Security programme at the University of Kent under the supervision of **Prof. Shujun Li**.

The project makes use of publicly available AI video generation models and Multimodal Large Language Models for academic research purposes.

---

## License

This repository is released for academic and research purposes.

Please refer to the `LICENSE` file for details.
