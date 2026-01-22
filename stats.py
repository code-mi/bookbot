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


def sort_on(items):
    return items["num"]


def sort_me(dictionary):
    result = list()
    for x, y in dictionary.items():
        tmp = {}
        tmp["char"] = x
        tmp["num"] = y
        result.append(tmp)
    result.sort(reverse=True, key=sort_on)
    return result
