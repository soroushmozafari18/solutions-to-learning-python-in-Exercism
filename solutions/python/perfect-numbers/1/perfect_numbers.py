def classify(number):
    aliquot=[]
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        for i in range(1,number-1):
            if not number%i:
                aliquot.append(i) 
            else:
                pass
    if sum(aliquot)==number:
        return 'perfect'
    if sum(aliquot)>number:
        return 'abundant'
    if sum(aliquot)<number:
        return 'deficient'
            
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
