import datetime
import psutil
import socket
import json
import uuid

def check_ram():
    return psutil.virtual_memory().percent


def check_cpu():
    return psutil.cpu_percent()


def check_disk():
    return psutil.disk_usage("/").percent


def check_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    f = open("monit_conf.json", "r")
    data = json.load(f)
    lst_ports = data["CHECK_PORTS"]
    for port in lst_ports:
        result = sock.connect_ex(("127.0.0.1", port))
        if result == 0:
            return True
        else:
            return False

def check():
    f = open(f"/var/monit/check_{datetime.datetime.now()}.json", "a")
    f.write(f"Date : {datetime.datetime.now()}\n")
    f.write(f"ID : {uuid.uuid4()}\n")
    f.write(f"CPU : {check_cpu()}\n")
    f.write(f"RAM : {check_ram()}\n")
    f.write(f"Disk : {check_disk()}\n")
    f.write(f"Port : {check_port()}\n")
    f.close()

