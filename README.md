# AI Meeting Minutes Generator

An intelligent application that automatically generates structured meeting minutes from audio recordings. The system records meetings in real-time, transcribes the audio using advanced speech recognition, and then creates organized meeting minutes with key discussion points, takeaways, and action items.

## Purpose

This application solves the common problem of manually taking meeting notes by:
- **Automating the process** of capturing and documenting meetings
- **Providing structured output** that highlights important information
- **Saving time** by eliminating manual note-taking during meetings
- **Ensuring consistency** in meeting documentation format
- **Maintaining privacy** by processing everything locally on your machine

## Technologies Used

### Core AI Technologies
- **OpenAI Whisper Medium**: Advanced speech-to-text transcription with CUDA acceleration
- **Deepseek LLM**: Large language model for intelligent meeting summarization and analysis
- **Ollama**: Local deployment platform for running the Deepseek model

### Development Framework
- **Gradio**: Web-based user interface for easy interaction
- **PyTorch**: Machine learning framework with CUDA support for GPU acceleration
- **Transformers**: Hugging Face library for loading and running the Whisper model

### Audio Processing
- **PyAudio**: Real-time audio recording and capture
- **Wave**: Audio file format handling and storage
- **NumPy**: Numerical processing for audio data

### System Architecture
- **Multi-threaded Design**: Non-blocking audio recording with background processing
- **Modular Structure**: Separate modules for audio processing, language model, and main application
- **Local Processing**: Complete privacy with no cloud dependencies

## Key Features

- **Real-time Recording**: High-quality audio capture (44.1kHz, 16-bit, mono)
- **GPU Acceleration**: CUDA-enabled processing for faster transcription
- **Structured Output**: Automatically organized into Key Discussion Points, Takeaways, and Action Items
- **Web Interface**: User-friendly browser-based application
- **File Management**: Automatic timestamped file naming and storage
- **Cross-platform**: Works on Windows, macOS, and Linux
