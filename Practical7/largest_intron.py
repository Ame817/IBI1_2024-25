import re
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intron=re.findall(r'GT.+AG',seq)
length=len(intron[0])
print('the largest intron is',intron[0], 'the length is', length)
