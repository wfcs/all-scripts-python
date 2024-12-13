import os
import shutil
import tempfile
import ctypes
from pathlib import Path

# Função para deletar arquivos de uma pasta e calcular o espaço liberado
def delete_files_in_directory(directory):
    total_freed = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                size = os.path.getsize(file_path)
                os.remove(file_path)
                total_freed += size
            except PermissionError:
                continue
    return total_freed

# Função para limpar o cache do navegador (Chrome)
def clear_chrome_cache():
    chrome_cache_path = Path.home() / "AppData" / "Local" / "Google" / "Chrome" / "User Data" / "Default" / "Cache"
    if chrome_cache_path.exists():
        return delete_files_in_directory(chrome_cache_path)
    return 0

# Função para limpar o cache do navegador (Edge)
def clear_edge_cache():
    edge_cache_path = Path.home() / "AppData" / "Local" / "Microsoft" / "Edge" / "User Data" / "Default" / "Cache"
    if edge_cache_path.exists():
        return delete_files_in_directory(edge_cache_path)
    return 0

# Função para limpar arquivos temporários do sistema
def clear_temp_files():
    temp_dir = tempfile.gettempdir()
    return delete_files_in_directory(temp_dir)

# Função para exibir uma caixa de mensagem com o total de espaço liberado
def show_message(total_freed):
    total_mb = total_freed / (1024 * 1024)
    total_gb = total_mb / 1024
    message = f"Total de espaço liberado: {total_mb:.2f} MB ({total_gb:.2f} GB)"
    ctypes.windll.user32.MessageBoxW(0, message, "Limpeza Concluída", 1)

# Função principal para executar as limpezas e calcular o total liberado
def main():
    total_freed = 0
    total_freed += clear_temp_files()
    total_freed += clear_chrome_cache()
    total_freed += clear_edge_cache()
    show_message(total_freed)

# Execução do script
if __name__ == "__main__":
    main()
