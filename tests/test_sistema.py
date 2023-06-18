import pytest
import subprocess
import warnings
import os

warnings.filterwarnings("ignore")

#prepara o path para o arquivo main.py
@pytest.fixture
def path():
    current_dir = os.path.abspath(os.path.dirname(__file__))

    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    path_main = os.path.join(parent_dir, "main.py")
    
    return path_main

@pytest.mark.cmd
def test_escolher_2_como_num_jogadores(path):
        
    processo = subprocess.Popen(['python', path], text= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    processo.stdin.write('2' + "\n")
    processo.stdin.write('Rodrigo' + "\n")
    processo.stdin.write('Andre Hora' + "\n")

    output, errors = processo.communicate()
    processo.stdin.close()

    assert 'Escolha o nome do jogador 1' in output
    assert 'Escolha o nome do jogador 2' in output
    
    assert 'Escolha o nome do jogador 3' not in output
    assert 'Escolha o nome do jogador 4' not in output

@pytest.mark.cmd
def test_escolher_4_como_num_jogadores(path):
        
    processo = subprocess.Popen(['python', path], text= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    processo.stdin.write('4' + "\n")
    processo.stdin.write('Rodrigo' + "\n")
    processo.stdin.write('Ana' + "\n")
    processo.stdin.write('Samuel' + "\n")
    processo.stdin.write('Heitor' + "\n")


    output, errors = processo.communicate()
    processo.stdin.close()

    assert 'Escolha o nome do jogador 1' in output
    assert 'Escolha o nome do jogador 2' in output
    
    assert 'Escolha o nome do jogador 3' in output
    assert 'Escolha o nome do jogador 4' in output
