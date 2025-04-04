#!/bin/bash

# Clone the repository (if applicable)
git clone https://huggingface.co/coqui/XTTS-v2

# Install necessary Python packages
pip install -U pip
pip install torch torchaudio librosa soundfile pydub openai langchain langgraph pysrt TTS==0.21.*


echo "Installation complete."
