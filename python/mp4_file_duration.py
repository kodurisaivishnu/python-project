import os
import subprocess

folder_path = '/home/user/Downloads/videos'

for filename in os.listdir(folder_path):
    if filename.endswith('.mp4'):
        video_path = os.path.join(folder_path, filename)
        # cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_path}'
        # try:
        #     output = subprocess.check_output(cmd, shell=True).decode('utf-8')
        #     duration = float(output.strip())
        #     print(f"{filename}: {duration} seconds")
        # except subprocess.CalledProcessError as e:
        #     print(f"Error while getting duration for {filename}")