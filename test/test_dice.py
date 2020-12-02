import pytest
from tasks import dice

def test_roll():
    assert dice.randm <=6
    assert dice.randm >= 1