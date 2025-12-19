def sum_of_multiples(limit, multiples):
    final_set=set()
    for multiple in multiples:
        if multiple!=0:
            final_set=final_set|set(i for i in range(1,limit) if  not i%multiple )
    return sum(final_set)