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


