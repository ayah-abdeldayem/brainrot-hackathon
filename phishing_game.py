import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
# Sample emails with sender address, subject, and body
emails = [
    {
        "sender": "support@amazon.com",
        "subject": "Your Amazon Order #123-4567890-1234567 Has Shipped",
        "body": "Hello Ciara,\n\nYour order has been shipped and is on its way! You can track your package here: [link].\n\nThank you for shopping with us,\nThe Amazon Team",
        "is_phish": False,
        "image": "credit_card_phishing.png",  # Placeholder for safe email image
        "explanation": "This email is legitimate because the sender is from Amazon's official domain, the content is relevant, and the link directs to Amazon's website."
    },
    {
        "image": "paypal.png",
        "is_phish" : False

    },
    {
        "sender": "billing@spotify.com",
        "subject": "Your Spotify Premium Subscription Renewal Confirmation",
        "body": "Hi Audrey,\n\nYour Spotify Premium subscription has been successfully renewed. The payment of $9.99 has been charged to your account.\n\nNeed help? Contact us here: [link].\n\nThanks,\nThe Spotify Team",
        "is_phish": False,
        "image": "safe_email_2.png",  # Placeholder for safe email image
        "explanation": "This email is legitimate because it comes from Spotify's official domain, does not ask for sensitive information, and communicates relevant details."
    },
    {
        "sender": "info@bestbuy.com",
        "subject": "Your Best Buy Account has been locked",
        "body": "We have detected unusual activity on your Best Buy account. To unlock your account, click here and confirm your personal details.",
        "is_phish": True,
        "image": "phish_email_7.png",  # Placeholder for phishing email image
        "explanation": "Phishing attempt. Best Buy would not ask for sensitive personal details in this manner. The email also uses a non-secure link, which is a common tactic used in phishing scams."
    },
    {
        "sender": "alerts@chase.com",
        "subject": "Unusual Activity Detected on Your Credit Card",
        "body": "Dear Audrey Chen,\n\nWe detected unusual activity on your Chase credit card ending in 1234. Please log into your account via the Chase website or app to review the transaction.\n\nFor security, we have not included a link in this email. Please visit chase.com directly to access your account.\n\nThank you for your attention,\nChase Customer Service",
        "is_phish": False,
        "image": "safe_email_3.png",  # Placeholder for safe email image
        "explanation": "This email is legitimate because Chase avoids including links, uses their official domain, and encourages secure practices."
    },
    {
        "sender": "security@facebook-alert.com",
        "subject": "Your Facebook account has been compromised",
        "body": "Your Facebook account is at risk! Please log in now to verify your account details and change your password.",
        "is_phish": True,
        "image": "phish_email_9.png",  # Placeholder for phishing email image
        "explanation": "Phishing attempt. The sender's domain is suspicious, and Facebook would not ask for such details via email."
    },

    {
        "sender": "support@paypal.com",
        "subject": "You’ve received money!",
        "body": "Hi Ciara,\n\nYou have received $50.00 from John Smith. Log in to your PayPal account to review the transaction.\n\nThanks for using PayPal,\nThe PayPal Team",
        "is_phish": False,
        "image": "safe_email_4.png",  # Placeholder for safe email image
        "explanation": "This email is legitimate because it comes from PayPal's official domain, does not include any suspicious links, and provides accurate transaction details."
    },
    {
        "sender": "info@officialbank.com",
        "subject": "Your Bank Account Has Been Suspended",
        "body": "Your bank account has been suspended due to suspicious activity. Click this link to verify your identity and restore access.",
        "is_phish": True,
        "image": "phish_email_8.png",  # Placeholder for phishing email image
        "explanation": "The email uses urgent language and requests sensitive information via a link. Legitimate banks will never ask you to verify your account through a link sent in an email."
    },
    {
        "sender": "team@linkedin.com",
        "subject": "You Have a New Connection Request",
        "body": "Hi Morgan,\n\nYou have a new connection request from John Smith. View their profile and decide if you'd like to connect.\n\n[Accept] [Decline]\n\nRegards,\nThe LinkedIn Team",
        "is_phish": False,
        "image": "safe_email_5.png",  # Placeholder for safe email image
        "explanation": "This email is legitimate because it comes from LinkedIn's official domain, uses clear and relevant messaging, and does not request sensitive information."
    },
    {
    "sender": "admin@university-portal.com",
    "subject": "Password Expiration Notification",
    "body": "Dear Student,\n\nYour university account password is set to expire in 24 hours. Please update your password immediately to avoid being locked out. Click here to update: [link].\n\nSincerely,\nUniversity IT Support",
    "is_phish": True,
    "image": "phish_email_10.png",  # Placeholder for phishing email image
    "explanation": "Phishing attempt. The domain is suspicious ('university-portal.com' instead of the university's actual domain). Universities typically use their official portals for account updates."
},
{
    "sender": "alerts@apple-security.com",
    "subject": "Unusual Login Attempt on Your Apple ID",
    "body": "Hello,\n\nWe noticed an unusual login attempt on your Apple ID from an unknown device. If this was not you, please secure your account immediately by clicking the link below:\n\n[Secure My Account]\n\nThanks,\nApple Security Team",
    "is_phish": True,
    "image": "phish_email_11.png",  # Placeholder for phishing email image
    "explanation": "Phishing attempt. The domain ('apple-security.com') is not Apple's official domain. Apple would ask you to log in via their official site or app without including suspicious links."
}
]
# Initialize score and email pool
score = 0
shown_emails = []

