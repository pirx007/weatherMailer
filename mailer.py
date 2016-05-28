emails = []
email_file = open('emails.txt', 'r')

for line in email_file:
    line = line.strip()
    emails.append(line)

print(emails)

