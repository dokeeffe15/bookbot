def num_words(text):
    # This function takes a string of text and returns the number of words in it
    # It splits the text by whitespace and counts the number of elements in the resulting list
    return len(text.split())


def num_characters(text):
    dic = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            # Convert character to lowercase to count case-insensitively
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
    return dic


def sort_characters(dic):
    #Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries
    result = [{"char": char, "num": count} for char, count in dic.items()]
    # Sort the list of dictionaries by the 'num' key in descending order
    result.sort(key=lambda x: x["num"], reverse=True)
    return result

