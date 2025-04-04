import os
from agent import app, initial_state, load_srt  # Import from agent.py

# Configuration
OPENAI_API_KEY = "your-openai-api-key-here"  # Replace with your actual key
SRT_FILE = "./sampels/input.srt"  # Path to your input SRT file
REFERENCE_AUDIO = "./sampels/en_sample.wav"  # Path to your reference audio file
TARGET_LANGUAGE = "ru"  # Target language code (e.g., "ru" for Russian)
CONFIG = {"recursion_limit": 100}  # Workflow config

def main():
    """
    Main function to run the SRT translation and audio generation agent.
    """
    # Validate input files
    if not os.path.exists(SRT_FILE):
        print(f"Error: SRT file not found at {SRT_FILE}")
        return
    
    if not os.path.exists(REFERENCE_AUDIO):
        print(f"Error: Reference audio file not found at {REFERENCE_AUDIO}")
        return
    
    # Set OpenAI API key as environment variable (if required by your agent)
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    
    try:
        # Load SRT data
        print(f"Loading SRT file: {SRT_FILE}")
        srt_data = load_srt(SRT_FILE)
        print(f"Loaded {len(srt_data)} subtitles")
        
        # Initialize agent state
        state = initial_state(
            srt_data=srt_data,
            target_language=TARGET_LANGUAGE,
            reference_audio_path=REFERENCE_AUDIO
        )
        
        # Run the agent
        print("Starting agent processing...")
        result = app.invoke(state, config=CONFIG)
        
        # Output results
        print(f"Process completed successfully!")
        print(f"Translated SRT saved to: {result['srt_file_path']}")
        print(f"Dubbed audio saved to: {result['audio_file_path']}")
        
    except Exception as e:
        print(f"Error during processing: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()