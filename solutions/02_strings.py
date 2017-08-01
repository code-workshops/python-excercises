# Custom Functions
def first_last(s):
    """Return the first and last letter of a string."""
    return "{0} {1}".format(s[0], s[-1])

def letter_swap(a,b):
    """Given two words, swap the first letter of each and return the new string."""
    new_second = a[0] + b[1:]
    new_first = b[0] + a[1:]
    return "{0} {1}".format(new_first, new_second)

def censor(word):
    """
    Take the first letter of a word and replace all occurences of it with #.
    Do not change the first letter of the word, only the next appearances.
    """
    return word[0] + word[1:].replace(word[0], '#')
    
def counter():
    """
    Write a function that counts from 1 to 100. Return the numbers 
    divisble by 10.
    """
    results = []
    for number in range(100):
        if number % 10 == 0:
            results.append(number)       
    return results

# Testing Tools
# The functions below help us test the functions we created above.
def test(input, output):
    if input == output:
        result = '\u2714 Pass'
    else:
        result = '\u2718 Pass'
    print("{0} - Actual Output: {1}, Expected Output: {2}".format(result, input, output))
    
def run_tests():
    """Test that our functions work the way we think they do."""
    print("Testing first_last() ...")
    test(first_last('building'), 'b g')
    test(first_last('car'), 'c r')
    print('\n')
    
    print("Testing letter_swap() ...")
    test(letter_swap('beer', 'cheese'), 'ceer bheese')
    test(letter_swap('doctor', 'couch'), 'coctor douch')
    print('\n')
    
    print("Testing censor()...")
    test(censor('scissor'), 'sci##or')
    test(censor('cry'), 'cry')
    test(censor('tricky test'), 'tricky #es#')
    
    print("Testing counter() ...")
    test(counter(), (10,20,30,40,50,60,70,80,90,100))
    print("\n")
run_tests()
