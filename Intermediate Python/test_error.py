from error import addArrays

# this is correctnes testing

def test_add():
    a = [1,2,3]
    b = [4,5,6]
    expect = [5,7,100]
    c = addArrays(a,b)
    assert expect == c

if __name__ == "__main__":
    test_add()
