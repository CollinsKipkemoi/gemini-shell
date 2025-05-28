# Gemini Shell

A command-line interface for interacting with Google's Gemini AI model. This project provides a simple and interactive way to chat with the Gemini model directly from your terminal.

## Features

- Interactive chat interface with Gemini AI
- Conversation history management
- Context-aware responses
- Graceful error handling
- Clean exit with Ctrl+C

## Prerequisites

- Python 3.7 or higher
- Google API key for Gemini

## Installation

1. Clone the repository:

```bash
git clone https://github.com/CollinsKipkemoi/gemini-shell.git
cd gemini-shell
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

## Usage

Run the script:

```bash
python script.py
```

- Type your message and press Enter to chat with the AI
- Press Ctrl+C to exit the chat

## Project Structure

```
gemini-shell/
├── script.py          # Main application file
├── requirements.txt   # Project dependencies
├── .env              # Environment variables (not tracked in git)
└── README.md         # This file
```

## Dependencies

- `google-generativeai`: Google's official Gemini API client
- `python-dotenv`: Environment variable management
- `datetime`: Timestamp handling
- `json`: Data serialization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Google Gemini AI team for providing the API
- Python community for the excellent libraries used in this project
