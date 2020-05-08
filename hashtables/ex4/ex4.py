def has_negatives(a):

    """
    YOUR CODE HERE
    """
    result = []
    cache = {}
    for num in a:
        # if num not in cache:
        #     cache[num] = num
        if abs(num) in cache:
            # print(abs(num))
            # print(cache[num])
            # if abs(num) + abs(cache[abs(num)]) == abs(num) * 2:
                # print(num, [cache])
            if num < 0 and cache[abs(num)] == 'pos':
                result.append(abs(num))
            elif num > 0 and cache[abs(num)] == 'neg':
                result.append(abs(num))
        else:
            if num < 0:
                cache[abs(num)] = 'neg'
            else:
                cache[num] = 'pos'
    # print(result)
    # print(cache)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
