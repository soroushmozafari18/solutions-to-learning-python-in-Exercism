def classify(number):
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
       aliquot=sum(factor for factor in range(1,number-1)if not number%factor)
    if aliquot== number:
        return 'perfect'
    elif aliquot > number:
        return 'abundant'
    else:
        return 'deficient'
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
