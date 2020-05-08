def finder(files, queries):

    """
    YOUR CODE HERE
    """
    result = []
    cache = {}
    # queries = set(queries)

    for path in queries:
        if path not in cache:
            cache[path] = path
    for fn in files:
        filename = fn.split('/')[-1]
        if filename in cache:
            result.append(fn)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
