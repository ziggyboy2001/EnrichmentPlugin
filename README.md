# LinkedIn Data Enrichment Chrome Extension

## Overview

This project consists of a Chrome extension and a Python backend service that enriches LinkedIn profile data by scraping user data and offering AI driven encancements and suggestions for each field.

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

    •	Scrape LinkedIn Profile Data: The scrape_linkedin_profile function in scraper.py scrapes the necessary details from the LinkedIn profile page.
    •	Prepare Data for ChatGPT: The scraped data is formatted into a string that summarizes the profile.
    •	Send Data to ChatGPT: The enrich_profile function in server.py sends the formatted profile data to the OpenAI API.
    •	Receive and Process Enhanced Data: The response from ChatGPT contains suggestions for enhancing the LinkedIn profile. This data is split into sections and sent back to the Chrome extension.
    •	Display Enhanced Data: The Chrome extension receives the enriched data and displays it in a user-friendly interface with three tabs, each containing suggestions for improving different aspects of the LinkedIn profile.
