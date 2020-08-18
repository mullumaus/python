
def maxchar(str):
    dict ={}
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] = dict[str[i]] + 1
        else:
            dict[str[i]] = 1

    maxvalue = 0
    for key in dict:
        if dict[key] > maxvalue:
            maxvalue = dict[key]
            mchar = key
    print("{} occur {} time".format(mchar,maxvalue))


if __name__ == "__main__":
    maxchar("dskandklllllll")
