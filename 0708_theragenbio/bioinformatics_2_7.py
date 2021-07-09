#! /usr/bin/env python

codon_dic = {}

while True:
    codon = input("Enter three-base codon to build: ")
    codon = codon.upper()
    if codon == "XXX":
        print("OKay, I will switch")
        break
    aa = input("Enter amino acid: ")
    aa = aa.upper()
    codon_dic[codon] = aa

while True:
    codon = input("Enter three-base codon to serch: ")
    codon = codon.upper()
    if codon == "XXX":
        print("Okay, I will stop.")
        break
    if codon in codon_dic:
        aa = codon_dic[codon]
        print(f"Amino acid for {codon} : {aa}")
    else:
        print("Okay, I will stop")
