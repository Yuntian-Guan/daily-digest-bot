#Daily Digest Bot

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-In_Development-orange)](https://github.com/Yuntian-Guan/daily-digest-bot)

**Tired of checking the weather and stock market every morning? I built a bot to do it for me.**

This is an automated personal assistant that collects the information I care about every day (such as weather and Hong Kong stock index), and compiles it into a concise summary to send to me, allowing me to have all the information at my fingertips when I start my day.

## Current Features (Phase 1)
- Fetches **real-time weather** for Hong Kong from a public API.
- Fetches **major Hong Kong stock indices** (e.g., HSI, HSCEI).
- Sends a formatted **email digest** to my personal inbox at a scheduled time.
- Runs reliably as a **local Python script**.

## Tech Stack
*   **Language**: Python 3
*   **Key Libraries**:
    *   `requests` - For fetching data from APIs.
    *   `smtplib` & `email` - For sending emails.
    *   `schedule` - For task scheduling.
*   **Environment**: Local development (will be deployed to a cloud server in Phase 2).

## Project Structure
daily-digest-bot/
   ├── bot.py # Main logic script
   ├── config.example.py # Configuration file template (Do not submit real passwords!)
   ├── requirements.txt # Project dependency list
   └── README.md # This document

## Getting Started
1.  **Clone the repo**: `git clone https://github.com/Yuntian-Guan/daily-digest-bot.git`
2.  **Install dependencies**: `pip install -r requirements.txt`
3.  **Set up configuration**: Copy `config.example.py` to `config.py` and fill in your [email credentials and API keys].
4.  **Run the bot**: `python bot.py`

## Development Roadmap
- **Phase 1 (Current)**: Core functionality running locally.
- **Phase 2**: Deploy to a cloud server (e.g., Railway) for 24/7 operation.
- **Phase 3**: Add more data sources (GitHub trending, RSS feeds) and a web dashboard.

## Contributing
This is a personal learning project, but suggestions and feedback are always welcome!

---
*This project is part of my journey to learn Python and automation. Built with curiosity and coffee.*
