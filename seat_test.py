import pytest
from main import Seat

@pytest.fixture
def seat():
    return Seat()

def test_fwd(seat):
    seat.fwd()
    assert seat.pos == 49

def test_bwd(seat):
    seat.bwd()
    assert seat.pos == 51