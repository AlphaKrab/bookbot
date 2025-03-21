def get_number_of_words(text):
    # Printing what book_text retrieved
    word_count = len(text.split())
    return word_count

def character_count(text):
    # converts each upper to lower case
    converted_text = text.lower()
    # Open dictionary to be filled
    character_totals = {}
    for char in converted_text:
        character_totals[char] = character_totals.get(char, 0) + 1
    return character_totals

def organized_characters(character_totals):
    # Create a list to hold the dictionary.
    character_list = []

    # For each character and count create a dictionary.
    for char, count in character_totals.items():
        character_list.append({"char": char, "count": count})
    
    # This will choose the sorting format for the output.
    character_list.sort(reverse=True, key=lambda x: x["count"])
    return character_list


