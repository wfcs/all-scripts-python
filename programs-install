import os
import subprocess
from tkinter import messagebox

# Dicionário com os programas disponíveis para instalação agrupados por categoria
programas_por_categoria = {
    "1": [
        "7zip",
        "Discord",
        "Valve.Steam",
        "Ubisoft.Connect",
        "GOG.Galaxy",
        "qBittorrent",
        "EpicGames.EpicGamesLauncher",
        "Amazon.Games",
        "ElectronicArts.EADesktop",
        "Spotify.Spotify",
        "Apple.iTunes",
        "Deezer.Deezer",
        "Bethesda.Launcher",
    ],
    "2": [
        "Figma",
        "Flow-Launcher",
        "InternetDownloadManager",
        "Microsoft.Teams",
        "Microsoft.WindowsTerminal",
        "Mozilla.Firefox",
        "Obsidian.Obsidian",
        "qBittorrent.qBittorrent",
        "Microsoft.PowerToys",
        "Telegram.TelegramDesktop",
        "DaxStudio.DaxStudio",
        "Microsoft.OneDrive",
        "Microsoft.PowerBI",
        "Spotify.Spotify",
        "Apple.iTunes",
        "Deezer.Deezer",
    ],
}

# Função para exibir o menu de opções
def exibir_menu_opcoes():
    print("‎ ‎ ‎ ‎ ‎                                                           ")
    print("‎ ‎ ‎ ‎ ‎* ============ MENU DE OPÇÕES | OPTIONS MENU ==============")
    print("‎ ‎ ‎ ‎ ‎*                                                         *")
    print("‎ ‎ ‎ ‎ ‎* Selecione uma opção ( select an option ) :              *")
    print("‎ ‎ ‎ ‎ ‎*                                                         *")
    print("‎ ‎ ‎ ‎ ‎* 1. Apenas jogos - Only Games                            *")
    print("‎ ‎ ‎ ‎ ‎* 2. Apenas trabalho - Only Work                          *")
    print("‎ ‎ ‎ ‎ ‎* 3. Trabalho e Jogos - Work and Games                    *")
    print("‎ ‎ ‎ ‎ ‎* 4. Atualizar programas - Update all programs            *")
    print("‎ ‎ ‎ ‎ ‎* 5. Sair - Exit                                          *")
    print("‎ ‎ ‎ ‎ ‎*                                                         *")
    print("‎ ‎ ‎ ‎ ‎*         Desemvolvido por @felipedovinho                 *")
    print("‎ ‎ ‎ ‎ ‎*                                                         *")
    print("‎ ‎ ‎ ‎ ‎* =========================================================")
    print("‎ ‎ ‎ ‎ ‎                                                           ")
    print("‎ ‎ ‎ ‎ ‎                                                           ")


# Função para instalar os programas selecionados
def instalar_programas(programas):
    for programa in programas:
        os.system(f"winget install {programa} -h --accept-package-agreements")


# Função para atualizar todos os programas
def atualizar_programas():
    subprocess.run(["winget", "update", "-h", "--all"])


# Função principal
def main():
    while True:
        # Limpar a tela do console
        os.system("cls" if os.name == "nt" else "clear")

        # Exibir menu de opções
        exibir_menu_opcoes()
        opcao = input("Opção selecionada: ")

        if opcao == "1":
            # Only Games
            programas_selecionados = programas_por_categoria["1"]
            instalar_programas(programas_selecionados)
        elif opcao == "2":
            # Only Work
            programas_selecionados = programas_por_categoria["2"]
            instalar_programas(programas_selecionados)
        elif opcao == "3":
            # Work and Games
            programas_selecionados = (
                programas_por_categoria["1"] + programas_por_categoria["2"]
            )
            instalar_programas(programas_selecionados)
        elif opcao == "4":
            # Update all programs
            atualizar_programas()
        elif opcao == "5":
            # Exit
            confirmar_saida = messagebox.askquestion(
                "Confirmação", "Deseja realmente sair?"
            )
            if confirmar_saida == "yes":
                break
        else:
            messagebox.askquestion(
                "Opção inválida", "Por favor, selecione uma opção válida."
            )


if __name__ == "__main__":
    main()
