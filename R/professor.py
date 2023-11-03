from atividade import Atividade
from disciplina import Disciplina


class Professor(Atividade, Disciplina):
  def __init__(self, nome, disciplina):
    self.nome = nome
    self.atvdd_concluidas = []
    self.atvdd_acessivel = []
    self.a_disciplinas = []
    self.a_disciplinas.append(Disciplina(disciplina))

  def adicionar_disciplina(self,disciplina):
      for mudar_disciplina in self.a_disciplinas:
        if mudar_disciplina.nome == disciplina:
          print(f"A disciplina {disciplina} já está cadastrada.")
          return None
      self.a_disciplinas.append(Disciplina(disciplina))

  
  def add_atividade(self,nome,data,descricao,disciplina):
      for mudar_disciplina in self.a_disciplinas:
        if mudar_disciplina.nome == disciplina:
          for mudar_atividade in mudar_disciplina.atv_atividade:
            if mudar_atividade.nome == nome:
              print("Erro: atividade já existe.")
              return None
            elif mudar_atividade.data == data:
              print("Erro: datas iguais na mesma disciplina.")
              return None
            else:
              pass
          atividade = Atividade(nome,data,descricao,disciplina)
          self.atvdd_acessivel.append(atividade)
          
          mudar_disciplina.atv_atividade.append(atividade)
          return None
        else:
          pass

      else:
        print("Erro: disciplina não existe.")



  def marcar_concluida(self,nome, disciplina):
    if not len(self.atvdd_acessivel) and not len(self.atvdd_concluidas):
      print("Você ainda não cadastrou nenhuma atividade.")
    else:
      for mudar_disciplina in self.a_disciplinas:
        if mudar_disciplina.nome == disciplina:
          for mudar_atividade in mudar_disciplina.atv_atividade:
            if mudar_atividade.nome == nome:
              if mudar_atividade.concluida:
                print("Erro: atividade concluída.")
                return None
              else:
                mudar_atividade.concluida = True
                self.atvdd_acessivel.remove(mudar_atividade)
                self.atvdd_concluidas.append(mudar_atividade)
                print("Atividade marcada como concluída.")
                return None
          else:
            print('Atividade não encontrada.')
            
        else:
          pass
      else:
        print("Dicisplina enexistente.")

  def listar_concluidas(self):
    if  not len(self.atvdd_acessivel) and not len(self.atvdd_concluidas):
      print('Você não adicionou nenhuma atividade.')
      print('='*40)
    elif not len(self.atvdd_concluidas):
      print("Você ainda não tem atividades concluídas.")
      print('='*40)
    else:
      for pos, atv_concluida in enumerate(self.atvdd_concluidas):
        print(f'Posição na lista: {pos}')
        print(f'Nome: {atv_concluida.nome}')
        print(f'Data: {atv_concluida.data}')
        print(f'Descrição: {atv_concluida.descricao}')
        print(f'Disciplina: {atv_concluida.disciplina}')
        print(f'Concluída: {atv_concluida.concluida}')
        print('='*40)
  def listar_aberto(self):
    if not  len(self.atvdd_acessivel) and not len(self.atvdd_concluidas):
      print('Nenhuma atividade adicionada.')
      print('='*40)
    elif not len(self.atvdd_acessivel):
      print('nenhuma atividade pendente.')
      print('='*40)
    else:
      for pos, atv_aberta in enumerate(self.atvdd_acessivel):
        print(f'Posição na lista: {pos}')
        print(f'Nome: {atv_aberta.nome}')
        print(f'Data: {atv_aberta.data}')
        print(f'Descrição: {atv_aberta.descricao}')
        print(f'Disciplina: {atv_aberta.disciplina}')
        print(f'Concluída: {atv_aberta.concluida}')
        print('='*40)
