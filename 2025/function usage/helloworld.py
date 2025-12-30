def hello():
    # return sends value back to caller
    return "Hello, World!"

print(hello())

def test_hello():
    assert hello() == "Hello, World!"

test_hello()
print("Test passed")
