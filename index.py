import smtplib as s
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

object = s.SMTP('smtp.gmail.com',587)
object.ehlo()
object.starttls()
object.login('email@gmail.com', 'xxxx xxxx xxxx xxxx ') 

subject = "Only for Test Python"
body = "Below are the required files"

list = ['receiver@gmail.com','receiver2@gmail.com']

msg = MIMEMultipart()
msg["From"] = 'email@gmail.com'
msg["To"] = ','.join(list)
msg["Subject"] = subject

msg.attach(MIMEText(body, 'plain'))


filepath1 = r'\Email\cv.jpg' 
filepath2 = r'\Email\cv_Bibhuti_Bhandari.pdf'

attachments = [filepath1,filepath2]

for filepath in attachments:
    filename = filepath.split('\\')[-1]
    with open(filepath,'rb') as attachments:
        part = MIMEBase('application','ocet-stream')
        part.set_payload(attachments.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',f'attachments; filename={filename}')
        msg.attach(part)
    
                        
object.sendmail('email@gmail.com', list, msg.as_string())
print("Mail sent")
object.quit()
