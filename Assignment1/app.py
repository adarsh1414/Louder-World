import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup

app = Flask(__name__)

# Set up email configurations
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Enter your email
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Enter your email password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

# Global list to store events (should be updated periodically)
events = []

# Function to scrape events from a website
def scrape_events():
    global events
    url = "https://www.eventbrite.com/d/australia--sydney/events/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    events = []
    for event in soup.find_all("div", class_="search-event-card"):
        name = event.find("div", class_="eds-is-hidden-accessible").text.strip()
        date = event.find("div", class_="eds-text-color--primary").text.strip()
        link = event.find("a")['href']
        events.append({
            "name": name,
            "date": date,
            "link": link
        })

# Schedule the scraping function to run every 24 hours
def schedule_scraping():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_events, 'interval', hours=24)
    scheduler.start()

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/get_tickets', methods=['POST'])
def get_tickets():
    user_email = request.form['email']
    event_link = request.form['event_link']

    # Send confirmation email (optional)
    msg = Message('Event Ticket Information', recipients=[user_email])
    msg.body = f"Thank you for your interest! You can get your tickets here: {event_link}"
    mail.send(msg)

    # Redirect to the event link
    return redirect(event_link)

if __name__ == '__main__':
    # Run the scraper initially and start scheduling
    scrape_events()
    schedule_scraping()
    app.run(debug=True)
