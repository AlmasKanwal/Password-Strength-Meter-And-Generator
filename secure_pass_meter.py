import re 
import streamlit as st
import secrets
import string

# Password Strength Checker

# Common Passwords
common_passwords = [
    "123456", "123456789", "12345", "1234", "000000",
    "111111", "123123", "654321", "987654", "password",
    "password123", "admin", "welcome", "iloveyou",
    "qwerty", "letmein", "monkey", "sunshine", "football",
    "abc123", "passw0rd", "superman", "batman", "charlie",
    "dragon", "pokemon", "michael", "shadow", "hello",
    "1990", "2000", "2010", "2025", "qwerty2025",
    "hello2023", "password2022"
]

# Password Strength Meter Checker Function
def password_strength_meter(password):
    score = 0
    feedback = []

    # Common Password Check
    if password.lower() in common_passwords:
        return "🔴 Weak Password", ["This password is too common. Please choose another."]

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Upper & Lower Case Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one digit (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Final Result
    if score == 4:
        return "🟢 Strong Password", []
    elif score == 3:
        return "🟡 Moderate Password", feedback
    else:
        return "🔴 Weak Password", feedback

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Check the strength of your password</h3>", unsafe_allow_html=True)

with st.form("check_strength_form"): 
    password = st.text_input("Enter your Password", type="password")
    check_button = st.form_submit_button("Check Password Strength")

if check_button and password:
    strength, suggestions = password_strength_meter(password)
    st.subheader(strength)

    if suggestions:
        st.warning("🔍 Suggestions to improve your password")
        for s in suggestions:
            st.write(f"🔹 {s}")
    else:
        st.success("✅ Your password is strong and secure!")

    st.markdown("<h4>🔋 Progress Bar For Password Strength</h4>", unsafe_allow_html=True)
    if strength.startswith("🟢"):
        st.progress(100)
    elif strength.startswith("🟡"):
        st.progress(60)
    else:
        st.progress(30)


# Random Strong Password Generator 

# function to generate a strong password 
def generate_random_password(length):
    random_password = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(random_password) for p in range(length))

st.markdown("<h1 style='text-align: center;'>🔑 Generate a Strong Password</h1>", unsafe_allow_html=True)
length = st.slider("Select Password Length", max_value=30, min_value=8, value=12)

if st.button("Generate Strong Password"):
    strong_password = generate_random_password(length)
    # st.write(f"Generated Password: {strong_password}")
    st.text_input("### Generated Password", value=strong_password)
    st.success("✅Use this password for better security.")

st.write("********************************")
st.markdown("<h5 style='text-align: center;'>Made By 💝 Almas Kanwal</h5>", unsafe_allow_html=True)

