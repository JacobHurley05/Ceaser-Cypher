userAnswer = input("ENCRYPT, DECRYPT, or BRUTE? ").upper()

userMessage = input("Enter your message: ")

if userAnswer == "ENCRYPT" or userAnswer == "DECRYPT":
    shift = int(input("Enter shift value: "))
    if userAnswer == "DECRYPT":
        shift = -shift

    result = ""
    for c in userMessage:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c

    print("Result:", result)

elif userAnswer == "BRUTE":
    for shift in range(1, 26):
        result = ""
        for c in userMessage:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c) - base - shift) % 26 + base)
            else:
                result += c

        print(f"Shift {shift}: {result}")