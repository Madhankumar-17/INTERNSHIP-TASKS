correct_pin = "1234"
attempts = 0

print("----- ATM PIN Checker -----")

while attempts < 3:
    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Incorrect PIN")

if attempts == 3:
    print("Card Blocked")