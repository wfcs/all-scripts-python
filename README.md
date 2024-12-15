# all-scripts-python - Gerador de Dados e Ferramentas Automatizadas

Este repositório contém uma coleção de scripts desenvolvidos para diferentes finalidades, incluindo geração de dados fictícios, automação de pipelines de dados, instalação de softwares e organização de dados em notebooks interativos.

## Descrição dos Arquivos

### 1. GerarDadosFakes.py
Um script para gerar dados logísticos fictícios, como pedidos, datas de envio, distâncias, transportadoras, entre outros, e salvar o resultado em um arquivo CSV.

- **Funcionalidades**:
  - Geração de dados randomizados e reprodutíveis (usando `np.random.seed`).
  - Criação de um DataFrame com pandas contendo colunas como:
    - **ID Pedido**: Identificador único de cada pedido.
    - **Data de Envio e Entrega**: Datas aleatórias no intervalo configurado.
    - **Quantidade enviada e entregue**: Quantidades de produtos enviadas e efetivamente entregues, considerando possíveis perdas.
    - **Distância percorrida**: Em quilômetros, gerados aleatoriamente.
    - **Transportadora**: Nome fictício da transportadora responsável.
  - Exportação dos dados para um arquivo CSV chamado `Dados_Logistica_Ficticios.csv`.

---

### 2. Materiais_de_agricultura.ipynb
Este notebook interativo analisa materiais relacionados à agricultura. Ele combina análises estatísticas, visualizações e manipulações de dados para explorar informações relevantes (detalhes mais específicos podem ser adicionados após revisão do conteúdo completo).

- **Possíveis Funcionalidades**:
  - Leitura e limpeza de dados agrícolas.
  - Criação de gráficos para análise visual.
  - Modelos preditivos ou insights sobre tendências no setor agrícola.

---

### 3. NotebookPipelineFabric.py
Este script implementa uma pipeline de dados que conecta a um ambiente de SharePoint para leitura e transformação de arquivos Excel, e carrega os dados processados em um banco de dados.

- **Funcionalidades**:
  - **Autenticação no SharePoint**: Utilizando credenciais para acessar pastas específicas.
  - **Download de arquivos Excel**: Coleta de arquivos armazenados em uma pasta configurada.
  - **Transformações com pandas**: Exemplos incluem:
    - Criação de colunas derivadas de dados existentes.
    - Aplicação de fórmulas para enriquecer os dados.
  - **Carregamento em Banco de Dados**:
    - Conexão via ODBC para enviar os dados transformados para um Lakehouse ou Datamart.

---

### 4. ProgramasInstall.py
Um script em Python para instalação e atualização automatizada de softwares agrupados por categorias (jogos, trabalho ou ambos).

- **Funcionalidades**:
  - **Instalação de programas**:
    - Uso do gerenciador `winget` para instalar programas de forma automatizada.
    - Separação por categorias:
      - Apenas Jogos
      - Apenas Trabalho
      - Ambos
  - **Atualização de softwares**:
    - Atualiza todos os programas instalados com um único comando.
  - **Menu interativo**:
    - Interface baseada em texto para selecionar as opções desejadas.
    - Confirmação de ações usando `tkinter`.

---

## Requisitos

- Python 3.8 ou superior.
- Dependências especificadas nos scripts:
  - `pandas`: Manipulação e análise de dados.
  - `numpy`: Geração de dados aleatórios.
  - `pyodbc`: Conexão com bancos de dados.
  - `tkinter`: Interface gráfica para confirmações.
  - `datetime`: Manipulação de datas.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute os scripts conforme necessário:

   - Para gerar dados fictícios:
     ```bash
     python GerarDadosFakes.py
     ```
   - Para usar o instalador de programas:
     ```bash
     python ProgramasInstall.py
     ```
   - Para a pipeline de dados:
     ```bash
     python NotebookPipelineFabric.py
     ```

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

**Desenvolvido por:** Felipe Dovinho
