# Comparative Study of Artefacts in Modern AI-Generated Video Using MLLMs

**MSc Cyber Security Dissertation — University of Kent (COMP7300)**
**Author:** Shantanu Uday Vedante
**Supervisor:** Prof. Shujun Li

## Project Overview

A comparative study of artefacts in modern AI-generated video content, examined through multiple multimodal large language models (MLLMs). Two groups of generators are compared:

- **Open-weight text-to-video models** (self-hosted on Colab Pro): LTX-2.3, HunyuanVideo, Wan 2.7
- **Commercial state-of-the-art models** (via publicly-posted user samples): Kling 3.0, Veo 3.1, Runway Aleph 2.0

Four MLLMs act as analytical tools: Claude Opus 4.7, Gemini 2.0 Flash, Qwen2.5-VL, and LLaVA-1.6.

## Research Questions

**RQ1** — What visual and temporal artefact profiles emerge when multiple MLLMs analyse videos produced by different modern generation models, and how do these profiles compare between open-weight and commercial models?

**RQ2** — To what extent do different MLLMs agree in their identification and severity assessment of artefacts across generation sources?

**RQ3** — How does the detection accuracy and explanation quality of multiple MLLMs vary across generation sources, and what does this imply for MLLM-based forensic pipelines?

## Repository Structure
msc-deepfake-detection/
├── corpus/                    # Data and outputs for submission
│   ├── videos/                # Generated + curated videos (git-ignored due to size)
│   ├── metadata/              # Video metadata, prompt logs, source URLs
│   ├── mllm_outputs/          # Structured MLLM responses per model
│   └── results/               # Figures, tables, statistical outputs
├── code/                      # Source code
│   ├── generation/            # Video generation scripts (LTX, HunyuanVideo, Wan)
│   ├── analysis/              # MLLM analysis pipelines
│   ├── preprocessing/         # Frame extraction, face detection utilities
│   └── utils/                 # Shared utilities
├── dissertation/              # Dissertation drafts and final document
├── logbook/                   # Individual project logbook
└── supervisor_communication/  # Records of supervisor discussions

## Project Timeline

- **15–21 July:** Environment setup and pipeline verification
- **22–28 July:** Bulk video generation and commercial sample curation
- **29 July – 4 August:** MLLM analysis across all videos
- **5–11 August:** Cross-analysis, figures, statistics
- **12–20 August:** Corpus assembly + writing
- **21 August:** Corpus submission
- **22 August – 4 September:** Full dissertation writing, revisions, submission

## Reproducibility

Full reproducibility instructions are documented in each subdirectory README once code is added.

## Ethical Considerations

All video generation is done using publicly-available open-weight models under permissive licences. Commercial model outputs are sourced only from publicly-posted user content with clear attribution, and used solely for academic research.