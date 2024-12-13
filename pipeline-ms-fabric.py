from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext

# Autenticação com e-mail e senha
url = "https://3yssb5.sharepoint.com/sites/BasedeDados/"
username = "felipesilva@fluxbi.com.br"
password = "Felipe*1993"

context = AuthenticationContext(url)
if context.acquire_token_for_user(username, password):
    ctx = ClientContext(url, context)
    # Agora você pode interagir com o SharePoint
else:
    print("Falha na autenticação")
    

import pandas as pd
from io import BytesIO


# Definir o caminho da pasta
library_name = "Documentos Compartilhados"
folder_url = f"{library_name}/ArquivosFelipeNuvem/AAA/Transporte de Madeira"

# Listar os arquivos da pasta
files = ctx.web.get_folder_by_server_relative_url(folder_url).files.get().execute_query()

 # Iterar sobre os arquivos .xlsx
for file in files:
    if file.name.endswith('.xlsx'):
        file_url = file.properties["ServerRelativeUrl"]
        response = ctx.web.get_file_by_server_relative_url(file_url).download()
        bytes_file = BytesIO(response.content)

        # Ler e transformar os dados com pandas
        df = pd.read_excel(bytes_file)
        # Transformações, exemplo:
        df['Nova_Coluna'] = df['Coluna_Existente'] * 2
        print(df.head())


import pyodbc

# Conectar ao Lakehouse ou Datamart (configure a string de conexão)
conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=<seu_servidor>;DATABASE=<seu_db>;UID=<seu_user>;PWD=<sua_senha>")

# Carregar dados
df.to_sql('nome_da_tabela', con=conn, if_exists='replace', index=False)
conn.close()
