import re
def enzyme_cut(DNA_sequence,recognised_sequence):
    if re.findall('[^ATCG]',DNA_sequence):
        return('ERROR: DNA sequence contains invalid characters')
    elif re.findall('[^ATCG]',recognised_sequence):
        return('ERROR: recognised sequence contains invalid characters')
    else:
        find_sequence='[ATCG]*?'+recognised_sequence
        sequence=re.findall(find_sequence,DNA_sequence)
        if len(sequence)==0:
            return('Sorry,the recognized sequence is not found in the DNA sequence.')
        else:
            position_list=[]
            for i in (0,len(sequence)):
                where=str(sequence[i])
                position=len(where)-len(recognised_sequence)+1
                position_list.append(position)
            return(position_list)

position_result=enzyme_cut('AGGTGGAATTCCGCGGGCCCGGGTAGCGTA','GAATTC')
print(position_result)