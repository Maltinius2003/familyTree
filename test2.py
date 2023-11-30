original_list = [
    ['0', 'None'], ['1', 'Unknown'], ['2', 'Other'], ['3', 'Christianity'], ['4', 'Islam '],
    ['5', 'Judaism'], ['6', 'Hinduism'], ['7', 'Buddhism'], ['8', 'Sikhism'], ['9', 'BahÃ¡Ê¼Ã\xad Faith'],
    ['10', 'Shintoism'], ['11', 'Taoism'], ['12', 'Zoroastrianism'], ['13', 'Jainism'], ['14', 'Confucianism']
]

def transpose_list(input_list):
    transposed_list = []

    # Bestimme die Anzahl der Spalten
    num_columns = len(input_list[0])

    # Iteriere über die Spalten
    for i in range(num_columns):
        # Erstelle eine Liste für die aktuelle Spalte
        current_column = []

        # Iteriere über die Zeilen und füge das i-te Element zur aktuellen Spalte hinzu
        for row in input_list:
            current_column.append(row[i])

        # Füge die aktuelle Spalte zur transponierten Liste hinzu
        transposed_list.append(current_column)

    return transposed_list

transposed_list = transpose_list(original_list)
print(transposed_list)
