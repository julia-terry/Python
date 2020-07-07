all_aminos = ['Arg', 'Gly', 'Pro', 'His', 'Lys', 'Ala', 'Ile', 'Leu', 'Met', 'Val', 'Phe', 'Trp', 'Tyr', 'Asn', 'Cys']
all_aminos2 = ['Gln', 'Thr', 'Ser', 'Asp', 'Glu']
hydrophobic_aliphatic = ['Ala', 'Ile', 'Leu', 'Met', 'Val']
hydrophobic_aromatic = ['Phe', 'Trp', 'Tyr']
polar_neutral = ['Asn', 'Cys', 'Gln', 'Thr', 'Ser']
acidic = ['Asp', 'Glu']
basic = ['Arg', 'His', 'Lys']
unique = ['Gly', 'Pro']

#get an amino acid code from user
aa = input("Please enter one of the 20 three-letter amino acid codes:")

#capitalize, strip white space, and print out user input
aa = aa.capitalize()
aa = aa.strip()
print("You entered: " + aa)

#make sure the input is a three-letter amino acid code
while aa in all_aminos or all_aminos2:

    #go through lists to find the property of the amino acid and print
    if aa in hydrophobic_aliphatic or hydrophobic_aromatic:
        print(aa + " is hydrophobic")
        break
    if aa in polar_neutral:
        print(aa + " is polar neutral")
        break
    if aa in acidic:
        print(aa + " is acidic")
        break
    if aa in basic:
        print(aa + " is basic")
        break
    if aa in unique:
        print(aa + " is unique")
        break
