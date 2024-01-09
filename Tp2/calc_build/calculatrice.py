import argparse
import socket
import logging
import select
import os

import colorlog

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('/var/log/bs_server/bs_server.log', 'w', 'utf-8')
file_handler.setLevel(logging.INFO)
stream_handler = colorlog.StreamHandler()
stream_handler.setLevel(logging.INFO)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

host = ''
parser = argparse.ArgumentParser(description="Usage: allows you to communicate with a server")
parser.add_argument("-p", "--port", action="store", help="change the default port by the argument")
args = parser.parse_args()
if os.environ.get('CALC_PORT') is not None:
    port = int(os.environ.get('CALC_PORT'))
if args.port is None:
    port = 13337
elif int(args.port) < 0 or int(args.port) > 65535:
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif int(args.port) < 1025:
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)
else:
    port = int(args.port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
logging.info(f"Le serveur tourne sur {ip_address}:{port}")
while select.select([s], [], [], 60) == ([], [], []):
    logging.warning('Aucun client depuis plus de une minute.')
conn, addr = s.accept()
while True:
    try:
        data = conn.recv(1024)
        data = data.decode()
        if not data : break
        logging.info(f"Le client {addr[0]} a envoyé comme calcul {data}.")
        try:
            logging.info(f"La reponse du calcul est {eval(data)}.")
            envoie = "Hey mon frère !".encode()
            conn.sendall(envoie)
            logging.info(f"Réponse envoyée au client {addr[0]} : {envoie.decode()}.")
            conn.sendall(f"Voici la réponse à ton calcul : {eval(data)}")
        except SyntaxError:
            logging.error(f"Le calcul n'est pas bon")
            conn.sendall(f"Mon cher confrère tu ne sais pas écrire tes calculs")
    except socket.error:
        print("Error Occured.")
        exit(1)
conn.close()
exit()
