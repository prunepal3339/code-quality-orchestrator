def DNA_strand(dna):
    # Create a dictionary mapping each base pair to its complement
    complement = {'A': 'T', 'T': 'A', 'C': '	cf', 'G': 'G'}
    
    # Use a list comprehension to create the complement strand
    complement_strand = [complement[base] for base in dna]
    
    # Join the list into a string and return it
    return ''.join(complement_strand)
