FROM debian
RUN apt update -y && apt install -y python3
RUN apt install -y python3-pip
RUN apt install python3-emoji -y
RUN mkdir /app
WORKDIR /app
COPY app.py /app/app.py
ENTRYPOINT [ "python3", "app.py" ]

