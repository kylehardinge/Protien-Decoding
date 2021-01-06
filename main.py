# Protein synthesis lab decoding lab

def convert_to_protein():
    input_str = input("Input the string to be converted: ")
    mrna = convert_to_mrna(input_str)
    protein = convert_to_amino_acid(mrna)
    readable_protein = array_to_sentence(protein)
    code = decode(protein)
    print(mrna)
    print(readable_protein)
    print(code)


def conversion(char):
    if char == "A":
        return "U"
    elif char == "T":
        return "A"
    elif char == "C":
        return "G"
    elif char == "G":
        return "C"
    elif char == " ":
        return " "
    else:
        return char


def convert_to_mrna(input_str):
    output_str = ""
    for i in range(len(input_str)):
        output_str = output_str + conversion(input_str[i])
    return output_str


def convert_to_amino_acid(input_str):
    output = []
    input_str = input_str.replace(" ", "")
    for i in range(int(len(input_str)/3)):
        output.append(mrna_to_amino[input_str[(i+1)*3-3]+input_str[(i+1)*3-2]+input_str[(i+1)*3-1]])
    return output


def array_to_sentence(input):
    output = ", ".join(input)
    return output


def decode(input_array):
    output = ""
    for i in range(len(input_array)):
        output = output + decoding_symbols[input_array[i]]
    return output


mrna_to_amino = {
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",
    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "GAU": "Aspartic acid",
    "GAC": "Aspartic acid",
    "GAA": "Glutamic acid",
    "GAG": "Glutamic acid",
    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UAA": "Stop",
    "UAG": "Stop",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGA": "Stop",
    "UGG": "Tryptophan",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",
    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "AUG": "Methionine",
    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",
    "AGU": "Serine",
    "AGC": "Serine",
    "AGA": "Arginine",
    "AGG": "Arginine",
}

decoding_symbols = {
    "Alanine": "A",
    "Arginine": "R",
    "Asparagine": "N",
    "Aspartic acid": "D",
    "Cysteine": "C",
    "Glutamic acid": "E",
    "Glutamine": "Q",
    "Glycine": "G",
    "Histidine": "H",
    "Isoleucine": "I",
    "Leucine": "L",
    "Lysine": "K",
    "Methionine": "M",
    "Phenylalanine": "F",
    "Proline": "P",
    "Serine": "S",
    "Threonine": "T",
    "Tryptophan": "W",
    "Tyrosine": "Y",
    "Valine": "V",
    "Stop": " "
}


if __name__ == '__main__':
    convert_to_protein()


