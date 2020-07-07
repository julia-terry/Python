#utilize SequenceConditionalsTest.txt to test the code

dnaSeq = input("Input a DNA sequence: ")
dnaSeq2 = dnaSeq[0:10]
frag = dnaSeq.find('TACGTACG')
print(" ")

#make sure the starting sequence is greater than 50 nucleotides
if len(dnaSeq) > 50:

    #if sequence TACGTACG is present in the first 10 nucleotides, print whole sequence
    if frag < 10 and frag >= 0:
        print(dnaSeq)
        print("Sequence has 'TACGTACG' in the first 10 nucleotides ")

    #if sequence is present after first 10, print a trimmed sequence to the right of said sequence if more than or equal to 50 nucleotides
    elif "TACGTACG" in dnaSeq:
        endOfAdapter = dnaSeq.find("TACGTACG") + 8
        dnaSeq3 = dnaSeq[endOfAdapter :]

        if len(dnaSeq3) >= 50:
            print(dnaSeq3)
            print("Trailing sequence is longer than 50 nucleotides and original sequence has 'TACGTACG' within it (but not the first 10)")
        else:
            print("Trailing sequence is shorter than 50 nucleotides and original sequence has 'TACGTACG' within it (but not the first 10)")

    else:
        print("Sequence does not contain 'TACGTACG'")

#notify user if sequence was not longer than 50 nucleotides
else :
    print("Sequence isn't long enough")

