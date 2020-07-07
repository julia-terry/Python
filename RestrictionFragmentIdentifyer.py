#processes the fasta file into a single DNA sequence
DNA = open("NC_007898.fasta")
lines = DNA.readlines()
sequence = []
for i in range(0, len(lines)):
    if lines[i][0:1] != ">":
        sequence.append(lines[i].strip("\n"))
sequence = ''.join(sequence)
DNA.close()

#list of fragments split using Pstl restriction site pattern
firstSite = "CTGCAG"
splitSeq = sequence.split(firstSite)

#get first and last seqs
firstSeq = splitSeq[0]
lastSeqIndex = len(splitSeq) - 1
lastSplitSeq = (splitSeq[lastSeqIndex])

#reverse last seq
reversedLastSplitSeq = lastSplitSeq[::-1]

#join first and reversed last seq
firstAndLast = firstSeq + reversedLastSplitSeq

#delete first and last element from orig seqlist and add the modified seq
del splitSeq[lastSeqIndex]
del splitSeq[0]
splitSeq.append(firstAndLast)

#print first 20 characters of each frag with its length
for i in splitSeq:
    print("Fragment starting with: %s" % i[:20])
    print("Length: %s" % len(i))