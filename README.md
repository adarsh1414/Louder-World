# Event Scraping and Notification System

## Overview
This project involves scraping events from Sydney, Australia, and displaying them on a web page. Users can click a "GET TICKETS" button to provide their email and get redirected to the event page. The event data is automatically updated every 24 hours.

## Requirements
- Python 3.x
- Flask or Django (for backend)
- BeautifulSoup, Selenium (for scraping)
- smtplib/Flask-Mail (for email handling)
- APScheduler (for scheduling)

## Setup Instructions
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure your email server (for sending emails).
4. Run the Flask/Django app with `python app.py`.
5. Schedule scraping to run every 24 hours using APScheduler.

## Challenges Faced
- Dynamic content scraping using Selenium.
- Ensuring smooth user experience for email collection and redirection.

## Future Improvements
- Integrating AI for smarter event recommendations.
- Scaling the project to handle more cities and events.
