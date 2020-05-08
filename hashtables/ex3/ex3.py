def intersection(arrays):

    """
    YOUR CODE HERE
    """

    result = []
    cache = {}
    
    # May want to rewrite this as a binary search 
    # Iterate through the shortest list, and BS the other 2
    # Should be O((log n) * 2) at least
    for element in arrays:
        for arr in element:
            if arr not in cache:
                cache[arr] = 1
            else:
                cache[arr] += 1
                if cache[arr] == len(arrays):
                    result.append(arr)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
