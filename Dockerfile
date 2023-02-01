FROM mcr.microsoft.com/playwright:v1.30.0-focal

RUN apt update && apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update && apt install -y --no-install-recommends \
    python3.11 \
    python3.11-venv \
    python3-pip \
    && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Expose the ports
EXPOSE 3000

RUN python3.11 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
COPY requirements.txt /app/
RUN /opt/venv/bin/pip install -r requirements.txt

COPY . /app

CMD . /opt/venv/bin/activate && /opt/venv/bin/python main_sync.py