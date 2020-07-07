#get input from user
DNAinput = input("Enter a DNA sequence: ").upper().strip()

#function to calculte the percentage of G and Cs and return said percentage
def gcCalc (DNAseq):
    gcount = DNAseq.count("G")
    ccount = DNAseq.count("C")
    DNAlength = len(DNAseq)
    totalcount = ((gcount+ccount)/DNAlength)*100
    return totalcount

#run the function with our user input and print result
gclist = gcCalc(DNAinput)
print("The GC percentage is: " + str(gclist) + "%")