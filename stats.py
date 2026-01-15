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
    del tmp_dict["\ufeff"]
    return tmp_dict
