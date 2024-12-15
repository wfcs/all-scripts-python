from azure.identity import InteractiveBrowserCredential
from azure.storage.filedatalake import DataLakeServiceClient

# Definição de variáveis
DATA_LAKE_URL = " "
CONTAINER_NAME = " "

# Função para conectar ao DataLake
def connect_to_datalake():
    credential = InteractiveBrowserCredential()  # Prompt para login
    service_client = DataLakeServiceClient(account_url=DATA_LAKE_URL, credential=credential)
    print("Conexão bem-sucedida ao DataLake!")
    return service_client

# Conexão inicial
service_client = connect_to_datalake()
