password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True

length = len(password)

if length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("✅ Strong Password")
elif length >= 6 and ((has_upper and has_digit) or (has_lower and has_special)):
    print("🟡 Medium Password")
else:
    print("🔴 Weak Password")
