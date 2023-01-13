def twoNumberSum(array, targetSum):
    hashtable = {}
    for i in range(len(array)):
        y = targetSum - array[i]
        if y in hashtable:
            return[y, array[i]]
        else:
            hashtable[array[i]] = True
    return []
