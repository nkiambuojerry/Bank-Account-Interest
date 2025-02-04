# Bank Account Interest Calculation Program
# Open Source Operating Systems - ITMD 413/513
# Lab 3 - Loops and Repetition

# Step 1: PIN Authentication
correct_pin = "1234"  # Set a 4-digit PIN
success = False  # Track authentication status

# Allow user up to 3 attempts
for attempt in range(3):
    user_pin = input("Enter your 4-digit PIN: ")
    
    if user_pin == correct_pin:
        print("Access granted!\n")
        success = True
        break
    else:
        print(f"Invalid PIN. {2 - attempt} attempts remaining.\n")

# If authentication fails after 3 attempts, exit the program
if not success:
    print("Too many incorrect attempts. Access denied.")
    exit()

# Step 2: Get Bank Account Information
bank_balance = float(input("Enter initial bank balance: "))
annual_interest_rate = float(input("Enter annual interest rate (as decimal, e.g., 0.04 for 4%): "))

# Display table header
print("\nMonth #\tInterest Amt\tBalance")
print("-" * 30)

# Initialize total interest earned
total_interest = 0.0

# Step 3: Calculate Interest for 12 Months
for month in range(1, 13):
    interest = (annual_interest_rate / 12) * bank_balance  # Monthly interest calculation
    bank_balance += interest  # Update balance
    total_interest += interest  # Track total interest

    # Print monthly details in column format
    print(f"{month}\t${interest:.2f}\t   ${bank_balance:.2f}")

# Step 4: Display Summary
print("\nSummary:")
print(f"Total Interest Earned: ${total_interest:.2f}")
print(f"Final Balance After 12 Months: ${bank_balance:.2f}")
