"""
Regras do FizzBuzz!

1- Se a posição for múltiplo de 3: fizz
2- Se a posição for múltipli de 5: buzz
3- Se a posição for múltiplo de 3 e 5: fizzbuzz
4- Para qualquer outra posição será o próprio n°.
"""

import pytest

def jogo(pos):
  exit = str(pos)
  if pos % 3 == 0 and pos % 5 == 0:
    exit = 'fizzbuzz'
  elif pos % 3 == 0:
    exit = 'fizz'
  elif pos % 5 == 0:
    exit = 'buzz'
  return exit


def test_jogo():
  assert jogo(1) == '1'
  assert jogo(2) == '2'
  assert jogo(4) == '4'
  
  assert jogo(3) == 'fizz'
  assert jogo(6) == 'fizz'
  assert jogo(9) == 'fizz'

  assert jogo(5) == 'buzz'
  assert jogo(10) == 'buzz'
  assert jogo(20) == 'buzz'

  assert jogo(15) == 'fizzbuzz'
  assert jogo(30) == 'fizzbuzz'
  assert jogo(45) == 'fizzbuzz'


if __name__ == "__main__":
  pytest.main(['-svv', __file__])
  
