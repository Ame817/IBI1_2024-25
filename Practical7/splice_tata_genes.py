import re
combinations=input('please input one of: GTAG, GCAG, ATAC\n')
if combinations in ['GTAG','GCAG','ATAC']:
    filename=combinations+'_genes.fa'
    open_file=open(filename,'w')
else:
    print('Sorry, this is not one of the possible donor/acceptor combinations')

openfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
input_0=openfile.read()
input=re.sub('\n','',input_0)


tata_sequence=re.findall(r'>[^>]+?TATA[AT]A[AT][ATCG]*',input)

for i in range(0,len(tata_sequence)-1):
    sequence=str(tata_sequence[i])
    gene_name=re.findall(r'>(\S+?)[_\s]',sequence)
    tata_count=re.findall('TATA[AT]A[AT]',sequence)
    count=len(tata_count)
    open_file.write(str(gene_name[0]))
    open_file.write('\n')
    open_file.write(str(count))
    open_file.write('\n')
open_file.close()