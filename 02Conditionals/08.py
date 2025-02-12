# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password : ")

if len(password) < 6:
    print("Password is weak")

elif len(password) <= 10:
    print("Password is medium")

else:
    print("Password is strong")