import hprose

if __name__ == "__main__":
    client = hprose.HttpClient('http://localhost:8181/')

    # Testando métodos
    print("Executando testes no serviço distribuído:")

    # Teste Update
    print("Criando chave 'alpha':", client.update('alpha', 10))
    print("Atualizando chave 'alpha':", client.update('alpha', 20))

    # Teste Get
    print("Consultando chave 'alpha':", client.get('alpha'))
    print("Consultando chave 'beta' inexistente:", client.get('beta'))

    # Teste Remove
    print("Removendo chave 'alpha':", client.remove('alpha'))
    print("Removendo chave 'beta' inexistente:", client.remove('beta'))

    # Consultando após remoção
    print("Consultando chave 'alpha' após remoção:", client.get('alpha'))
