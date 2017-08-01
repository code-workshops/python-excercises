# Databases
# These object will act as a source of data

# Custom Functions
def to_list(s):
    """Convert the given string s into a list."""
    return s.split('')

def to_string(l):
    """Convert the given list l into a string. Each should be separated by a space."""
    l.join(' ')

def merge(list_k,list_v):
    """
    Take two lists: one has keys and the other values. Return a dictionary.
    """
    return dict(zip(list_k, list_v))

def char_count(word):
    """
    Count the number of times each letter occurs in a given word. Return
    a dictionary with each letter as a key and their count as values.
    """
    counter = {}
    for letter in word:
        if not letter in counter.keys():
            counter[letter] = 0
        else:
            counter[letter] += 1
    return counter
    

def is_palindrome(word):
    """
    Given a word, determine if it's a palindrome. Ignore case.
    """
    reversed = ''
    limit = len(word)
    count = 1
    while limit > 0:
        for letter in word:
            reversed += word[-count]
        limit -= -1
        count += 1
    return reversed
    
def count_by(num):
    """
    Write a function that counts from 1 to 300. Return the numbers
    divisible by num in a list. If the number is greater than 
    300 return 'Number too big!'
    """
    results = []
    for i in range(300):
        if num > 300:
            return 'Number too big!'
        elif i % num == 0:
            results.append(num)
            # return [c for c in range(300) if c % num == 0]
    
    return results

def squares(max):
    """
    Given a max number, return a list of the squares between 1 and max.
    """
    return [s**s for s in range(max)]
    
# Testing Tools
# The functions below help us test the functions we created above.
def test(input, output):
    """
    Fancy unicode check marks: https://en.wikipedia.org/wiki/Check_mark
    """
    if input == output:
        result = '==> \u2714 Pass'
    else:
        result = '==> \u2718 Fail'
    print("{0} - input: {1}, expected output: {2}".format(result, input, output))
    
def run_tests():
    """Test that our functions work the way we think they do."""
    print("Testing first_last() ...")
    test(first_last('building'), 'b g')
    test(first_last('car'), 'c r')
    print("\n")
    
    print("Testing letter_swap() ...")
    test(letter_swap('beer', 'cheese'), 'ceer bheese')
    test(letter_swap('doctor', 'couch'), 'coctor douch')
    print("\n")
    
    print("Testing censor() ...")
    test(censor('oblong'), 'obl#ng')
    test(censor('bad'), 'bad')
    print("\n")

run_tests()
