# -------------------------------
# REAL LIFE SCENARIO:
# A person is trying to sign up for a gym.
# The gym only allows people who are 18 or older.
# -------------------------------


# ✅ PURE FUNCTION
# This function only checks a rule.
# It does NOT print, save, or change anything.
# Same input → same output every time.
def is_age_valid(age):
    return age >= 18


# 📝 SIDE EFFECT FUNCTION (Logging)
# This function talks to the outside world.
# It prints information for humans to see.
# That makes it a "side effect".
def log_message(message):
    print(message)


# -------------------------------
# MAIN PROGRAM (this is the "app")
# -------------------------------

# A user enters their age
user_age = input("Please enter your age: ")
if user_age.isdigit():
    user_age = int(user_age) # Convert to integer
else:
    log_message("Invalid input. Please enter a numeric age.")
    exit()

# We ask the pure validation function:
# "Is this age allowed?"
if is_age_valid(user_age):

    # If yes, we log success
    log_message("Welcome to the gym! Your membership is active.")

else:
    # If no, we log rejection
    log_message("Sorry, you must be 18 or older to join the gym.")
