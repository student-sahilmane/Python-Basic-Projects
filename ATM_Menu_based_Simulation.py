balance = 1000

while True:
    print("\n=== ATM Menu ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"💰 Your balance is ₹{balance}")

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
        else:
            print("❌ Invalid deposit amount.")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
        else:
            print("❌ Insufficient balance or invalid amount.")

    elif choice == '4':
        print("👋 Thank you for using ATM. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select between 1–4.")




