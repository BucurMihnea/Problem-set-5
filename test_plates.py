from code_plates import is_valid


def test_len():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAAAA") == False
    
def test_firt_char():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False

def test_punct():
    assert is_valid(" ,") == False
    assert is_valid(".:") == False
    assert is_valid(";!") == False  
    assert is_valid("??") == False
    
def test_num():
    assert is_valid("AAA111") == True
    assert is_valid("111AAA") == False
    assert is_valid("A1111A") == False
    assert is_valid("AAA011") == False
    
test_len()
test_firt_char()
test_punct()
test_num
