import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv("config/.env")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))


def send_email(subject, body, recipient):
    """Send an email using SMTP."""
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")


# Example usage
if __name__ == "__main__":
    send_email("Test Email", "This is a test message!", "ggallitz03@icloud.com")
