# A little database we can use to check information
database = ['King', 'cookies', 'street', 'rain', 'computer', 7]

# Custom Functions
def greet(name):
    """Given a name, return the greeting 'Nice to meet you, <name>'."""
    # Your code here
    
def exists(val):
    """
    Check the database to see if val is already stored there.
    """
    # Your code here

def convert_to_celcius(temp):
    """
    CHALLENGE!
    Given a temperature in Fahrenheit, convert it to celcius and return it.
    Formula: http://www.celsius-to-fahrenheit.com/
    """
    # Your code here
    

# Testing Tools
# The functions below help us test the functions we created above.
def test(inpt, output):
    """
    This is a simple function to test that the results of our function
    match what we expect. Get used to writing these! As you learn, 
    you'll find more and better tools to help you test your code.
    
    Fancy unicode check marks: https://en.wikipedia.org/wiki/Check_mark
    """
    if inpt == output:
        result = '==> \u2714 Pass'
    else:
        result = '==> \u2718 Fail'
    print("{0} - input: {1}, expected output: {2}".format(result, inpt, output))
    
def run_tests():
    """Test that our functions work the way we think they do."""
    print("Testing greet() ...")
    test(greet('Terry'), 'Nice to meet you, Terry!')
    test(greet(007), 'Nice to meet you, 007!')
    print("\n\n")
      
    print("Testing exists() ...")
    test(exists('King'), True)
    test(exists('Queen'), False)
    print("\n\n")
    
    print("Testing convert_to_celcius()...")
    test(convert_to_celcius(73), 23)
    test(convert_to_celcius(57), 14)
    print("\n\n")

run_tests()
