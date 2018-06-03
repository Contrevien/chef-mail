import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
def sendMe():
    fromaddr = "contrevien@outlook.com"
    toaddr = "akkimysite@gmail.com"
     
    msg = MIMEMultipart()
     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Another Step to Success!"
     
    body = "Today's problem is attached:"
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = "today.txt"
    attachment = open("./today.txt", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp-mail.outlook.com:587')
    server.starttls()
    server.login(fromaddr, "@nzCallahan1")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    
    server.quit()
