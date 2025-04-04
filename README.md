
This repository houses an AI-powered tool designed to streamline the process of translating and dubbing subtitles. Using **OpenAI's GPT-3.5** for accurate subtitle translation and **XTTS** for high-quality text-to-speech generation, this project automates the creation of dubbed audio that seamlessly aligns with the original video timings. Key features include:

- **Efficient Processing**: Handles large SRT files by translating them in manageable chunks.
- **Audio Synchronization**: Adjusts generated audio to match the original subtitle timings for a natural viewing experience.
- **Robust Design**: Incorporates error handling and debugging tools to ensure smooth operation and easy troubleshooting.

The codebase is organized into core components:
- **`agent.py`**: Manages the workflow, orchestrating translation and audio generation.
- **`main.py`**: Serves as the entry point, handling file inputs and configuration.
- **`xtts_voice.py`**: Provides utilities for XTTS-based audio generation, including voice conditioning with reference audio.
