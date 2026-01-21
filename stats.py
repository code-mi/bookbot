def count_words(text):
    words = text.split()
    return len(words)


def count_char(text):
    tmp_dict = {}
    for i in text.lower():
        if i not in tmp_dict:
            tmp_dict[i] = 1
        else:
            tmp_dict[i] += 1
    if "\ufeff" in tmp_dict:
        del tmp_dict["\ufeff"]
    return tmp_dict


def sort_me(dictionary):
    # for x, y in items.items():
    #    print(x, y)
    result = list(dictionary)
    # result.sort(reverse=True)
    # for i in result:
    #   print(i)
    return result
