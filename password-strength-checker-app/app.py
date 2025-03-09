import random
import streamlit as st
import re
import string  


# Step 1: Password Generator
def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*()+=_-?/<>()~"
    return "".join(random.choice(characters) for _ in range(length))


# Step 2: Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Common password check
    common_passwords = ["12345678", "abc123", "khan123", "pak123", "password"]
    if password in common_passwords:
        return ["❌ This password is too common. Choose a more unique one."], "Weak"
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚜ Password should be at least 8 characters long.")

    # Uppercase & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚜ Include both uppercase and lowercase letters.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚜ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*\(\)+=_\-?/<>~]", password): 
        score += 1
    else:
        feedback.append("⚜ Include at least one special character (!@#$%^&*()+=_-?/<>()~).")

    # Determine Strength
    if score == 4:
        return ["✔ Strong Password!"], "Strong"
    elif score == 3:
        return ["⬜ Moderate Password - Consider adding more security features."], "Moderate"
    else:
        return feedback, "Weak"


# Streamlit UI
st.title("🔐 Password Strength Manager")

# Password Strength Checker UI
check_password = st.text_input("Enter your password", type="password")
if st.button("Check Strength"):
    if check_password:
        feedback, strength = check_password_strength(check_password)
        
     
        if strength == "Strong":
            st.success(feedback[0])
            st.balloons()
        elif strength == "Moderate":
            st.warning(feedback[0])  
        else:
            st.error("❗ Weak Password! Consider the following tips:")
            for message in feedback:
                st.write(f"🔹 {message}")  

    else:
        st.warning("Please enter a password")


# Password Generator UI
password_length = st.number_input("Enter the length of password", min_value=8, max_value=20, value=10)
if st.button("Generate Password"):
    password = generate_password(password_length)
    st.success(f"Generated Password: `{password}`")  

    # ✅ Copy Button
    st.code(password, language="") 
