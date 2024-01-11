import glob
import os


def list():
    for root, dirs, files in os.walk("/var/monit/check_*.json"):
        for file in files:
            print(file)