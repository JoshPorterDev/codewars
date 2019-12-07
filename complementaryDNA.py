def DNA_string(dna):
    """ Takes in a DNA string and returns its complementary value """
    DNA = list(dna)
    complementaryStrandList = []
    for char in DNA:
        if char == 'A':
            complementaryStrandList.append('T')
        elif char == 'T':
            complementaryStrandList.append('A')
        elif char == 'C':
            complementaryStrandList.append('G')
        elif char == 'G':
            complementaryStrandList.append('C')

    return ''.join(complementaryStrandList)

print(DNA_string('CATGACCGT'))




