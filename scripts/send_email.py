import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load .env file
dotenv_path = "/Users/georg/Desktop/projects/remindme/config/.env"
load_dotenv(dotenv_path)

# Load environment variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))  # Defaults to 587 if missing

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
    send_email("Daily Reminder", "This is your knowledge boost for today!", "ggallitz03@icloud.com")
