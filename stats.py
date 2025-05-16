def get_word_count(book):
    
    count = 0
    words = book.split()
    
    for word in words:
        count += 1

    return count

def get_count_per_char(book):
    
    counts = {}

    for char in book.lower():
        if char not in counts:
            counts[char] = 0

        counts[char] += 1

    return counts

def sort_chars(chars_dict):
    chars_list = []

    for char in chars_dict:
        chars_list.append({"char": char, "count": chars_dict[char]})
    
    chars_list.sort(key=sort_on, reverse=True)
    
    return chars_list

def sort_on(dict):
    return dict["count"]

