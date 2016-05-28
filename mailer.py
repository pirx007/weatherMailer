emails = []
email_file = open('emails.txt', 'r')

for line in email_file:
    emails.append(line)

print(emails)

