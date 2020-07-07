myDNA = "GATTATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCACATTATTTATTTATTTATACAGATTATGCATGCATGCATGCATGCACATTATTTATTTATTTATTTATTTATTTATTTATTTATTTATTTATTTATACAGATTATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCACATATAAAAAAAA"
myIntronDNA = "GATTATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCACATTATTTATTTATTTATACAGATTATGCATGCATGCATGCATGCACATTATTTATTTATTTATTTATTTATTTATTTATTTATTTATTTATTTATACAGATTATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCACATATAAAAAAAA"
exons = []
introns = []
i = 0

#list of exons in myDNA that start with GATT and end with ACA
while len(myDNA) >= 3:

    #find exon that starts with GATT and ends with ACA
    exonStart = myDNA.find("GATT")
    exonEnd = myDNA.find("ACA") + 3
    exonSeq = myDNA[exonStart:exonEnd]

    #change myDNA to include all myDNA after exonEnd
    myDNA = myDNA[exonEnd :]

    #add exon sequence to exon list
    if len(exonSeq) >= 3 :
        exons.append(exonSeq)

#print exon list from myDNA
print("Exons:")
print(exons)

#list of introns in myDNA that end with ACA but start with something else
while len(myIntronDNA) >= 3 :

    # find intron that ends with ACA
    intronEnd = myIntronDNA.find("ACA") + 3
    intronSeq = myIntronDNA[:intronEnd]

    # change myIntronDNA to include all myIntronDNA after intronEnd
    myIntronDNA = myIntronDNA[intronEnd:]

    # add intron sequence to intron list
    if len(intronSeq) >=3 :
        introns.append(intronSeq)

#print intron list from myIntronDNA
print("Introns:")
print(introns)

#concatinate exons
exonsString = "".join(exons)

#print concatinated exon list from myDNA
print("Concatinated exons: ")
print(exonsString)
