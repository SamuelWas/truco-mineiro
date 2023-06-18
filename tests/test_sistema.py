# import pytest
# import subprocess
# import warnings

# warnings.filterwarnings("ignore")

# @pytest.mark.cmd
# def test_escolher_2_como_num_jogadores():
#     path =  r"C:\Users\rodrigo.braz\Rodrigo_Si\tp_testesoftware\truco-mineiro\main.py"
        
#     processo = subprocess.Popen(['python', path], text= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#     processo.stdin.write('2' + "\n")
#     processo.stdin.write('Rodrigo' + "\n")
#     processo.stdin.write('Andre Hora' + "\n")

#     output, errors = processo.communicate()
#     processo.stdin.close()

#     assert 'Escolha o nome do jogador 1' in output
#     assert 'Escolha o nome do jogador 2' in output
    
#     assert 'Escolha o nome do jogador 3' not in output
#     assert 'Escolha o nome do jogador 4' not in output

# @pytest.mark.cmd
# def test_escolher_4_como_num_jogadores():
#     path =  r"C:\Users\rodrigo.braz\Rodrigo_Si\tp_testesoftware\truco-mineiro\main.py"
        
#     processo = subprocess.Popen(['python', path], text= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#     processo.stdin.write('4' + "\n")
#     processo.stdin.write('Rodrigo' + "\n")
#     processo.stdin.write('Ana' + "\n")
#     processo.stdin.write('Samuel' + "\n")
#     processo.stdin.write('Heitor' + "\n")


#     output, errors = processo.communicate()
#     processo.stdin.close()

#     assert 'Escolha o nome do jogador 1' in output
#     assert 'Escolha o nome do jogador 2' in output
    
#     assert 'Escolha o nome do jogador 3' in output
#     assert 'Escolha o nome do jogador 4' in output
