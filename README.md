# Introduction

This script is a Canvas Scraper that automates the process of downloading attachments and files from your Canvas course modules. It uses Selenium for web scraping and automates interactions with the Canvas web interface, including handling Duo Mobile two-factor authentication (specific to the configured school's Canvas setup).
Disclaimer

    School-Specific Duo Mobile Policy: The script's handling of Duo Mobile two-factor authentication is tailored to a specific school's Canvas setup. It may not work with other institutions' Duo Mobile configurations.
    Potential Out-of-Date Methods: The methods used in this script may become outdated due to changes in Canvas or Duo Mobile's policies and interfaces.

# Prerequisites

    Python 3.6 or higher
    Selenium package
    Chrome WebDriver
    Valid Canvas account credentials
    Access to Duo Mobile for two-factor authentication

# Setup

# Installation

    Python & Selenium Installation:
    Install Python 3.6 or higher, then use pip to install Selenium:

    bash

    pip install selenium

    WebDriver Setup:
    Download the Chrome WebDriver that matches your Chrome version from ChromeDriver - WebDriver for Chrome. Ensure it's in your PATH or specify its location in the script.

# Configuration

    Update the script with your Canvas credentials, course code, and Canvas URL:

    python

    CANVAS_USERNAME = "your_username"
    CANVAS_PASSWORD = "your_password"
    COURSE_CODE = "your_course_code"
    CANVAS_URL = "your_canvas_url"

# Running the Application

    Execute the script using Python. Ensure that you are in the correct directory where your script is located:

    open shell

    python canvas_scraper.py

    The script will navigate through the Canvas site, handle two-factor authentication via Duo Mobile, and download the necessary files from the specified course modules.

# Features

    Automatic login to Canvas with credentials.
    Handling of Duo Mobile two-factor authentication.
    Navigation to specific course modules.
    Downloading of attachments and files from modules.

# Limitations

    The script currently only supports Chrome WebDriver.
    The handling of Duo Mobile is specific to the configured school's setup and may require adjustments for other institutions.

# Troubleshooting

    If the script fails at the Duo Mobile step, ensure that your device is ready to approve the push notification promptly.
    Make sure the Chrome WebDriver version matches your browser's version.
    Check your internet connection and Canvas URL if the script cannot access the Canvas site.

# Future Enhancements

    Support for other web browsers and their respective WebDrivers.
    Configurable options for selecting specific modules or file types for download.
    Improved error handling and logging.
