# da5402-a2-test
Testing done

# Multi-Modal Orchestrated Cluster – Part 1

## Developer B Responsibilities

### 1. Named Entity Recognition (NER)
- Endpoint: POST /ner
- Library: spaCy (en_core_web_sm)

### 2. Speech Synthesis (TTS)
- Endpoint: POST /tts
- Library: gTTS

---

## Setup Instructions

1. Create virtual environment:
python3.11 -m venv venv
source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt
3. Download spaCy model:
   python -m spacy download en_core_web_sm
4. Run server:
   uvicorn app.main:app --reload

---

## Collaboration Process

- Each feature developed in separate branch
- Pull Requests used for merging
- One intentional merge conflict created and resolved
- Conflict documented in CONFLICT.md
