import os
import numpy as np
import librosa
import soundfile as sf

# Function to perform noise reduction using aggressive spectral gating
def reduce_noise(y, sr, noise_reduction_factor=0.1, n_iter=3):
    for _ in range(n_iter):
        # Compute the Short-Time Fourier Transform (STFT) of the audio signal
        stft = librosa.stft(y)
        stft_magnitude, stft_phase = librosa.magphase(stft)

        # Compute the mean magnitude spectrum of the noise
        noise_magnitude = np.mean(stft_magnitude[:, :int(sr * 0.1)], axis=1)
        
        # Create a mask that attenuates regions below the noise threshold
        mask = stft_magnitude > noise_reduction_factor * noise_magnitude[:, np.newaxis]
        
        # Apply the mask to the magnitude spectrogram
        stft_magnitude_denoised = stft_magnitude * mask
        
        # Inverse STFT to get the denoised signal
        stft_denoised = stft_magnitude_denoised * stft_phase
        y = librosa.istft(stft_denoised)
    
    return y

# Function to process all .wav files in a folder structure
def process_audio_files(input_folder, output_folder, noise_reduction_factor=10, n_iter=10):
    # Iterate through all files and subfolders in the input folder
    for root, _, files in os.walk(input_folder):
        # Create the corresponding output directory structure
        relative_path = os.path.relpath(root, input_folder)
        target_dir = os.path.join(output_folder, relative_path)
        os.makedirs(target_dir, exist_ok=True)
        
        for filename in files:
            if filename.endswith(".wav"):
                file_path = os.path.join(root, filename)
                print(f"Processing file: {file_path}")
                
                try:
                    # Load the audio file
                    y, sr = librosa.load(file_path)
                    
                    # Apply aggressive noise reduction
                    y_denoised = reduce_noise(y, sr, noise_reduction_factor=noise_reduction_factor, n_iter=n_iter)
                    
                    # Save the denoised audio signal in the target directory
                    output_file_path = os.path.join(target_dir, filename)
                    sf.write(output_file_path, y_denoised, sr)
                    print(f"Denoised audio saved to: {output_file_path}")
                
                except Exception as e:
                    # Print an error message and skip to the next file
                    print(f"Error processing {file_path}: {e}")
                    continue

# Define the input and output folders
input_folder = r"E:\Python_proj\ML_Project\musan\test"
output_folder = r"E:\Python_proj\ML_Project\musan\test_filtered"

# Process all audio files in the specified folder structure
process_audio_files(input_folder, output_folder, noise_reduction_factor=10, n_iter=10)
