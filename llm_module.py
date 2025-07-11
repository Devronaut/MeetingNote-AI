import ollama
import re 





def generate_meeting_minutes(transcription):
    system_message = """You are an expert assistant specializing in generating concise and actionable meeting minutes from audio transcripts. Your goal is to extract meaningful insights, key discussions, and actionable next steps from the provided text, even with potentially limited information."""

    user_prompt = f"""Generate meeting minutes from the following transcript. Focus on extracting:
    1. Key Discussion Points
    - Main topics discussed
    - Important insights
    - Significant conversations
    2. Takeaways
    - Core learnings
    - Critical insights
    - Strategic implications
    3. Action Items
    - Specific tasks or next steps
    - Prioritize clear, actionable items
    - Include any suggested responsibilities (if mentioned)
    Transcript:
    {transcription}
    Guidelines:
    - Never add placeholders like '[Insert Date]' or '[Name]'
    - Be concise and precise
    - Extract value even from fragmented conversation
    - Prioritize actionable information
    - Use markdown formatting
    - If information is unclear or missing, note it appropriately"""

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt}
    ]
    MODEL='deepseek-r1'
    response = ollama.chat(model=MODEL, messages=messages)
    result=response['message']['content']
    meeting_minutes = re.sub(r'<think>.*?</think>', '', result, flags=re.DOTALL)
    return meeting_minutes