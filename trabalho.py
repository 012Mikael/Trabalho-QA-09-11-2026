#BRYAN

#ThinkCenter

###🟡 Squad 3


responsavel = "Beatriz Santos"
data = "10/11/2026"
testes_aprovados = 65
testes_reprovados = 5
data_execucao = "10/11/2026"
modulo = "Rastreamento e Geolocalização em Tempo Real"
projeto = "FastDelivery Logística"
testes_nao_executados = 10

Total_de_testes = (testes_aprovados + testes_reprovados + testes_nao_executados)

testes_executados = (testes_aprovados + testes_reprovados)

Taxa_de_aprovação = (testes_aprovados / testes_executados ) * 100

Taxa_de_reprovação = (testes_reprovados / testes_executados) * 100

Taxa_de_não_executados = (testes_nao_executados / Total_de_testes) * 100
 
print("======================================== RELATÓRIO DE EXECUÇÃO DE TESTES ========================================")
print ("Projeto: "+ projeto)
print ("Modulo: "+ modulo)
print ("Responsável: "+ responsavel)
print ("Data: "+ data_execucao)
print (f"Aprovados: {testes_aprovados}")
print (f"Reprovados: {testes_reprovados}")
print (f"Executados: {testes_nao_executados}")
print("---------------------------------------- RESULTADOS REGISTRADOS ----------------------------------------")


print("----------------------------------------MÉTRICAS DA EXECUÇÃo----------------------------------------")

print (f"Total de testes: {Total_de_testes}")
print (f"Testes executados: {testes_executados}")
print(f"Taxa De aprovação: {Taxa_de_aprovação:.2f}%")
print(f"Taxa de reprovação: {Taxa_de_reprovação:.2f}%")
print(f"Taxa de não executados: {Taxa_de_não_executados:.2f}%")

print("---------------------------------------- CÁLCULOS CONCLUÍDOS ---------------------------------------- ")