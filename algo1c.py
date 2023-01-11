def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentsum = array[left] + array[right]
        if currentsum == targetSum:
            return [array[left], array[right]]
        elif currentsum < targetSum:
            left += 1
        elif currentsum > targetSum:
            right -= 1
    return []