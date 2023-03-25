def is_anagram(first_string, second_string):
    first_string_array = sort_string(list(first_string.lower()))
    first_string = "".join(first_string_array)
    second_string_array = sort_string(list(second_string.lower()))
    second_string = "".join(second_string_array)

    if not first_string or not second_string:
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)


def sort_string(letters):
    if len(letters) <= 1:
        return letters
    pivo = letters[0]
    right = [letter for letter in letters[1:] if letter < pivo]
    left = [letter for letter in letters[1:] if letter >= pivo]
    return sort_string(right) + [pivo] + sort_string(left)
