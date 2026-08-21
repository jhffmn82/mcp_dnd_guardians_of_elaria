# Signal Rome Bot - Deployment Guide

## Setup

### 1. Install signal-cli locally first

You need to set up signal-cli on your machine to link your Signal account:

```bash
# Download signal-cli (works on Windows, Mac, Linux)
# https://github.com/AsamK/signal-cli/releases

# Link your Signal account
signal-cli -u +YOUR_NUMBER link

# This generates a QR code - scan it with Signal on your phone to authorize
```

### 2. Configure environment variables

Copy `.env.example` to `.env` and fill in:

```
ANTHROPIC_API_KEY=sk-ant-...  # Get from https://console.anthropic.com/
SIGNAL_ACCOUNT_NUMBER=+1234567890  # Your Signal number (the bot's account)
TARGET_SIGNAL_NUMBER=+0987654321    # The person you're messaging
SIGNAL_CLI_PATH=signal-cli  # Or path to signal-cli binary if not in PATH
PORT=5000
ENABLE_SCHEDULER=true
```

### 3. Deploy to a cloud platform

#### Option A: Railway (recommended, free tier)

1. Install Railway CLI: `npm install -g @railway/cli`
2. Create account at railway.app
3. From this directory: `railway init`
4. Push to Railway: `railway up`
5. Railway will build and deploy automatically

Railway needs:
- Your `.env` variables (add in Railway dashboard under Variables)
- Your signal-cli to be available (see below)

#### Option B: Fly.io

1. Install Fly CLI: https://fly.io/docs/hands-on/install/
2. Create account at fly.io
3. From this directory: `flyctl launch`
4. Set secrets: `flyctl secrets set ANTHROPIC_API_KEY=...` etc.
5. Deploy: `flyctl deploy`

#### Option C: Docker (any cloud platform)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

# Install signal-cli dependencies
RUN apt-get update && apt-get install -y \
    openjdk-17-jre-headless \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Download signal-cli
RUN curl -L https://github.com/AsamK/signal-cli/releases/download/v0.12.10/signal-cli-0.12.10.tar.gz \
    | tar -xz -C /opt && \
    ln -s /opt/signal-cli-0.12.10/bin/signal-cli /usr/local/bin/signal-cli

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PORT=5000
EXPOSE 5000

CMD ["python", "main.py"]
```

## Important Notes

### signal-cli requires persistent storage

signal-cli stores account data in `~/.local/share/signal-cli/`. On deployment, you need:

- **For Railway/Fly.io**: Mount a persistent volume for signal-cli data
- **Or**: Link signal-cli locally, then copy the `.local/share/signal-cli` directory to your deployment

### Message polling

The bot polls Signal every 30 seconds for new messages. This is fine for casual messaging but could miss rapid-fire messages. For production, consider:
- Running signal-cli as a daemon with webhooks
- Using a queue system (Redis/RabbitMQ)

### Cost

- Claude API: ~$0.01 per message
- Hosting: Free tiers available (Railway, Fly.io)
- Signal: Free (runs through their servers)

## Testing locally

```bash
cp .env.example .env
# Edit .env with your values
pip install -r requirements.txt
python main.py
```

Visit http://localhost:5000/health to verify it's running.

## Troubleshooting

**"signal-cli: command not found"**
- signal-cli isn't in PATH. Set `SIGNAL_CLI_PATH` to full path in .env

**"Device not linked"**
- Run `signal-cli -u +YOUR_NUMBER link` to authorize with Signal on your phone

**No messages received**
- Check that TARGET_SIGNAL_NUMBER is correct
- Verify signal-cli can send: `signal-cli -u +YOUR_NUMBER send -m "test" +TARGET_NUMBER`

**Claude not responding**
- Verify ANTHROPIC_API_KEY is set and valid
- Check Flask logs for API errors
