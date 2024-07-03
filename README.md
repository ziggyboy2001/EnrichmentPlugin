# LinkedIn Data Enrichment Chrome Extension

## Overview

This project consists of a Chrome extension and a Python backend service that enriches LinkedIn profile data by scraping email addresses from relevant web pages.

## Project Structure

lead-scraping-extension/
│
├── chrome-extension/
│ ├── manifest.json
│ ├── content.js
│ ├── background.js
│ ├── popup.html
│ ├── popup.js
│ └── styles.css
│
├── backend/
│ ├── server.py
│ ├── requirements.txt
│ └── scraper.py
│
└── README.md

To set Up and Run the Backend:

    1.	Navigate to the backend directory:

    cd backend

    2.	Create a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    3.	Install the dependencies:

    pip install -r requirements.txt

    4.	Run the server:

    python server.py

Load and Test the Chrome Extension

    1.	Navigate to chrome://extensions/ in Chrome.
    2.	Enable Developer Mode.
    3.	Click “Load unpacked” and select the chrome-extension directory.
    4.	Navigate to a LinkedIn profile and test the extension.

Summary

This guide covers the entire process of using this Chrome extension that integrates with a Python backend for data enrichment. By following these steps, you’ll have a Chrome extension that detects LinkedIn profiles, communicates with a Python backend to enrich data, and displays the data in a user-friendly UI.
