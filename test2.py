def trenne_string(string):
    teile = []
    trennsymbole = []

    aktuelles_teil = ""
    for char in string:
        if char == ' ' or char == '-':
            if aktuelles_teil:
                teile.append(aktuelles_teil)
                aktuelles_teil = ""
            trennsymbole.append(char)
        else:
            aktuelles_teil += char

    if aktuelles_teil:
        teile.append(aktuelles_teil)

    return teile, trennsymbole

# Beispielverwendung:
eingabe_string = "Hallo-Welt ist ein Beispiel-String"

teile, trennsymbole = trenne_string(eingabe_string)

print("Teile:", teile)
print("Trennsymbole:", trennsymbole)

def baue_liste_zusammen(teile, trennsymbole):
    namePartListStr = []

    for i in range(len(teile)):
        namePartListStr.append(teile[i])
        if i < len(trennsymbole):
            namePartListStr.append(trennsymbole[i])

    return namePartListStr

# Beispielverwendung:
zusammengesetzte_liste = baue_liste_zusammen(teile, trennsymbole)
print("Zusammengesetzte Liste:", zusammengesetzte_liste)