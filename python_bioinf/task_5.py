class Sequences:
    weights = {"A": 313.21, "T": 304.2, "C": 289.18, "G": 329.21, "U": 306.17}
    complement_dna = {"A": "T", "G": "C", "T": "A", "C": "G"}
    complement_dna_to_rna = {"A": "U", "G": "C", "T": "A", "C": "G"}
    complement_rna = {"A": "U", "G": "C", "U": "A", "C": "G"}

    def __init__(self, sequences, name, alphabet):
        self.name = name
        self.sequences = sequences
        self.alphabet = alphabet

    def get_alphabet(self):
        print("Alphabet: " + str(self.alphabet))

    def get_name(self):
        print("Name: " + str(self.name))

    def get_sequences(self):
        print("Sequences: " + str(self.sequences))

    def get_sequences_length(self):
        print("Sequences length: " + str(len(self.sequences)))

    def get_statistics(self):
        stat = "Невозможно получить статистику"
        if self.name == 'DNA':
            stat = "A:" + str(self.sequences.count('A')) + ", C:" + str(self.sequences.count('C')) + ", G:" + str(
                self.sequences.count('G')) + ", T:" + str(self.sequences.count('T'))
        elif self.name == 'RNA':
            stat = "A:" + str(self.sequences.count('A')) + ", C:" + str(self.sequences.count('C')) + ", G:" + str(
                self.sequences.count('G')) + ", U:" + str(self.sequences.count('U'))
        print("Статистика по используемым символам:\n" + stat)

    def get_molecular_weight(self):
        molecular_weight = self.weights.get("A") * self.sequences.count('A') \
                           + self.weights.get("T") * self.sequences.count('T') \
                           + self.weights.get("C") * self.sequences.count('C') \
                           + self.weights.get("G") * self.sequences.count('G') \
                           + self.weights.get("U") * self.sequences.count('U')
        print("Molecular weight = " + str(molecular_weight))

    def get_complement(self):
        complemented = ""
        if self.name == 'DNA':
            for i in self.sequences:
                complemented += self.complement_dna.get(i)
        if self.name == 'RNA':
            for i in self.sequences:
                complemented += self.complement_rna.get(i)
        else:
            complemented = "Невозможно использовать принцип комплементарности"
        print(complemented)

    def get_complement_dna_to_rna(self):
        complemented = ""
        if self.name == 'DNA':
            for i in self.sequences:
                complemented += self.complement_dna.get(i)
        else:
            complemented = "Невозможно использовать принцип комплементарности"
        print(complemented)


class DNA(Sequences):
    def __init__(self, sequences, name="DNA", alphabet={'A', 'C', 'G', 'T'}):
        # используем метод __init__ суперкласса
        super().__init__(sequences, name, alphabet)


class RNA(Sequences):
    codon = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
             "UCU": "S", "UCC": "s", "UCA": "S", "UCG": "S",
             "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
             "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
             "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
             "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
             "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
             "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
             "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
             "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
             "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
             "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
             "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
             "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
             "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
             "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }

    def __init__(self, sequences, name="RNA", alphabet={'A', 'C', 'G', 'U'}):
        # используем метод __init__ суперкласса
        super().__init__(sequences, name, alphabet)

    def RNA_to_protein(self):
        res = ""
        triplets = [self.sequences[i:i + 3] for i in range(0, len(self.sequences), 3)]

        for triplet in triplets:
            if self.codon.get(triplet, "X") == "Stop":
                return
            else:
                res += self.codon.get(triplet, "X")
        if res == "":
            res = "трансляция РНК -> белок невозможна"
        print(res)


if __name__ == "__main__":
    a = RNA("AUGAAUGCGAGGAGUUCUACCGGCAGGGAAGCAUCAAUGGUCGACAUG")
    a.get_statistics() #A:14, C:9, G:16, U:9
    a.get_alphabet() #Alphabet: {'U', 'A', 'C', 'G'}
    a.get_name() #Name: RNA
    a.get_molecular_weight() #Molecular weight = 15010.449999999999
    a.get_complement() #UACUUACGCUCCUCAAGAUGGCCGUCCCUUCGUAGUUACCAGCUGUAC
    a.RNA_to_protein() #MNARSSTGREASMVDM
