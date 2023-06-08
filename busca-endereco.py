import requests

print("<==== Buscador de Endereço ====>\n")

#Funcao
def isnumber(value):
  try:
    float(value)
  except ValueError:
    return False
  return True


cep = input("Digite o cep: ")

#substitui uma string
cep = cep.replace("-", "")


if (isnumber(cep) == False):
  print("digite um cep valido.")
else:
  url = "https://viacep.com.br/ws/" + cep + "/json"

  response = requests.get(url)

  if (response.status_code == 200):
    result = response.json()
  
    print("\ncep: " + result['cep'])
    print("logradouro: " + result['logradouro'])
    print("bairro: " + result['bairro'])
    print("localidade: " + result['localidade'])
    print("uf: " + result['uf'])
  else:
    print("cep não encontrado")
    
input("")
