import re

def analyze_email(email_text):
    risk_score = 0

    suspicious_keywords = [
        "urgent",
        "verify your account",
        "click here",
        "password",
        "bank details",
        "login now",
        "limited time",
        "winner",
        "claim prize"
    ]

    found_patterns = []

    # Check suspicious keywords
    for keyword in suspicious_keywords:
        if keyword.lower() in email_text.lower():
            risk_score += 1
            found_patterns.append(keyword)

    # Check for links
    links = re.findall(r'https?://\S+|www\.\S+', email_text)
    if links:
        risk_score += 1
        found_patterns.append("Suspicious Link")

    # Display result
    print("\n--- Analysis Result ---")

    if risk_score >= 3:
        print("⚠️ High Risk Email Detected")
    elif risk_score >= 1:
        print("⚠️ Suspicious Email")
    else:
        print("✅ Safe Email")

    if found_patterns:
        print("Detected Patterns:")
        for item in found_patterns:
            print("-", item)

# Main Program
email = input("Enter Email Content:\n")
analyze_email(email)