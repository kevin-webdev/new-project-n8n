import subprocess

def generate_video(image_path, audio_path, output_path):
    subprocess.run([
        "ffmpeg", "-y",
        "-loop", "1", "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264", "-c:a", "aac",
        "-tune", "stillimage", "-shortest",
        "-pix_fmt", "yuv420p",
        "-vf", "scale=1080:1920",
        output_path
    ])

def add_music(video_path, music_path, output_path):
    subprocess.run([
        "ffmpeg", "-y",
        "-i", video_path, "-i", music_path,
        "-filter_complex", "[1:a]volume=0.2[a1];[0:a][a1]amix=inputs=2:duration=shortest",
        "-c:v", "copy", "-shortest",
        output_path
    ])

def crop_to_vertical(input_path, output_path):
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path,
        "-vf", "crop=in_h*9/16:in_h:(in_w-out_w)/2:0",
        output_path
    ])
