import smtplib as s

ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login("testemmail2024@tempmail.com","G7#x9!pVq2&zL8rT")
subject="Testing Scam"
body="SELECT employee_id FROM EmployeesWHERE salary < 30000 AND manager_id IS NOT NULL AND manager_id IN (SELECT employee_id FROM Employees);"

n = int(input("Enter no of time to bombing : "))
for i in range(n):
    message = "Subject:{}\n\n{}".format(subject, body)
    recipients = ['recipient@example.com']
    ob.sendmail('testemmail2024@tempmail.com', recipients, message)
    print("Message sent")