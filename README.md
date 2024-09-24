# WhatsApp AI Chatbot

This project implements an AI-powered chatbot that interacts with WhatsApp Web. It uses OpenAI's GPT-3.5 model to generate responses and PyAutoGUI for automating interactions with the WhatsApp Web interface.

## Components

1. OpenAI Chat Completion Script
2. WhatsApp Web Automation Script
3. Mouse Position Tracker

## Features

- Integrates with WhatsApp Web to read and respond to messages
- Uses OpenAI's GPT-3.5 model to generate context-aware responses
- Automates mouse and keyboard actions to interact with the WhatsApp Web interface
- Includes a utility to track mouse positions for setup

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- pip (Python package manager)
- Google Chrome browser
- WhatsApp Web account
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/whatsapp-ai-chatbot.git
   ```
2. Navigate to the project directory:
   ```
   cd whatsapp-ai-chatbot
   ```
3. Install the required packages:
   ```
   pip install openai pyautogui pyperclip
   ```

## Configuration

1. OpenAI API Key: Replace `"Your OpenAI API Key"` in both script files with your actual OpenAI API key.
2. Screen Coordinates: You may need to adjust the hardcoded screen coordinates in the WhatsApp Web automation script to match your screen resolution and browser window position.

## Usage

1. Open Google Chrome and log into WhatsApp Web.
2. Ensure the WhatsApp Web window is positioned correctly on your screen.
3. Run the WhatsApp Web automation script:
   ```
   python whatsapp_automation.py
   ```
4. The script will continuously monitor for new messages and respond when appropriate.

## Mouse Position Tracker

To help with setting up the correct screen coordinates, use the mouse position tracker:

1. Run the mouse position tracker script:
   ```
   python mouse_tracker.py
   ```
2. Move your mouse to the desired positions on the WhatsApp Web interface and note the coordinates.
3. Update the coordinates in the WhatsApp Web automation script accordingly.

## How It Works

1. The script clicks on the Chrome icon to focus the WhatsApp Web window.
2. It selects and copies the latest chat messages.
3. The chat history is analyzed to determine if the last message is from the target sender.
4. If so, the OpenAI API is used to generate a response based on the chat history.
5. The response is pasted into the WhatsApp Web input field and sent.

## Customization

- Modify the system prompts in the OpenAI API calls to change the bot's personality or behavior.
- Adjust the sleep times in the automation script to match your system's performance and network speed.

## Dependencies

- [openai](https://github.com/openai/openai-python): For interacting with OpenAI's GPT models.
- [pyautogui](https://pyautogui.readthedocs.io/): For automating mouse and keyboard actions.
- [pyperclip](https://pypi.org/project/pyperclip/): For cross-platform clipboard operations.

## Additional Resources

1. [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
2. [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)
3. [WhatsApp Web](https://web.whatsapp.com/)

## Troubleshooting

- If the automation is not clicking on the correct positions, re-run the mouse position tracker and update the coordinates.
- Ensure that your WhatsApp Web is logged in and the chat window is open before running the script.
- If you encounter OpenAI API errors, check your API key and quota.

## Ethical Considerations and Disclaimer

This project automates interactions on WhatsApp Web and uses AI to generate responses. Please consider the following:

1. Ensure you have permission from your chat partners to use an AI bot.
2. Be aware of WhatsApp's terms of service regarding automated interactions.
3. The AI may generate unexpected or inappropriate responses. Use with caution.
4. This tool should not be used for spamming or any malicious purposes.

The authors are not responsible for any misuse of this software or violations of terms of service.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/yourusername/whatsapp-ai-chatbot/issues) if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
