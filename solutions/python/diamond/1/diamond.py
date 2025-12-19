def rows(letter):
    alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters_used=alphabets[:alphabets.index(letter)+1]
    my_list=[]
    rows_count=2*len(letters_used)-1
    my_list.append(int((rows_count-1)/2)*' '+'A'+(int((rows_count-1)/2)*' '))
    for i in range(1,rows_count-1):
        my_list.append(((int(abs((rows_count-1)/2-i))*' '))+letters_used[int(-abs(i-((rows_count-1)/2))+((rows_count-1)/2))]+(int(-abs(2*(i-((rows_count-1)/2)))+rows_count-2)*' ')+letters_used[int(-abs(i-((rows_count-1)/2))+((rows_count-1)/2))]+(int(abs((rows_count-1)/2-i))*' '))
    if letters_used!='A':
        my_list.append(int((rows_count-1)/2)*' '+'A'+(int((rows_count-1)/2)*' '))
    return my_list