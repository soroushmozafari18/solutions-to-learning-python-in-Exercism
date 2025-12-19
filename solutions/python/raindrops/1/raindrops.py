def convert(number):
    output_string=''
    if  number%3==0:
        output_string+='Pling'
    if number%5==0:
        output_string+='Plang'
    if number%7==0:
        output_string+='Plong'
    if not number%3==0 and not number%5==0 and not number%7==0:
        output_string=str(number)
    return output_string
        
