#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text_list = [letter + "\n\n" if letter in ".?:"
                     else letter for letter in text]
    new_text = "".join(character for character in new_text_list).splitlines()
    for i in range(len(new_text)):
        if i == len(new_text) - 1:
            print(str(new_text[i]).strip(), end='')
        else:
            print(str(new_text[i]).strip())
