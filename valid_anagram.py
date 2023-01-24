def is_anagram(str1, str2):
    # remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # edge case check
    if len(str1) != len(str2):
        return False

    # create a frequency dictionary for each string
    count1 = {}
    count2 = {}
    for i in str1:
        if i in count1:
            count1[i] += 1
        else:
            count1[i] = 1

    for i in str2:
        if i in count2:
            count2[i] += 1
        else:
            count2[i] = 1

    # compare the frequency dictionaries
    for key in count1:
        if key in count2:
            if count1[key] != count2[key]:
                return False
        else:
            return False

    return True
