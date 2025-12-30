def rev_string(strng):
    return strng[::-1]
    
my_string = input("Enter String to reverse:\n")

print(rev_string(my_string))

def test_rev_string():
    assert rev_string("hello") == "olleh"
    assert rev_string("sudha") == "ahdus"
    assert rev_string("") == ""

test_rev_string()
print("Test Successful")
