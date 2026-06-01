import flet as ft
import requests


def main(page: ft.Page):
    page.title = "DigimonDex"

    lista = ft.Column()

    nome = ft.TextField(label="Nome do Digimon")
    nivel = ft.TextField(label="Nível")

    def carregar_digimons():
        lista.controls.clear()

        try:
            resposta = requests.get(
                "http://127.0.0.1:5000/digimons"
            )

            digimons = resposta.json()

            for digimon in digimons:
                lista.controls.append(
                    ft.Text(
                        f"{digimon['nome']} - {digimon['nivel']}"
                    )
                )

        except Exception as erro:
            lista.controls.append(
                ft.Text(f"Erro: {erro}")
            )

    def cadastrar(e):

        resposta = requests.post(
            "http://127.0.0.1:5000/digimons",
            json={
                "nome": nome.value,
                "nivel": nivel.value
            }
        )

        if resposta.status_code == 201:

            nome.value = ""
            nivel.value = ""

            carregar_digimons()

            page.snack_bar = ft.SnackBar(
                ft.Text("Digimon cadastrado com sucesso!")
            )

            page.snack_bar.open = True

            page.update()

    carregar_digimons()

    page.add(
        ft.Text(
            "DigimonDex",
            size=30,
            weight=ft.FontWeight.BOLD
        ),

        nome,
        nivel,

        ft.ElevatedButton(
            "Cadastrar Digimon",
            on_click=cadastrar
        ),

        ft.Divider(),

        lista
    )


ft.app(target=main)