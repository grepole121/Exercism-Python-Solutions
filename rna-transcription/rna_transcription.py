def to_rna(dna_strand):
    if dna_strand == "":
        return ""
    dna = ("A", "T", "C", "G")
    rna = ("U", "A", "G", "C")
    out = ""
    for char in dna_strand:
        out = out + (rna[dna.index(char)])
    return out