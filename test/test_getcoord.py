import pytest
from getcoord.getcoord import get_coords

def test_api():
  townname="Москва"
  place=get_coords(townname,"somekey")
  assert ("Key is required" == place['message'])
  
