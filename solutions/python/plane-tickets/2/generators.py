def generate_seat_letters(number):
    mylist=['A','B','C','D']
    count=0
    while count<number:
        yield mylist[count%4]
        count+=1
def generate_seats(number):
    mylist=['A','B','C','D']
    count=0
    if number>=48:
        number+=4
    while count<number:
        if count//4+1!=13:
            yield str(count//4+1)+mylist[count%4]
        count+=1     
def assign_seats(passengers):
    main_dic=dict()
    my_seats=generate_seats(len(passengers))
    for name in passengers:
        main_dic[name]=next(my_seats)
    return main_dic
def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        ticket_id=seat+flight_id
        while len(ticket_id)!=12:
            ticket_id+='0'
        yield ticket_id