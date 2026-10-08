# AutoReply-Whatsapp-Bot

Python desktop automation prototype that reads WhatsApp Web chats and generates replies through OpenAI.

## Repository guide

### Contents

- [01_getcursor.py](01_getcursor.py)
- [02_openai.py](02_openai.py)
- [03_Bot.py](03_Bot.py)
- [README.md](README.md)
- [requirements.txt](requirements.txt)
- [tests](tests)

### Getting started

```bash
git clone https://github.com/Raimal-Raja/AutoReply-Whatsapp-Bot.git
cd AutoReply-Whatsapp-Bot
```

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r "requirements.txt"
```

Application entry point:

```bash
python 03_Bot.py
```

### Configuration and limitations

Requires a desktop session, calibrated screen coordinates, a selected chat, and an OpenAI API key. Live messaging was not run.

### Maintenance fixes

- Parse the final timestamped sender without assuming 2024.
- Avoid duplicate replies to an unchanged transcript.
- Read the OpenAI API key from OPENAI_API_KEY.

### Validation

Reviewed on 2026-10-08. Three transcript-parser regression tests passed. Python source syntax checks passed. Live desktop automation and message delivery were not exercised.

```bash
python -m unittest discover -s tests -v
```

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

No top-level license file was found during this review.
