import streamlit as st
import pandas as pd
from io import BytesIO

# Função para processar as planilhas
def processar_planilhas(arquivo1, arquivo2, arquivo_produtos):
    try:
        # Leitura das planilhas
        planilha1 = pd.read_excel(arquivo1)
        planilha2 = pd.read_excel(arquivo2)
        planilha_produtos = pd.read_excel(arquivo_produtos)

        # Verificar se as colunas necessárias estão presentes
        colunas_necessarias = ['CODID', 'ESTOQUE', 'SKU', 'Unidades que ocupan espacio en Full']
        for coluna in colunas_necessarias:
            if coluna not in planilha1.columns or coluna not in planilha2.columns or coluna not in planilha_produtos.columns:
                raise ValueError(f"A coluna {coluna} está faltando em uma das planilhas.")

        # Merge entre a planilha de produtos e a planilha1 (que contém o estoque)
        planilha_com_codid = pd.merge(planilha_produtos[['CÓD. INTERNO', 'CODID']], planilha1, on='CÓD. INTERNO', how='left')

        # Merge entre a planilha com o CODID e a planilha2 (que contém o estoque)
        dados_relacionados = pd.merge(planilha_com_codid, planilha2[['CODID', 'ESTOQUE']], on='CODID', how='left')

        # Calcular o estoque final
        dados_relacionados['Estoque Final'] = dados_relacionados['ESTOQUE'] + dados_relacionados['Unidades que ocupan espacio en Full']

        # Retornar a tabela final com SKU e o estoque final
        resultado = dados_relacionados[['SKU', 'Estoque Final']]
        return resultado

    except Exception as e:
        st.error(f"Erro ao processar as planilhas: {e}")
        return None

# Função para permitir que o usuário envie os arquivos e exiba os resultados
def main():
    # Título da aplicação
    st.title("Cálculo de Estoque Final por SKU")

    # Exibição para upload das planilhas
    st.sidebar.header("Carregar Planilhas")
    arquivo1 = st.sidebar.file_uploader("Selecione a Planilha 1 (estoque full)", type=["xlsx"])
    arquivo2 = st.sidebar.file_uploader("Selecione a Planilha 2 (estoque com código interno)", type=["xlsx"])
    arquivo_produtos = st.sidebar.file_uploader("Selecione a Planilha de Produtos (contém CÓD. INTERNO e CODID)", type=["xlsx"])

    # Verificar se os arquivos foram carregados
    if arquivo1 is not None and arquivo2 is not None and arquivo_produtos is not None:
        st.write("Planilhas carregadas com sucesso!")
        
        # Processar as planilhas e exibir a tabela com o resultado
        resultado = processar_planilhas(arquivo1, arquivo2, arquivo_produtos)

        if resultado is not None:
            # Exibir a tabela com o estoque final
            st.write("Estoque Final por SKU")
            st.dataframe(resultado)

            # Gerar o arquivo Excel em memória para o download
            with BytesIO() as excel_buffer:
                with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                    resultado.to_excel(writer, index=False, sheet_name='Estoque Final')

                # Buscar o conteúdo do arquivo gerado em BytesIO e disponibilizar para download
                excel_data = excel_buffer.getvalue()

            st.download_button(label="Baixar Resultado", data=excel_data, file_name="estoque_final.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.write("Erro ao processar as planilhas. Verifique os arquivos e tente novamente.")
    else:
        st.write("Por favor, faça o upload das três planilhas para calcular o estoque final.")

if __name__ == "__main__":
    main()