import os

def init():
    try:
        os.mkdir('/var/monit')
    except:
        print("Directory already exist")
