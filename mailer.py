import requests
import smtplib

def get_emails():
    emails = {}

    try:
        email_file = open('emails2.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name
    except FileNotFoundError as err:
        print(err)
    return emails


def get_schedule():
    schedule = ""
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
    return schedule


def get_weather_forecast():
    # city id for Krakow
    # url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=3094802&APPID=5381c26391241dd6d843dcf600d3589c'
    url = 'http://api.openweathermap.org/data/2.5/weather?id=3094802&units=metric&APPID=5381c26391241dd6d843dcf600d3589c'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    #print(weather_json)

    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = 'Forecast for today, '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min))

    return forecast


def send_emails(emails, schedule, forecast):
    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    #Login
    password = input("Pass?")
    email = 'zdjjeden@gmail.com'
    server.login('zdjjeden@gmail.com', password)
    server.sendmail(email, email, forecast)
    server.quit()

def main():
    emails = get_emails()
    schedule = get_schedule()
    forecast = get_weather_forecast()
    #print(forecast)
    send_emails(emails, schedule, str(forecast))

main()