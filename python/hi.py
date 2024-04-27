import math
import os
import subprocess
import socket
folder_path="/home/user/Desktop/clanguage"

for filename in os.listdir(folder_path):
    if filename.endswith(".mp4"):
        filepath=os.path.join(folder_path,filename)
        cmd=f"ffprobe -v error -select_strems v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey1'{filepath}'"
        output=subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        duration=float(output)
        printf(f"{filename}:{duration}")
