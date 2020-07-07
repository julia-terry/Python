#read in FASTA genome file (seqs only)
def readFile (fileName):
    DNA = open(fileName)
    lines = DNA.readlines()
    sequence = []
    for i in range (0, len(lines)):
        if lines[i][0:1] != ">":
            sequence.append(lines[i].strip("\n"))
    DNA.close()
    sequence = ''.join(sequence)
    return sequence

#read in FASTA genome file (seqs only) using a generator
#How to call:
#with open("nameFile.faa") as fp:
    #for name, seq in readFASTA(fp):
        #print(name,seq)
def readFASTA(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield(name, ''.join(seq))
            name,seq = line, []
        else:
            seq.append(line)
    if name: yield(name, ''.join(seq))

#read in fastq file using a generator
#How to call:
#with open("fastqFileName") as infastq:
    #for iname, iseq, iqual in readFASTQ(infastq):
        #readlen = iname.split()[2]
        #qualities = [ord(x) - 33 for x in iqual]
        #avgqual = sum(qualities) / len(qualities)
def readFASTQ(fastq):
    name, seq, qual = [None], [None], [None]
    for i, line in enumerate(fastq):
        line = line.strip()
        if i % 4 == 0:
            name = line
        elif i % 4 == 1:
            seq = line
        elif i % 4 == 3:
            qual = line
            yield name, seq, qual
            name, seq, qual = [None], [None], [None]
        else:
            pass

#get a list of names/descriptions in the FASTA file (follows > in file)
def readNames(fileName):
    DNA2 = open(fileName)
    lines2 = DNA2.readlines()
    names = []
    for j in range(0, len(lines2)):
        if lines2[j][0:1] == ">":
            names.append(lines2[j].strip("\n"))
    names = ''.join(names)
    DNA2.close()
    splitNames = names.split(">")
    return splitNames

#split the file using the pstl restriction enzyme site
def splitPST (readFileName):
    firstSite = "CTGCAG"
    splitSeq = readFileName.split(firstSite)
    return splitSeq

#calculate GC percentage
def gcPercentage (useableSequence):
    for j in range(0, len(useableSequence)):
        seq= useableSequence[j].upper()
        gcount = seq.count("G")
        ccount = seq.count("C")
        DNAlength = len(seq)
        totalCount = ((gcount+ccount)/DNAlength)*100
    return totalCount

#call above functions
readFileSeq = readFile("mock.faa")
readFileNames = readNames("mock.faa")
newSplitSeq = splitPST(readFileSeq)
newGCPercentage = gcPercentage(newSplitSeq)

#make a new .txt with the first name/description, the gc percentage of entire FASTA file, and all the seqs in FASTA file
finalOutput = open("finalOutput.txt", "w")
finalOutput.write("> " + readFileNames[1] + "\n" + "GC:" + str(newGCPercentage) + "%\n" + readFileSeq)
finalOutput.close()

