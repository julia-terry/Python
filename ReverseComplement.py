#get input from user
DNAseq = input("Enter a DNA sequence: ")

#make input all lower case
DNAseq = DNAseq.lower()

#make complement dna
RvCompl = DNAseq.replace("a", "T"). replace("t", "A"). replace("c", "G"). replace("g", "C")

#print reverse complement dna
print(RvCompl[::-1])