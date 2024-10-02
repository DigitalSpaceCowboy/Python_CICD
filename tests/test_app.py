import sys
import os
import pytest 

# root directory 
sys.path.insert(0, r'C:\Users\NickJ\Python_CICD')

from app import multiply, divide

def test_multiply():
    assert multiply(2, 5) == 10
    assert multiply(0, 5) == 0
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(10, 0)  # This should raise an error for division by zero
