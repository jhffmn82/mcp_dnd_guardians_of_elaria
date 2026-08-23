FROM eclipse-temurin:25-jre-noble

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-venv curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://github.com/AsamK/signal-cli/releases/download/v0.14.7/signal-cli-0.14.7.tar.gz \
    | tar -xz -C /opt \
    && ln -s /opt/signal-cli-0.14.7/bin/signal-cli /usr/local/bin/signal-cli

WORKDIR /app
COPY requirements.txt .
RUN python3 -m venv /venv && /venv/bin/pip install --no-cache-dir -r requirements.txt

COPY main.py signal_handler.py ./
ENV PATH="/venv/bin:$PATH"

CMD ["python", "main.py"]
