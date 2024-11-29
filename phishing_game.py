import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
.fromkeys(key, value)
# Sample emails with sender address, subject, and body
emails = [
    {
        "sender": "service@apple-support.com",
        "subject": "Important: Your Apple ID has been locked",
        "body": "Dear Customer, we noticed suspicious activity in your account. Your Apple ID has been temporarily locked. To unlock it, click here.",
        "is_phish": True,
        "image": "phish_email_3.png",  # Placeholder for phishing email image
        "explanation": "This email is phishing because it uses a generic greeting instead of your name. Legitimate companies like Apple would never ask for your credentials via email. The sender's address is also fake."
    },
    {
        "sender": "contact@secure-gmail.com",
        "subject": "Your Google Account has been compromised",
        "body": "Dear User, we detected unauthorized sign-in activity in your Google account. Click this link to secure your account.",
        "is_phish": True,
        "image": "phish_email_4.png",  # Placeholder for phishing email image
        "explanation": "The sender's email address is not a legitimate Google address. Google also never sends urgent emails like this asking for your personal credentials. Always verify by visiting the official Google website."
    },
    {
        "sender": "admin@taxrefund.gov",
        "subject": "Your Tax Refund Is Ready for Deposit",
        "body": "Congratulations! Your tax refund is ready for deposit. Please provide your bank details to receive your refund.",
        "is_phish": True,
        "image": "phish_email_5.png",  # Placeholder for phishing email image
        "explanation": "This is a classic phishing attempt. The IRS will never ask for sensitive information via email. The grammar is also suspicious, with incomplete phrases and vague language."
    },
    {
        "sender": "no-reply@netflix.com",
        "subject": "Account Suspension Notice",
        "body": "Dear Customer, we have temporarily suspended your Netflix account due to suspicious activity. Please confirm your payment details here to restore access.",
        "is_phish": True,
        "image": "phish_email_6.png",  # Placeholder for phishing email image
        "explanation": "This email is phishing because Netflix will never ask for payment details via email. The email address is also not the official Netflix domain, which is another red flag."
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
        "sender": "info@officialbank.com",
        "subject": "Your Bank Account Has Been Suspended",
        "body": "Your bank account has been suspended due to suspicious activity. Click this link to verify your identity and restore access.",
        "is_phish": True,
        "image": "phish_email_8.png",  # Placeholder for phishing email image
        "explanation": "The email uses urgent language and requests sensitive information via a link. Legitimate banks will never ask you to verify your account through a link sent in an email."
    },
    {
        "sender": "amazon-customer-support@service.com",
        "subject": "Your Amazon Account has been temporarily blocked",
        "body": "Your Amazon account has been temporarily blocked due to suspicious activity. Click here to verify your information and restore access.",
        "is_phish": True,
        "image": "phish_email_9.png",  # Placeholder for phishing email image
        "explanation": "This email is phishing because the sender address is not from Amazon's official domain. Also, Amazon will never ask you to click a link to verify your account via email."
    },
    {
        "sender": "news@bestdeal.com",
        "subject": "Limited Time Offer: Get a Free iPhone!",
        "body": "Get the latest iPhone for free today! Click here to claim your reward.",
        "is_phish": True,
        "image": "phish_email_10.png",  # Placeholder for phishing email image
        "explanation": "This is clearly phishing. No legitimate company would offer an iPhone for free with such an unrealistic offer. The email also contains no contact information or official branding."
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

    # If all emails have been shown, reset the list
    if len(shown_emails) == len(emails):
        show_final_score()
        return

    # Select a random email from the list of emails that have not been shown
    remaining_emails = [email for email in emails if email not in shown_emails]
    current_email = random.choice(remaining_emails)
    shown_emails.append(current_email)  # Mark this email as shown
    
    # Update the email label with the selected email details
    email_details_label.setText(f"From: {current_email['sender']}\nSubject: {current_email['subject']}\n\n{current_email['body']}")
    
    # Load and display the image associated with the email
    pixmap = QPixmap(current_email["image"])
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignCenter)
    
    # Hide explanation until after answer is given
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
    QTimer.singleShot(5000, show_email)  # Show next email after 5 seconds

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
    QTimer.singleShot(5000, show_email)  # Show next email after 5 seconds

# Function to show explanation
def show_explanation(explanation):
    explanation_label.setText(explanation)
    explanation_label.setStyleSheet("font-size: 16px; color: black; padding: 10px; background-color: #f0f8ff; border-radius: 5px;")

# Function to show the final score and cybersecurity tips
# Function to show the final score and cybersecurity tips
# Function to show the final score and cybersecurity tips
def show_final_score():
    final_score_message = f"Your final score is: {score} / {len(emails)}"
    tips = """
    Cybersecurity Tips for Identifying Phishing Emails:
    - Always check the sender's email address carefully.
    - Look for spelling or grammatical errors in the email.
    - Avoid clicking on links or downloading attachments from unknown senders.
    - Be cautious of emails with urgent language or requests for personal information.
    - Never provide sensitive information (like passwords or credit card numbers) via email.
    - Verify requests through official channels or websites.
    - Check for a secure connection (look for HTTPS) when providing sensitive information online.
    - Don't trust unsolicited offers of free products or services.
    """

    # Create the message box
    msg_box = QMessageBox(window)
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("Final Score")
    msg_box.setText(final_score_message + "\n\n" + tips)
    msg_box.setStandardButtons(QMessageBox.Ok)

    # Set custom stylesheet for better readability
    msg_box.setStyleSheet("""
        background-color: #f0f8ff;
        color: #333333;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
    """)

    msg_box.exec_()  # Show the message box
    QApplication.quit()  # Quit the application after the message box is closed


# Set up the PyQt5 application
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("Phishing Email Detector Game")
window.setGeometry(100, 100, 600, 500)
window.setStyleSheet("background-color: #f4f7f6;")  # Set background color to a pastel color

# Create a title label
title_label = QLabel("Phishing Email Detector Game")
title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #5f6368;")
title_label.setAlignment(Qt.AlignCenter)

# Create a label to show the email details
email_details_label = QLabel("")
email_details_label.setStyleSheet("font-size: 14px; color: #333; padding: 20px; background-color: #ffffff; border-radius: 5px;")
email_details_label.setAlignment(Qt.AlignCenter)
email_details_label.setWordWrap(True)

# Create a score label
score_label = QLabel("Score: 0")
score_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #5f6368;")

# Create the explanation label
explanation_label = QLabel("")
explanation_label.setStyleSheet("font-size: 14px; color: #333; padding: 20px; background-color: #ffffff; border-radius: 5px;")
explanation_label.setAlignment(Qt.AlignCenter)
explanation_label.setWordWrap(True)

# Create the image label
image_label = QLabel()
image_label.setAlignment(Qt.AlignCenter)

# Create buttons for "Phish" and "Safe"
phish_button = QPushButton("Phish")
phish_button.setStyleSheet("background-color: #ff6f61; color: white; font-size: 16px; padding: 10px; border-radius: 5px;")
phish_button.clicked.connect(check_phish)

safe_button = QPushButton("Safe")
safe_button.setStyleSheet("background-color: #4caf50; color: white; font-size: 16px; padding: 10px; border-radius: 5px;")
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
