PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt","r") as names:
    name_list = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as template_start:
    template_contents = template_start.read()
    for name in name_list:
        clean_name = name.strip()
        new_letter = template_contents.replace(PLACEHOLDER, clean_name)
        with open(f"Output/ReadyToSend/{clean_name}'s Letter", "w") as final_letter:
            final_letter.write(f"{new_letter}")
