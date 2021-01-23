import subprocess
import os


def exifinfo(filename):
    if os.path.isfile(filename):
        return subprocess.getoutput("exiftool "+filename)
    else:
        return "File not found."