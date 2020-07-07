dna = "AATTGGCC"
counts = {}

#loop through all the possible combinations of A, T, C, and G
for base1 in ['A','T','C','G']:
    for base2 in ['A','T','C','G']:
        for base3 in ['A','T','C','G']:
            trin = base1 + base2 + base3

            #see how many times that particular combination shows up in dna variable
            count = dna.count(trin)

            #assign the key "trin" to the value "count" if it is in our dna variable
            if count > 0:
                counts[trin] = count

#print out the counts dictionary
print(counts)