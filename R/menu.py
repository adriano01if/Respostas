from professor import *

print("Registre-se: ")

nome = input('Nome: ')

disciplina = input('Disciplina que irá lecionar: ')

professor1 = Professor(nome, disciplina)

print("MENU DE OPÇÕES: ")

#Menu opções:
print("""
--------------------------------------------
|                                          |
|  [1] - Cadastrar nova disciplina:        |
|                                          |
|  [2] - Cadastrar nova atividade:         |
|                                          |
|  [3] - Lista atividades pendentes:       |
|                                          |
|  [4] - Lista atividades concluídas:      |
|                                          |
|  [5] - Marcar atividade como concluída:  |
|                                          |
|  [6] - Sair:                             |
|------------------------------------------|
""")

regra = True

while regra == True:

  opcao = int(input("Escolha alguma dessas opções: "))
  print('=' * 50)

  if opcao == 1:
    nome = input('Nome da disciplina: ')
    professor1.adicionar_disciplina(nome)
    print('=' * 50)

  elif opcao == 2:
    nome = input('Nome da atividade: ')
    data = input('Data da atividade: ')
    descricao = input('Descrição da atividade: ')
    disciplina = input("Disciplina da atividade: ")
    professor1.add_atividade(nome, data, descricao, disciplina)
    print('=' * 50)
  elif opcao == 3:
    professor1.listar_aberto()
  elif opcao == 4:
    professor1.listar_concluidas()
  elif opcao == 5:
    nome = input('Nome da atividade: ')
    disciplina = input('Nome da disciplina: ')
    professor1.marcar_concluida(nome, disciplina)
    print('=' * 50)
  elif opcao == 6:
    print("Fim de codigo! Obrigado por utilizar nosso sistema.")
    regra = False
  else:
    print("opção inválida, tente novamente")
    print("=" * 50)