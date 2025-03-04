import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from fetch_content import get_random_line, get_random_summary  

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), "../config/.env")
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

if __name__ == "__main__":
    # Get random quote and book summary
    quote = get_random_line("data/quotes.txt")
    summary = get_random_summary("data/summaries.txt")

    # Format email body
    email_body = f"📖 *Daily Knowledge Boost*\n\n✏️ *Quote of the Day:*\n{quote}\n\n📚 *Book Summary:*\n{summary}"

    # Send the email
    send_email("Daily Knowledge Boost", email_body, "ggallitz03@icloud.com")
