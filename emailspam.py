import smtplib as s

ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login("testemmail2024@tempmail.com","G7#x9!pVq2&zL8rT")
subject="Testing Scam"
body="SELECT employee_id FROM EmployeesWHERE salary < 30000 AND manager_id IS NOT NULL AND manager_id IN (SELECT employee_id FROM Employees);"

while True:
    massage="Subject:{}\n\n{}".format(subject,body)
    listadd=['sendermail@gmail.com']
    ob.sendmail('testemmail2024@tempmail.com',listadd,massage)
    print("sended")
    ans=input("Do you want to send again ? (yes/no): ")
    if ans.lower()!='yes':
        break