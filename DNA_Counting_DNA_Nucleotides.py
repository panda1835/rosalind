f = open('Dataset/rosalind_dna.txt', 'r')
dna_sequence = f.read()
f.close()

A = 0
T = 0
G = 0
C = 0
for i in dna_sequence:
    if i == 'A':
        A += 1
    if i == 'T':
        T += 1
    if i == 'G':
        G += 1
    if i == 'C':
        C += 1

print(A,C,G,T)