
def step(n, row, str=""):
    if n==row:
        return
    if len(str) == n:
        print(str)
        step(n,row+1,"")
        return
    if len(str) <= row:
        str = str +"#"
    else:
        str = str + " "
    step(n,row,str)


if __name__ == "__main__":
    step(10,0,"")
