import re
blosum62 = {
    'A': {'A': 4,  'R': -1, 'N': -2, 'D': -2, 'C': 0,  'Q': -1, 'E': -1, 'G': 0,  'H': -2, 'I': -1,
          'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1,  'T': 0,  'W': -3, 'Y': -2, 'V': 0},
    'R': {'A': -1, 'R': 5,  'N': 0,  'D': -2, 'C': -3, 'Q': 1,  'E': 0,  'G': -2, 'H': 0,  'I': -3,
          'L': -2, 'K': 2,  'M': -1, 'F': -3, 'P': -2, 'S': -1, 'T': -1, 'W': -3, 'Y': -2, 'V': -3},
    'N': {'A': -2, 'R': 0,  'N': 6,  'D': 1,  'C': -3, 'Q': 0,  'E': 0,  'G': 0,  'H': 1,  'I': -3,
          'L': -3, 'K': 0,  'M': -2, 'F': -3, 'P': -2, 'S': 1,  'T': 0,  'W': -4, 'Y': -2, 'V': -3},
    'D': {'A': -2, 'R': -2, 'N': 1,  'D': 6,  'C': -3, 'Q': 0,  'E': 2,  'G': -1, 'H': -1, 'I': -3,
          'L': -4, 'K': -1, 'M': -3, 'F': -3, 'P': -1, 'S': 0,  'T': -1, 'W': -4, 'Y': -3, 'V': -3},
    'C': {'A': 0,  'R': -3, 'N': -3, 'D': -3, 'C': 9,  'Q': -3, 'E': -4, 'G': -3, 'H': -3, 'I': -1,
          'L': -1, 'K': -3, 'M': -1, 'F': -2, 'P': -3, 'S': -1, 'T': -1, 'W': -2, 'Y': -2, 'V': -1},
    'Q': {'A': -1, 'R': 1,  'N': 0,  'D': 0,  'C': -3, 'Q': 5,  'E': 2,  'G': -2, 'H': 0,  'I': -3,
          'L': -2, 'K': 1,  'M': 0,  'F': -3, 'P': -1, 'S': 0,  'T': -1, 'W': -2, 'Y': -1, 'V': -2},
    'E': {'A': -1, 'R': 0,  'N': 0,  'D': 2,  'C': -4, 'Q': 2,  'E': 5,  'G': -2, 'H': 0,  'I': -3,
          'L': -3, 'K': 1,  'M': -2, 'F': -3, 'P': -1, 'S': 0,  'T': -1, 'W': -3, 'Y': -2, 'V': -2},
    'G': {'A': 0,  'R': -2, 'N': 0,  'D': -1, 'C': -3, 'Q': -2, 'E': -2, 'G': 6,  'H': -2, 'I': -4,
          'L': -4, 'K': -2, 'M': -3, 'F': -3, 'P': -2, 'S': 0,  'T': -2, 'W': -2, 'Y': -3, 'V': -3},
    'H': {'A': -2, 'R': 0,  'N': 1,  'D': -1, 'C': -3, 'Q': 0,  'E': 0,  'G': -2, 'H': 8,  'I': -3,
          'L': -3, 'K': -1, 'M': -2, 'F': -1, 'P': -2, 'S': -1, 'T': -2, 'W': -2, 'Y': 2,  'V': -3},
    'I': {'A': -1, 'R': -3, 'N': -3, 'D': -3, 'C': -1, 'Q': -3, 'E': -3, 'G': -4, 'H': -3, 'I': 4,
          'L': 2,  'K': -3, 'M': 1,  'F': 0,  'P': -3, 'S': -2, 'T': -1, 'W': -3, 'Y': -1, 'V': 3},
    'L': {'A': -1, 'R': -2, 'N': -3, 'D': -4, 'C': -1, 'Q': -2, 'E': -3, 'G': -4, 'H': -3, 'I': 2,
          'L': 4,  'K': -2, 'M': 2,  'F': 0,  'P': -3, 'S': -2, 'T': -1, 'W': -2, 'Y': -1, 'V': 1},
    'K': {'A': -1, 'R': 2,  'N': 0,  'D': -1, 'C': -3, 'Q': 1,  'E': 1,  'G': -2, 'H': -1, 'I': -3,
          'L': -2, 'K': 5,  'M': -1, 'F': -3, 'P': -1, 'S': 0,  'T': -1, 'W': -3, 'Y': -2, 'V': -2},
    'M': {'A': -1, 'R': -1, 'N': -2, 'D': -3, 'C': -1, 'Q': 0,  'E': -2, 'G': -3, 'H': -2, 'I': 1,
          'L': 2,  'K': -1, 'M': 5,  'F': 0,  'P': -2, 'S': -1, 'T': -1, 'W': -1, 'Y': -1, 'V': 1},
    'F': {'A': -2, 'R': -3, 'N': -3, 'D': -3, 'C': -2, 'Q': -3, 'E': -3, 'G': -3, 'H': -1, 'I': 0,
          'L': 0,  'K': -3, 'M': 0,  'F': 6,  'P': -4, 'S': -2, 'T': -2, 'W': 1,  'Y': 3,  'V': -1},
    'P': {'A': -1, 'R': -2, 'N': -2, 'D': -1, 'C': -3, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -3,
          'L': -3, 'K': -1, 'M': -2, 'F': -4, 'P': 7,  'S': -1, 'T': -1, 'W': -4, 'Y': -3, 'V': -2},
    'S': {'A': 1,  'R': -1, 'N': 1,  'D': 0,  'C': -1, 'Q': 0,  'E': 0,  'G': 0,  'H': -1, 'I': -2,
          'L': -2, 'K': 0,  'M': -1, 'F': -2, 'P': -1, 'S': 4,  'T': 1,  'W': -3, 'Y': -2, 'V': -2},
    'T': {'A': 0,  'R': -1, 'N': 0,  'D': -1, 'C': -1, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -1,
          'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1,  'T': 5,  'W': -2, 'Y': -2, 'V': 0},
    'W': {'A': -3, 'R': -3, 'N': -4, 'D': -4, 'C': -2, 'Q': -2, 'E': -3, 'G': -2, 'H': -2, 'I': -3,
          'L': -2, 'K': -3, 'M': -1, 'F': 1,  'P': -4, 'S': -3, 'T': -2, 'W': 11, 'Y': 2,  'V': -3},
    'Y': {'A': -2, 'R': -2, 'N': -2, 'D': -3, 'C': -2, 'Q': -1, 'E': -2, 'G': -3, 'H': 2,  'I': -1,
          'L': -1, 'K': -2, 'M': -1, 'F': 3,  'P': -3, 'S': -2, 'T': -2, 'W': 2,  'Y': 7,  'V': -1},
    'V': {'A': 0,  'R': -3, 'N': -3, 'D': -3, 'C': -1, 'Q': -2, 'E': -2, 'G': -3, 'H': -3, 'I': 3,
          'L': 1,  'K': -2, 'M': 1,  'F': -1, 'P': -2, 'S': -2, 'T': 0,  'W': -3, 'Y': -1, 'V': 4}
}


#percentage identical amino acids
human=open('P04179.fasta','r')
mouse=open('P09671.fasta','r')
random=open('random.fasta','r')
human_seq=human.read()
mouse_seq=mouse.read()
random_seq=random.read()
seq1=re.findall(r'(?:^|\n)>.*\n((?:[A-Z]+\n?)+)',human_seq)[0]
seq2=re.findall(r'(?:^|\n)>.*\n((?:[A-Z]+\n?)+)',mouse_seq)[0]
seq3=re.findall(r'(?:^|\n)>.*\n((?:[A-Z]+\n?)+)',random_seq)[0]

seq1=seq1.replace('\n','')
seq2=seq2.replace('\n','')
seq3=seq3.replace('\n','')
print(len(seq1),len(seq2),len(seq3))
distance_12=0
for i in range(len(seq1)):
               if seq1[i]!=seq2[i]:
                       distance_12+=1
percentage12=(1-distance_12/len(seq1))
print('The percentage of identical amino acids between human and mouse sequence is:',100*percentage12,'%')
distance_23=0
for i in range(len(seq1)):
               if seq3[i]!=seq2[i]:
                       distance_23+=1
percentage23=(1-distance_23/len(seq1))
print('The percentage of identical amino acids between mouse and random sequence is:',100*percentage23,'%')
distance_13=0
for i in range(len(seq1)):
               if seq1[i]!=seq3[i]:
                       distance_13+=1
percentage13=(1-distance_13/len(seq1))
print('The percentage of identical amino acids between human and random sequence is:',100*percentage13,'%')

#alignment score
score12=0
for i in range(len(seq1)):
      acid1=seq1[i]
      acid2=seq2[i]
      score12+=blosum62[acid1][acid2]
print('The alignment score of human and mouse sequence is:',score12)

score23=0
for i in range(len(seq1)):
      acid2=seq2[i]
      acid3=seq3[i]
      score23+=blosum62[acid2][acid3]
print('The alignment score of mouse and random sequence is:',score23)

score13=0
for i in range(len(seq1)):
      acid1=seq1[i]
      acid3=seq3[i]
      score13+=blosum62[acid1][acid3]
print('The alignment score of human and random sequence is:',score13)