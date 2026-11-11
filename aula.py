# allan 


# relatorio FastDelivery Logística

#VARIAVEIS 👇

nome = "Beatriz Santos"

data_execuçao = "10/11/2026"

testes_aprovados = 65

testes_reprovados = 5

testes_nao_executados = 10

data = "10/11/2026"

modulo = "Rastreamento e Geolocalização em Tempo Real"

projeto = "FastDelivery Logística"

Total_de_testes = testes_aprovados + testes_reprovados + testes_nao_executados
Testes_executados = testes_aprovados + testes_reprovados
Taxa_de_aprovação = (testes_aprovados/Testes_executados) * 100 
Taxa_de_reprovação = (testes_reprovados /Testes_executados ) * 100 
Taxa_de_não_executados = (testes_nao_executados /Total_de_testes) * 100 

#Mikael

print("======================================== RELATÓRIO DE EXECUÇÃO DE TESTES ========================================")
print("Projeto: " + projeto)
print("Modulo: " + modulo) 
print("responsavel: " + nome)
print("Data de Execução " + data)   
print(f"Testes Aprovado: {testes_aprovados}" )
print(f"Testes Reprovados: {testes_reprovados}" )
print(f"Testes Não Executados: {testes_nao_executados} " )
print("----------------------------------------REGISTRO CONCLUÍDO-------------------------------------- ")

#parte 3 (Bryan)

print(f"Total de testes: {Total_de_testes:}")
print(f"Testes executados: {Testes_executados}")
print(f"Taxa de aprovação: {Taxa_de_aprovação:.2f}%")
print(f"Taxa de reprovação:{Taxa_de_reprovação:.2f}%")
print(f"Taxa de não executados:{Taxa_de_não_executados:.2f}%")

 



 