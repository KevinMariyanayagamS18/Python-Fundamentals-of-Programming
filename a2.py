def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return dna1>dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    total_nucleotide=0

    for i in dna:
        if i in nucleotide:
            total_nucleotide=total_nucleotide+1

    return total_nucleotide


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    

    return dna2 in dna1


def is_valid_sequence(DNA):
    """(str)-> bool
    Return True if and only if DNA has other dna strands other than A,T,C,G.
    mna will increase by one if a letter in the DNA string is invalid,
    causing the mistakes to be greater than zero and outputting False.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATYGGC')
    False

    """
    mna=0
    for i in DNA:
        if i in 'ATGC':
            mna=mna
        else:
            mna+=1

    return mna==0

def is_2_valid_sequence(DNA2):
    """(str)->bool
    Return True if and only if DNA2 does not contain any invalid
    strands of dna letters from the if statement string.

    >>> is_2_valid_sequence('ATCGGC')
    True
    >>> is_2_valid_sequence('ATYGGC')
    False

    """

    Dna=True

    for i in DNA2:
        if i in'BDEFHIJKLMNOPQRSUVWXYZ':
            Dna=False
        
    return Dna

def insert_sequence(dna3,dna4,num):
    """(str, str, int) -> str
    Return new_dna which takes the two dna samples, dn3 and dna4,
    then uses num to slice dna3 so that dna4 is inserted
    at the index stated to create the new dna string.

    >>>insert_sequence(dna3,dna4,num)
    
    >>>insert_sequence(dna3,dna4,num)

    """

    new_dna=dna3[0:num]+ dna4 + dna3[num:len(dna3)]

    return new_dna



def get_complement(strand_dna):
    """(str) -> str"""
    if strand_dna in 'A':
        return'T'
    elif strand_dna in 'T':
        return'A'
    elif strand_dna in 'G':
        return'C'
    else:
        return'G'


def get_complementary_sequence(test_dna):
    """(str) -> str
    Return the DNA sequence that is complementary to the given
    DNA sequence.

    >>>get_complement_sequence(test_dna)

    >>>get_complement_sequence(test_dna)

    """
    test_sequence=""

    for i in test_dna:
        test_sequence+=get_complement(i)

    return test_sequence
        
    
    
