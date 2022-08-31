class MergeLetter:
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter = (letter.read())

    with open("./Input/Names/invited_names.txt") as names:
        guests = names.readlines()

    guests_letters = []
    for guest in guests:
        guest = guest.replace('\n', '')
        guest_letter = letter.replace("[name]", guest)
        file_name = f"./Output/ReadyToSend/letter_for_{guest}.txt"
        with open(file_name, mode="w") as ready:
            ready.write(guest_letter)
