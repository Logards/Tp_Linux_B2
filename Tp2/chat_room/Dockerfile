FROM rockylinux:9

RUN dnf update -y && dnf install -y \
    python3 \
    python3-pip 

WORKDIR /chat_room
COPY chat.py /chat_room

ENTRYPOINT [ "python3", "chat.py" ]