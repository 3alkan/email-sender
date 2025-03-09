import smtplib
import time
import os
from lib.logger import logger
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from lib.constants import *
from lib.helpers import *

if CREDENTIAL_ERROR:
    logger.error("Error: Email credentials not set. Use environment variables.")
    exit(1)

PROJECT_FOLDER="project1"
project=read_project(PROJECT_FOLDER)
project=parse_project(project)
if not project:
    exit(1)
    
# Connect to SMTP server
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
except Exception as e:
    logger.error(f"SMTP Connection Error: {e}")
    exit(1)

# Send personalized emails
for recipient in project["recipients"]:
    personalized_body = project["email-body"].replace("{generic_name}", recipient["name"])
    full_body = f"{personalized_body}<br><br>{project['signature']}"

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient["email"]
    msg["Subject"] = project["subject"]
    #msg["CC"]=CC_EMAIL
    msg.attach(MIMEText(full_body, "html"))

    try:
        server.sendmail(SENDER_EMAIL, recipient["email"], msg.as_string())
        logger.info(f"Email sent to {recipient['email']}")
        time.sleep(2)  # Prevent spam detection
    except Exception as e:
        logger.error(f"Failed to send email to {recipient['email']}: {e}")

# Close connection
server.quit()
