def twoNumberSum(array, targetSum):
    hashtable = {}
    for i in array:
        y = targetSum - i
        if y in hashtable:
            return[y, i]
        else:
            hashtable[i] = True
    return []