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
        for index, note in enumerate(notes, start=1):
            print(index, note)

    elif choice == "3":
        break
    
    elif choice == "4":
        index = int(input("Enter note number: "))

        if 1 <= index <= len(notes):
            notes.pop(index - 1)
            print("Note deleted")
        else:
            print("Invalid note number")

    else:
        print("Invalid option")
        