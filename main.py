notes = []

while True:
    print("1. Add note")
    print("2. Show notes")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        note = input("Enter note: ")
        notes.append(note)

    elif choice == "2":
        for note in notes:
            print(note)

    elif choice == "3":
        break

    else:
        print("Invalid option")