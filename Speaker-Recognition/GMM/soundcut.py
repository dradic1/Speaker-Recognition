from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

def SoundCut(input_audio_path):
    song = AudioSegment.from_wav(input_audio_path)
    
    chunks = split_on_silence(
        # Use the loaded audio.
        song, 
        # Specify that a silent chunk must be at least 1 second or 1000 ms long.
        min_silence_len=1000,
        # Consider a chunk silent if it's quieter than -45 dBFS.
        # (You may want to adjust this parameter.)
        silence_thresh=-45
    )

    for i, chunk in enumerate(chunks):
        # Create a silence chunk that's 0.1 seconds (or 100 ms) long for padding.
        silence_chunk = AudioSegment.silent(duration=100)

        # Add the padding chunk to beginning and end of the entire chunk.
        audio_chunk = silence_chunk + chunk + silence_chunk

        # Normalize the entire chunk.
        #normalized_chunk = match_target_amplitude(audio_chunk, -30.0)
        normalized_chunk = audio_chunk.set_channels(1)
        
        # Export the audio chunk with new bitrate.
        output_path = os.path.splitext(input_audio_path)[0] + f"_chunk{i}.wav"
        print(f"Exporting {output_path}.")
        audio_chunk.export(
            output_path,
            bitrate="44.1k",
            format="wav"
        )

