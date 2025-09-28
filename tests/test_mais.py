import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

def test_soma():
    assert main.soma(2, 3) == 5
    assert main.soma(-1, 1) == 0

def test_subtrair():
    assert main.subtrair(5, 2) == 3
    assert main.subtrair(0, 3) == -3

def test_multiplicar():
    assert main.multiplicar(3, 4) == 12
    assert main.multiplicar(-2, 5) == -10

def test_dividir():
    assert main.dividir(10, 2) == 5
    assert main.dividir(9, 3) == 3
    assert main.dividir(10, 0) == "Erro: divisão por zero"
