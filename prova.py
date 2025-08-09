# PYIA-A02 Crie um dicionário que irá armazenar informações de 
# um contato, incluindo o nome, o telefone e o email. 
# Peça ao usuário para fornecer esses dados, solicitando que ele 
# insira o nome do contato, o número de telefone e o endereço de email.
# Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, 
# mostrando todas as informações do contato inserido pelo usuário.

# Criando o dicionário de contato
contato = {}

# Coletando informações do usuário
contato["nome"] = input("Digite o nome do contato: ")
contato["telefone"] = input("Digite o telefone do contato: ")
contato["email"] = input("Digite o email do contato: ")

# Exibindo as informações do contato
print("\nInformações do contato:")
print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")
