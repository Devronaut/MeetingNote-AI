import os
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer, BitsAndBytesConfig ,AutoModelForSpeechSeq2Seq ,AutoProcessor ,pipeline
import torch




AUDIO_MODEL = "openai/whisper-medium"
speech_model = AutoModelForSpeechSeq2Seq.from_pretrained(AUDIO_MODEL, torch_dtype=torch.float16, use_safetensors=True)
speech_model.to('cuda')
processor = AutoProcessor.from_pretrained(AUDIO_MODEL)


def speech_to_text(audio_filename):
    

    pipe = pipeline(
        "automatic-speech-recognition",
        model=speech_model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch.float16,
        device='cuda',
    )


    result = pipe(audio_filename,return_timestamps=True)
    transcription = result["text"]
    return transcription