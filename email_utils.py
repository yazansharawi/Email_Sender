import smtplib
import ssl
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Template

def send_email(name, email, attachment_path, background, attachment_type,template_file):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            message = MIMEMultipart()
            message['From'] = config.EMAIL_ADDRESS
            message['To'] = email
            message['Subject'] = "Professional Introduction and Attachment"
            
            with open(f'templates/{template_file}', 'r') as template_file:
                template = Template(template_file.read())
                body = template.render(name=name, background=background, attachment_type=attachment_type)
            
            message.attach(MIMEText(body, 'html'))
            with open(attachment_path, 'rb') as attachment_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment_file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
                message.attach(part)
            server.sendmail(config.EMAIL_ADDRESS, email, message.as_string())
    except Exception as e:
        raise Exception(str(e))