from bank import value


def test_Hello():
    assert value("hello world") == "$0"
    assert value("HELLO WORLD") == "$0"
    assert value("h3ll0 w0rld") == "$20"
    assert value("4@llo w*rld!!!") == "$100"
    
def test_H():
    assert value("hi world") == "$20"
    assert value("Hi WORLD") == "$20"
    assert value("hEllO w0rld") == "$0"
    assert value("41 w*rld!!!") == "$100"

def test_No():
    assert value("4i world") == "$100"
    assert value("78 WORLD") == "$100"
    assert value("HElLo w0rld") == "$0"
    assert value("h1 w*rld!!!") == "$20"
    
test_Hello()
test_H()
test_No()
