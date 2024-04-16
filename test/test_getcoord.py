import pytest
from getcoord.getcoord import get_coords

def test_api():
  townname="Москва"
  place=get_coords(townname)
  assert (townname in place['features'][0]['properties']['description'])
  
