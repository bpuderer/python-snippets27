"""string may contain alpha or digits, test if string contains all digits"""

def isdigit_cast(string):
    try:
        int(string)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    import timeit

    print timeit.timeit("'123123123123123123123z789'.isdigit()")
    print timeit.timeit("not any(c.isalpha() for c in '123123123123123123123z789')")
    print timeit.timeit("not bool(re.search(r'[a-zA-Z]', '123123123123123123123z789'))", setup="import re")
    print timeit.timeit("not bool(p.search('123123123123123123123z789'))", setup="import re; p=re.compile(r'[a-zA-Z]')")
    print(timeit.timeit("isdigit_cast('123123123123123123123z789')", setup="from __main__ import isdigit_cast"))
