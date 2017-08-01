# Custom Functions
def first_last(s):
    """Return the first and last letter of a string."""
    # Your code here

def letter_swap(a,b):
    """Given two words, swap the first letter of each and return the new string."""
    # Your code here

def censor(word):
    """
    Take the first letter of a word and replace all occurences of it with #.
    Do not change the first letter of the word, only the next appearances.
    """
    # Your code here

def counter():
    """
    Write a function that counts from 1 to 100. Return the numbers 
    divisble by 10. (10, 20, 30, 40)
    """
    # Your code here
    
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
    
    print("Testing counter() ...")
    test(counter(), (10,20,30,40,50,60,70,80,90,100))
    print("\n")

run_tests()
