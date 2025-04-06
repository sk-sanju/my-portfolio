def detect_mood(audio_file_path):
    # Your AI dev plugs their model here
    # Example return (mock)
    return {
        "mood": "calm",
        "confidence": 0.87
    }

def recommend_soundscape(mood):
    # Recommend based on detected mood
    mapping = {
        "calm": ["rainforest.mp3", "ocean_waves.mp3"],
        "happy": ["sunny_field.mp3", "birds_chirping.mp3"],
        "sad": ["gentle_piano.mp3"],
    }
    return mapping.get(mood, [])
