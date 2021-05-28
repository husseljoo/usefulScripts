import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



SMTP_SERVER = "smtp.mail.yahoo.com" #you may vhange the domain
SMTP_PORT = 587



SMTP_USERNAME =os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD=os.environ.get("SMTP_PASSWORD")
EMAIL_FROM = os.environ.get("SMTP_USERNAME")
EMAIL_TO = "username@kindle.com" #enter destination mail here

debuglevel = True

def helper(file):
    base=os.path.basename(file)
    name=os.path.splitext(base)[0]
    return name

def send_email(pdfname):
    body=""
    co_msg = "test email"

    msg = MIMEMultipart(co_msg)
    msg['Subject'] =helper(pdfname)
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    msg.attach(MIMEText(body, 'plain'))

    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    # enconding the binary into base64
    encoders.encode_base64(payload)
    # add header with pdf name
    payload.add_header('Content-Disposition', "attachment; filename= "+pdfname)
    msg.attach(payload)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.set_debuglevel(debuglevel)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    server.quit()

if __name__=='__main__':

    if(len(sys.argv)==2):
        pdfname=sys.argv[1]
        print("Sending "+helper(pdfname)+"...")
        print()
        print()
        print()
        send_email(pdfname)
        print(SMTP_USERNAME)
        print()
        print()
        print()
        print("Sent "+helper(pdfname))
    else:
        print("Provide more exactly one argument")



