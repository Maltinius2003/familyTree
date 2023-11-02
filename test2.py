def string_to_parts(nameStr, sepSymbolsList):
    parts = []
    sepSymbols = []
    currentPart = ""

    for symbol in sepSymbolsList:
        nameStr = nameStr.strip(symbol)

    for char in nameStr:
        if char in sepSymbolsList:
            if currentPart:
                parts.append(currentPart)
                currentPart = ""
            sepSymbols.append(char)
        else:
            currentPart += char

    if currentPart:
        parts.append(currentPart)

    return parts, sepSymbols

print(string_to_parts("Hans-Peter ddghg", [' ', '-']))