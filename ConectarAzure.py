from azure.identity import InteractiveBrowserCredential
from azure.storage.filedatalake import DataLakeServiceClient
import time

# Definição de variáveis
DATA_LAKE_URL = "dataanalytics" 
CONTAINER_NAME = "dataanalytics" 

# Função para conectar ao DataLake
def connect_to_datalake():
    start_time = time.time()  # Início da medição do tempo
    credential = InteractiveBrowserCredential()  # Prompt para login
    service_client = DataLakeServiceClient(account_url=DATA_LAKE_URL, credential=credential)
    end_time = time.time()  # Fim da medição do tempo
    print(f"Conexão bem-sucedida ao DataLake! Tempo de execução: {end_time - start_time} segundos")
    return service_client

# Conexão inicial
service_client = connect_to_datalake()

from azure.identity import InteractiveBrowserCredential
from azure.storage.filedatalake import DataLakeServiceClient
import time

# Definição de variáveis
DATA_LAKE_URL = "https://<your-storage-account-name>.dfs.core.windows.net"  # Substitua pelo URL correto
CONTAINER_NAME = "dataanalytics" 

# Função para conectar ao DataLake
def connect_to_datalake():
    start_time = time.time()  # Início da medição do tempo
    credential = InteractiveBrowserCredential()  # Prompt para login
    service_client = DataLakeServiceClient(account_url=DATA_LAKE_URL, credential=credential)
    end_time = time.time()  # Fim da medição do tempo
    print(f"Conexão bem-sucedida ao DataLake! Tempo de execução: {end_time - start_time} segundos")
    return service_client

# Função para listar arquivos no contêiner
def list_files_in_container(service_client, container_name):
    file_system_client = service_client.get_file_system_client(file_system=container_name)
    paths = file_system_client.get_paths()
    print(f"Arquivos no contêiner '{container_name}':")
    for path in paths:
        print(path.name)

# Conexão inicial
service_client = connect_to_datalake()

# Listar arquivos no contêiner
list_files_in_container(service_client, CONTAINER_NAME)