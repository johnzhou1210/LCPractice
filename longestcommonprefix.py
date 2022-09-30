def allCharsSame(arr, indx, result):
    allCharsMustBe = arr[0][indx]
    for word in arr:
        if word[indx] != allCharsMustBe:
            return ""
    return result + arr[0][indx]

def Solution(strs):
    #first get shortest word
    shortestWordLen = 201
    shortestWordIndx = -1
    longestCommonPrefix = ""
    for i,v in enumerate(strs):
        if len(strs[i]) < shortestWordLen:
            shortestWordLen = len(strs[i])
            shortestWordIndx = i
            
    # check all indices simulatenously
    for i,v in enumerate(strs[shortestWordIndx]):
        # check to see if all the characters are the same for the ith index
        newPrefix = allCharsSame(strs, i, longestCommonPrefix)
        if newPrefix == "":
            break
        longestCommonPrefix = newPrefix
    return longestCommonPrefix
   
def main():
    pass

if __name__ == "__main__":
    main()
    