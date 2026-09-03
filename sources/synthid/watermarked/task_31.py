def dna_complement(dna):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return ''.join(complement[i] for i in dna)
