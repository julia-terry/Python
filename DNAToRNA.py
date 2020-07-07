#Get user input
DNAseq = input("Please input a DNA sequence: ")

#Prints out DNA sequence in all uppercase
DNAseq = DNAseq.upper()
print("DNA sequence: " + DNAseq)

#Prints out the length of DNA sequence
DNAlength = len(DNAseq)
print("Length of sequence: " + str(DNAlength))

#Prints out the T count of the DNA sequence
tCount = DNAseq.count("T")
print("Number of Ts in sequence: " + str(tCount))

#Prints out the RNA sequence
RNAseq = DNAseq.replace("T", "U")
print("RNA sequence: " + RNAseq)