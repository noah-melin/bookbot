def number_of_words(get_book_text):
    words = get_book_text.split()
    return len(words)

def get_character_count(get_book_text):
    characters = {}
    for char in get_book_text.lower():
        if char.isalpha(): 
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def characters(get_book_text):
    char_count = get_character_count(get_book_text)
    result = ""
    for char, count in char_count.items():
        result += f"{char}: {count}\n"
    return result

def sorted_characters(get_book_text):
    char_count = get_character_count(get_book_text)
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda x: x["num"], reverse=True)
    result = ""
    for item in char_list:
        result += f"{item['char']}: {item['num']}\n"
    return result