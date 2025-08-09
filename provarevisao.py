# [PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos.
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o 
# preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, 
# calcule o valor total da compra somando todos os preços armazenados no dicionário. 
# Por fim, exiba o valor total da compra.

# Criar um dicionário vazio
produtos = {}

# Inserindo 5 produtos
for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    produtos[nome] = preco  

# Calcular o valor total
valor_total = sum(produtos.values())

# Exibir resultado
print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

print(f"\nValor total da compra: R$ {valor_total:.2f}")
