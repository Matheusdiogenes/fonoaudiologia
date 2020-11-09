import time
import os


def cabecalho(serie, exercicio, seg, index):
  print(f'Exercicio {index+1}: {exercicio}')
  print(f'{serie+1}° Serie')
  print(f'[{seg*"#"}{(60-seg)*"_"} ]')


def temp(exercicio, series, index):  
  for serie in range(series):
    for seg in range(60):
      cabecalho(serie, exercicio, seg, index)
      time.sleep(0.5)
      os.system('clear')
    print('Descanso de 3 segundos')
    time.sleep(3)


def main():
  exercicios = ['U - I','ESTRALAR LINGUA (BOCA FECHHADA)','INFLAR BOCHECHA E SEGURAR', 
            'LINGUA NA BOCHECHA (DIREITA & ESQUERDA)',
            'MASTIGAÇÃO EXAGERADA', 'LA-A LA-O LA-U', 'LA-A LA-E LA-I',
            'MOVIMENTAR A LINGUA - SENTIDO HORÁRIO / ANTI-HORÁRIO']
  
  for e in exercicios:
    temp(e, 2, exercicios.index(e))    


if __name__ == "__main__":
  main()
