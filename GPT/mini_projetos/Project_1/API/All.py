import requests

id_solicitado = int(input(
    "Informe uma opção:\n"
    "1 - Consultar post\n"
    "2 - Criar post\n"
    "3 - Atualizar post\n"
    "4 - Remover post\n"
))

if id_solicitado == 1:

    id_post = int(input("Informe o ID do post: "))
    url = f"https://jsonplaceholder.typicode.com/posts/{id_post}"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados_json = resposta.json()

        print(f"Título: {dados_json['title']}")
        print(f"Conteúdo: {dados_json['body']}")

    elif resposta.status_code == 404:
        print("Post não encontrado.")

    else:
        print(f"Status retornado: {resposta.status_code}")

elif id_solicitado == 2:

    titulo = input("Informe o título: ")
    corpo = input("Informe o conteúdo: ")

    dados = {
        "title": titulo,
        "body": corpo,
        "userId": 0
    }

    url = "https://jsonplaceholder.typicode.com/posts/"

    resposta = requests.post(url, json=dados)
    dados_json = resposta.json()

    if resposta.status_code == 201:
        print(f"Post criado com sucesso! \nTítulo retornado: {dados_json['title']}\nID retornado: {dados_json['id']}")
    else:
        print(f"Código retornado: {resposta.status_code}")

elif id_solicitado == 3:

    id_post = int(input("Informe o ID: "))
    titulo = input("Informe o título: ")
    corpo = input("Informe o corpo: ")

    dados = {
        "title": titulo,
        "body": corpo
    }
    url = f"https://jsonplaceholder.typicode.com/posts/{id_post}"
    resposta = requests.put(url, json=dados)

    if resposta.status_code == 200:
        print("Post atualizado com sucesso!")

        dados_json = resposta.json()

        print(f"Título devolvido: {dados_json['title']}")
        print(f"Conteúdo devolvido: {dados_json['body']}")

    elif resposta.status_code == 404:
        print(f"Status {resposta.status_code}: Not Found!")
    else:
        print(f"O status reportado foi {resposta.status_code}.")


elif id_solicitado == 4:
    id_post = int(input("Informe o ID do post que deseja remover: "))
    url = f"https://jsonplaceholder.typicode.com/posts/{id_post}"
    resposta = requests.delete(url)

    if resposta.status_code in [200, 204]:
        print("Post removido com sucesso!")
    elif resposta.status_code == 404:
        print("Post não encontrado.")
    else:
        print(f"O status reportado foi {resposta.status_code}.")

else:
    print("Informe uma opção válida!")