import requests


def escolher_opcao():
    while True:
        try:
            opcao = int(input(
                "1 - Consultar post\n"
                "2 - Criar post\n"
                "3 - Atualizar post\n"
                "4 - Excluir post\n"
                "Escolha: "
            ))
            if opcao in [1, 2, 3, 4]:
                return opcao
            else:
                print("Opção inválida. Digite um número entre 1 e 4.")

        except ValueError:
            print("Você precisa digitar um número.")


def consultar_post(id_post):
    url = f"https://jsonplaceholder.typicode.com/posts/{id_post}"
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        return dados_json


def criar_post(titulo, conteudo):
    dados = {
        "title": titulo,
        "body": conteudo
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts/",
        json=dados
    )

    if response.status_code == 201:
        dados_json = response.json()
        return dados_json


def atualizar_post(id_post, titulo, conteudo):
    dados = {
        "title": titulo,
        "body": conteudo
    }

    response = requests.put(
        f"https://jsonplaceholder.typicode.com/posts/{id_post}",
        json=dados
    )

    if response.status_code == 200:
        dados_json = response.json()
        return dados_json


def excluir_post(id_post):
    response = requests.delete(
        f"https://jsonplaceholder.typicode.com/posts/{id_post}"
    )

    if response.status_code == 200 or response.status_code == 204:
        return True

    return False

def escolher_id():
    while True:
        try:
            id_post = int(input("Informe o ID: "))
        
            if id_post > 0:
                return id_post
            else:
               print("O ID precisa ser um número positivo.")
        except ValueError:
            print("O ID precisa ser um número.")

opcao = escolher_opcao()


if opcao == 1:
    id_post = escolher_id()
    post = consultar_post(id_post)

    if post is not None:
        print(f"Título: {post['title']}")
        print(f"Conteúdo: {post['body']}")
    else:
        print("Post não encontrado.")


elif opcao == 2:
    titulo = input("Informe o título do post: ")
    conteudo = input("Informe o conteúdo do post: ")

    post2 = criar_post(titulo, conteudo)

    if post2 is not None:
        print(f'ID criado: {post2["id"]}')
    else:
        print("Não foi possível criar o post.")


elif opcao == 3:
    id_post = escolher_id()
    titulo = input("Informe o novo título do post: ")
    conteudo = input("Informe o novo conteúdo do post: ")

    post3 = atualizar_post(id_post, titulo, conteudo)

    if post3 is not None:
        print(f'Post atualizado: {post3["title"]}, {post3["body"]}')
    else:
        print("Não foi possível atualizar o post.")


elif opcao == 4:
    id_post = escolher_id()

    post4 = excluir_post(id_post)

    if post4:
        print("Post excluído com sucesso.")
    else:
        print("Não foi possível excluir o post.")


