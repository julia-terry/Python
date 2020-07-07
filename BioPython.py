#In terminal before proceeding:
#pip install numpy
#pip install biopython

#create a seq (similar to string)
import Bio
from Bio.Seq import Seq
mySeq = Seq("ATGCATGC")

#set alphabet attribute (similar to key-value pair)
#import Bio
#from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
myAlphabetSeq = Seq("AGTACACTGGT", IUPAC.unambiguous_dna)
#access key: myAlphabetSeq
#access value: myAlphabetSeq.alphabet

#complementing/reverse complementing nucleotides
#import Bio
#from Bio.Seq import Seq
#from Bio.Alphabet imort IUPAC
dnaSeq = Seq("GTAACCCTTAGCACTGGT", IUPAC.unambiguous_dna)
dnaSeqComplement = dnaSeq.complement() #CATTGGGAATCGTGACCA
dnaSeqReverseComplement = dnaSeq.reverse_complement() #ACCAGTGCTAAGGGTTAC

#transcribe dna
codingDNA = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
templateDNA = codingDNA.reverse_complement()
messengerRNA = codingDNA.transcribe() #AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG
#reverse transcription (codingDNA)
dnaFromMRNA = messengerRNA.back_transcribe()

#translation from RNA sequence
#import Bio
#from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
mRNA = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)
translation = mRNA.translate() #MAIVMGR*KGAR*

#stop at a stop codon
codingDNA.translate(to_stop= True) #MAIVMGR
codingDNA.translate(table= 2, to_stop= True) #MAIVMGRWKGAR

#Bio.Data (includes standard coding tables based on NCBI's)
from Bio.Data import CodonTable
standardTable = CodonTable.unambiguous_dna_by_name["Standard"]
mitoTable = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
#using NCB table ids:
#standardTable = CodonTable.unambiguous_dna_by_id[1]
#mitoTable = CodonTable.unambiguous_dna_by_id[2]

#Create your own SeqRecord object
#import Bio
#from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
tmp = Seq("MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF")
tmpR = SeqRecord(tmp)
tmpR.id = "YP_025292.1"
tmpR.description = "toxic membrane protein"
tmpR.name = "HokC"

#Create your own SeqRecord object with alphabet attribute
#import Bio
#from Bio.Seq import Seq
#from Bio.SeqRecord import SeqRecord
#from Bio.Alphabet import IUPAC
record = SeqRecord(seq=Seq('MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF'), id='YP_025292.1',
                   name='HokC', description='toxic membrane protein', dbxrefs=[])
#SeqRecord in FASTA format
recordFASTA = record.format("fasta")

#get SeqRecord from DBS
#import Bio
from Bio import Entrez
from Bio import SeqIO
Entrez.email = 'julianicoleterry@gmail.com'
handle = Entrez.efetch(db="nucleotide",rettype="fasta",id="6273291")
seqRecord = SeqIO.read(handle, "fasta")
handle.close()
seqRecordDescription = seqRecord.description

#converting file formats
#import Bio
#from Bio import SeqIO
inHandle = open("AP006852.gbk", "r")
outHandle = open("AP006852.fasta", "w")
records = SeqIO.parse(inHandle, "genbank")
count = SeqIO.write(records, outHandle, "fasta")
inHandle.close()
outHandle.close()




