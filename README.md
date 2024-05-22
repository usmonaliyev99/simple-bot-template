# bot-template

## Overview

It is built using the aiogram library in Python.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Telegram Bot Token (get it from BotFather on Telegram)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/usmonaliyev99/simple-bot-template.git

cd simple-bot-template
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure the bot:

- Create a new Telegram bot on [BotFather](https://t.me/BotFather).
- Copy the provided environment variable template:

```bash
cp .env.example .env
```

4. Open the .env file and replace variables with the actual variables.

```bash
ENV=production or development

TELEGRAM_BOT_TOKEN=

WEBHOOK_HOST=
WEBHOOK_PATH=/aiogram/daily-post-publisher

WEBAPP_HOST=127.0.0.1
WEBAPP_PORT=4000

AUTH_USER=
AUTH_PASSWORD=
```

### Usage

Run the bot:

```bash
python main.py
```

### Setup project with systemd

* [Setup a python script as a service through systemctl/systemd](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267)

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
