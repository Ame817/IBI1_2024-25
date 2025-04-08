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
            where=str(sequence[0])
            position=len(where)-len(recognised_sequence)+1
            return('The position of the recognized sequence of the restriction enzyme is '+str(position))

position_result=enzyme_cut('AGGTGGAATTCCGCGGGCCCGGGTAGCGTA','GAATTC')
print(position_result)