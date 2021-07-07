#! /usr/bin/env python

CMA = "1,234,567"

print(CMA.replace(',', ''))
print(int(CMA.replace(',',''))+100)

gene = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGT\
GTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

print(gene.count('A'))
print(gene.count('C'))
print(gene.count('G'))
print(gene.count('T'))

dnaString = 'GATGGAACTTGACTACGTAAATT'
print(dnaString.replace('T', 'U'))

