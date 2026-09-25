print("------------------------------------------------------------")
print("Bem-vindo ao sistema de gerenciamento de estoque do mercado!")
print("------------------------------------------------------------")

resposta = int(input("Deseja visualizar o estoque atual? (1-Sim / 2-Não): "))
if resposta == 1:
    item_escolhido = int(input("Escolha qual item deseja visualizar(1-Arroz / 2-Feijão / 3-Macarrão / 4-Açúcar / 5-Sal): "))
    if item_escolhido == 1:    
        print("Item: Arroz")
        print("Código: 1")
        print("Quantidade: 50")
        print("Preço: R$ 5.00")
    elif item_escolhido == 2:
        print("Item: Feijão")
        print("Código: 2")
        print("Quantidade: 30")
        print("Preço: R$ 8.00")
    elif item_escolhido == 3:
        print("Item: Macarrão")
        print("Código: 3")
        print("Quantidade: 40")
        print("Preço: R$ 3.00")
    elif item_escolhido == 4:
        print("Item: Açúcar")
        print("Código: 4")
        print("Quantidade: 20")
        print("Preço: R$ 4.00")
    elif item_escolhido == 5:
        print("Item: Sal")
        print("Código: 5")
        print("Quantidade: 50")
        print("Preço: R$ 2.00")

else:
    print("Obrigado por utilizar o sistema de gerenciamento de estoque do mercado!")

def obter_estoque():
    estoque = [
        {"nome": "Arroz", "codigo": "1", "quantidade": 50, "preco": 5.0},
        {"nome": "Feijão", "codigo": "2", "quantidade": 30, "preco": 8.0},
        {"nome": "Macarrão", "codigo": "3", "quantidade": 40, "preco": 3.0},
        {"nome": "Açúcar", "codigo": "4", "quantidade": 20, "preco": 4.0},
        {"nome": "Sal", "codigo": "5", "quantidade": 50, "preco": 2.0},
    ]
    return estoque
exibir_valor_total = int(input("Deseja exibir o valor total do estoque? (1-Sim / 2-Não): "))
if exibir_valor_total == 1:
    print("Exibindo o valor total do estoque...")
    valor_total = 0
    for item in obter_estoque():
        valor_total += item["quantidade"] * item["preco"]
    print("O valor total do estoque é: R$ {:.2f}".format(valor_total))
else:
    print("Obrigado por utilizar o sistema de gerenciamento de estoque do mercado!")

