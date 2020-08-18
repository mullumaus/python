
def capitalize(instr):
    words = instr.split()
    outstring = ""
    for wd in words:
        if len(wd) == 1:
            wd = wd[0].upper()
        else:
            wd = wd[0].upper() + str(wd[1:])
        outstring = outstring + " " + str(wd)
    print(str(outstring))


def capitalize1(instr):
    outString=instr[0].upper()
    for i in range(1,len(instr)):
        if instr[i-1] == " ":
            outString = outString + instr[i].upper()
        else:
            outString = outString + instr[i]
    return  outString


if __name__ == "__main__":
    #instr = "a short sentence"
    #instr = "a lazy fox!"
    instr = "coding interview by mastering data structures!"
    print(capitalize1(instr))
