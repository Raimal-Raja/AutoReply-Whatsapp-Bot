"""Parse timestamped WhatsApp Web transcript lines without a fixed year."""
import re

MESSAGE_HEADER = re.compile(r'^\[[^\]\n]+\]\s*([^:\n]+):', re.MULTILINE)

def is_last_message_from_sender(chat_log, sender_name="Thy Professor Gb"):
    headers = list(MESSAGE_HEADER.finditer(chat_log))
    return bool(headers) and headers[-1].group(1).strip() == sender_name
