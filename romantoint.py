def romanToInt(s):
    result = 0
    # find anything that looks like this first: IV,IX  XL,XC CD,CM
    for i,v in enumerate(s):
        if v == "I":
            result = result + 1
            if i + 1 <= len(s) - 1:
                if s[i+1] == "V" or s[i+1] == "X":
                    result = result - 2;
                    print("in here " + str(result))
        elif v == "V":
            result = result + 5
        elif v == "X":
            result = result + 10
            if i + 1 <= len(s) - 1:
                if s[i+1] == "L" or s[i+1] == "C":
                    result = result - 20;
        elif v == "L":
            result = result + 50
        elif v == "C":
            result = result + 100
            if i + 1 <= len(s) - 1:
                if s[i+1] == "D" or s[i+1] == "M":
                    result = result - 200;
        elif v == "D":
            result = result + 500
        elif v == "M":
            result = result + 1000
    return result

def main():
    pass

if __name__ == "__main__":
    main()