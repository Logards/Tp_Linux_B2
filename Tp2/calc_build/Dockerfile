FROM rockylinux:9

RUN dnf update -y && dnf install -y \
    python3 \
    python3-pip 

RUN pip install --upgrade pip 
RUN pip install colorlog 
RUN pip install psutil

WORKDIR /calc
COPY calculatrice.py /calc

RUN mkdir /var/log/bs_server -m 700 && touch /var/log/bs_server/bs_server.log && chmod 600 /var/log/bs_server/bs_server.log

ENTRYPOINT [ "python3", "calculatrice.py" ]