# Update the score label
def update_score():
    score_label.setText(f"Score: {score}")

# Function to select a random email and display it
def show_email():
    global current_email

    if len(shown_emails) == len(emails):
        show_final_score()
        return

    remaining_emails = [email for email in emails if email not in shown_emails]
    current_email = random.choice(remaining_emails)
    shown_emails.append(current_email)

    email_details_label.setText(f"From: {current_email['sender']}\nSubject: {current_email['subject']}\n\n{current_email['body']}")

    pixmap = QPixmap(current_email["image"])
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignCenter)

    explanation_label.setText("")

# Function to handle the "Phish" button click
def check_phish():
    global score
    if current_email["is_phish"]:
        score += 1
        explanation = f"Correct! This is a phishing email.\n\nExplanation: {current_email['explanation']}"
    else:
        explanation = f"Wrong! This is a safe email.\n\nExplanation: {current_email['explanation']}"
    show_explanation(explanation)
    update_score()
    QTimer.singleShot(5000, show_email)

# Function to handle the "Safe" button click
def check_safe():
    global score
    if not current_email["is_phish"]:
        score += 1
        explanation = f"Correct! This is a safe email.\n\nExplanation: {current_email['explanation']}"
    else:
        explanation = f"Wrong! This is a phishing email.\n\nExplanation: {current_email['explanation']}"
    show_explanation(explanation)
    update_score()
    QTimer.singleShot(5000, show_email)

# Function to show explanation
def show_explanation(explanation):
    explanation_label.setText(explanation)
    explanation_label.setStyleSheet("font-size: 16px; color: #333; padding: 10px; background-color: #d0f0f8; border-radius: 8px;")

# Function to show the final score
def show_final_score():
    final_score_message = f"Your final score is: {score} / {len(emails)}"
    tips = """
    Cybersecurity Tips:
    - Check sender email addresses carefully.
    - Avoid clicking suspicious links.
    - Never provide sensitive information via email.
    - Verify the authenticity of emails from trusted sources.
    """

    msg_box = QMessageBox(window)
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("Final Score")
    msg_box.setText(final_score_message + "\n\n" + tips)
    msg_box.setStandardButtons(QMessageBox.Ok)

    msg_box.setStyleSheet("""
        background-color: #f8eef7; 
        color: #555; 
        font-size: 16px; 
        padding: 10px; 
        border-radius: 8px;
    """)

    msg_box.exec_()
    QApplication.quit()

# Set up the PyQt5 application
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("Phishing Email Detector Game")
window.setGeometry(100, 100, 600, 500)
window.setStyleSheet("background-color: #fff4f9;")

# Create a title label
title_label = QLabel("Phishing Email Detector Game")
title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #705d82;")
title_label.setAlignment(Qt.AlignCenter)

# Create a label to show the email details
email_details_label = QLabel("")
email_details_label.setStyleSheet("font-size: 14px; color: #444; padding: 15px; background-color: #f3f0ff; border-radius: 8px;")
email_details_label.setAlignment(Qt.AlignCenter)
email_details_label.setWordWrap(True)

# Create a score label
score_label = QLabel("Score: 0")
score_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #707ea3;")

# Create the explanation label
explanation_label = QLabel("")
explanation_label.setStyleSheet("font-size: 14px; color: #444; padding: 15px; background-color: #f3f0ff; border-radius: 8px;")
explanation_label.setAlignment(Qt.AlignCenter)
explanation_label.setWordWrap(True)

# Create the image label
image_label = QLabel()
image_label.setAlignment(Qt.AlignCenter)

# Create buttons for "Phish" and "Safe"
phish_button = QPushButton("Phish")
phish_button.setStyleSheet("background-color: #f28a8a; color: white; font-size: 16px; padding: 10px; border-radius: 8px;")
phish_button.clicked.connect(check_phish)

safe_button = QPushButton("Safe")
safe_button.setStyleSheet("background-color: #87ceeb; color: white; font-size: 16px; padding: 10px; border-radius: 8px;")
safe_button.clicked.connect(check_safe)

# Create a layout
button_layout = QHBoxLayout()
button_layout.addWidget(phish_button)
button_layout.addWidget(safe_button)

main_layout = QVBoxLayout()
main_layout.addWidget(title_label)
main_layout.addWidget(email_details_label)
main_layout.addWidget(image_label)
main_layout.addWidget(score_label)
main_layout.addWidget(explanation_label)
main_layout.addLayout(button_layout)

# Set layout for the window
window.setLayout(main_layout)

# Start the game
show_email()

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
