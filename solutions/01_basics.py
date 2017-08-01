# A little database we can use to check information
database = ['King', 'cookies', 'street', 'rain', 'computer', 7]

# Custom Functions
def greet(name):
    """Given a name, return the greeting 'Nice to meet you, <name>'."""
    return "Nice to meet you, {0}!".format(name)
    
def is_saved(val):
    """
    Check the database to see if val is already stored there.
    """
    return val in database

def convert_to_celcius(temp):
    """
    Given a temperature in Fahrenheit, convert it to celcius and return it.
    Formula: http://www.celsius-to-fahrenheit.com/
    """
    return ((temp - 32) / 9) * 5

# Testing Tools
# The functions below help us test the functions we created above.
def test(input, output):
    """
    This is a simple function to test that the results of our function
    match what we expect. Get used to writing these! As you learn, 
    you'll find more and better tools to help you test your code.
    
    Fancy unicode check marks: https://en.wikipedia.org/wiki/Check_mark
    """
    if input == output:
        result = '==> \u2714 Pass'
    else:
        result = '==> \u2718 Fail'
    print("{0} - input: {1}, expected output: {2}".format(result, input, output))
    
def run_tests():
    """Test that our functions work the way we think they do."""
    print("Testing greet() ...")
    test(greet('Terry'), 'Nice to meet you, Terry!')
    test(greet(7), 'Nice to meet you, 7!')
    print("\n")
    
    print("Testing is_saved() ...")
    test(is_saved('King'), True)
    test(is_saved('Queen'), False)
    print("\n")
    
    print("Testing convert_to_celcius()...")
    test(convert_to_celcius(32), 0)
    test(convert_to_celcius(68), 20)
    print("\n")

run_tests()
