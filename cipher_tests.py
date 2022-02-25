from cipher import *

def test_generate_pad():
    assert generate_pad(length = 4) !=  generate_pad(length=4)

def test_shiftamount ():
    assert shiftamount("AADD") == shiftamount ("AADD")



