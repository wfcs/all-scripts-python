from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, when, current_date, datediff, lit, time, date_format
)

# Configurações do SQL Data Lake e Lakehouse
SQL_SERVER = "NomeDoServidor"
SQL_DATABASE = "dataanalytics_sql_pool"
SQL_USER = "usuario"
SQL_PASSWORD = "senha"
LAKEHOUSE_PATH = "caminho_para_o_lakehouse"

# Criar a sessão Spark
spark = SparkSession.builder \
    .appName("DataLakeToLakehouse") \
    .getOrCreate()

# Função para carregar dados do SQL Data Lake
def load_data_from_sql():
    """Carrega os dados do SQL Data Lake usando PySpark."""
    try:
        jdbc_url = f"jdbc:sqlserver://{SQL_SERVER};databaseName={SQL_DATABASE}"
        properties = {
            "user": SQL_USER,
            "password": SQL_PASSWORD,
            "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
        }
        query = """
        (SELECT
            DataHoraCriacao,
            OrdemServico,
            Equipamento,
            DataConclusao,
            DescricaoEquipamento,
            Departamento,
            StatusDescricao,
            TipoOs,
            DataInformeParada,
            DataInicioProgramada,
            DataHoraUltimaAlteracao
        FROM HxGN_ordem_servico
        WHERE DataInicioProgramada >= '2024-01-01') AS subquery
        """
        df = spark.read.jdbc(url=jdbc_url, table=query, properties=properties)
        print("Dados carregados com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao carregar dados do SQL Data Lake: {e}")
        return None

# Função para realizar transformações nos dados
def transform_data(df):
    """Aplica as transformações conforme o script M."""
    try:
        # Calcular DeltaProgramado
        df = df.withColumn(
            "DeltaProgramado",
            when(
                (col("StatusDescricao") != "FECHADA") & 
                (col("StatusDescricao") != "CANCELADA"),
                datediff(current_date(), col("DataInicioProgramada"))
            ).otherwise(None)
        )
        
        # Criar coluna TipoDataNovo
        df = df.withColumn(
            "TipoDataNovo",
            when(
                (col("DeltaProgramado") > 0) & 
                (col("StatusDescricao") != "FECHADA") & 
                (col("StatusDescricao") != "CANCELADA"),
                lit("Atrasada")
            ).otherwise(lit("No Prazo"))
        )
        
        # Criar coluna StatusOSAtual
        df = df.withColumn(
            "StatusOSAtual",
            when(col("DeltaProgramado").isNull(), lit("Sem Inicio Programado"))
            .otherwise(lit("Atrasada"))
        )
        
        # Filtrar dados
        df = df.filter(~col("TipoOs").isin("*", "MEC", "OSOP"))
        
        # Substituir valores em TipoOs
        df = df.withColumn(
            "TipoOs",
            when(col("TipoOs") == "BRKD", lit("MCE")).otherwise(col("TipoOs"))
        )
        
        # Adicionar colunas HoraCriacao e HoraConclusao
        df = df.withColumn("HoraCriacao", date_format(col("DataHoraCriacao"), "HH:mm:ss")) \
               .withColumn("HoraConclusao", date_format(col("DataConclusao"), "HH:mm:ss"))
        
        # Extrair apenas as datas de DataHoraCriacao, DataConclusao e DataInicioProgramada
        df = df.withColumn("DataHoraCriacao", col("DataHoraCriacao").cast("date")) \
               .withColumn("DataConclusao", col("DataConclusao").cast("date")) \
               .withColumn("DataInicioProgramada", col("DataInicioProgramada").cast("date"))
        
        print("Transformações aplicadas com sucesso.")
        return df
    except Exception as e:
        print(f"Erro durante as transformações: {e}")
        return None

# Função para salvar no Lakehouse
def save_to_lakehouse(df, path):
    """Salva os dados transformados no formato Parquet no Lakehouse."""
    try:
        df.write.mode("overwrite").parquet(path)
        print(f"Dados salvos no Lakehouse em: {path}")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

# Processo principal
def main():
    # Carregar dados do SQL Data Lake
    df = load_data_from_sql()
    if df is None:
        return
    
    # Aplicar transformações
    transformed_df = transform_data(df)
    if transformed_df is None:
        return
    
    # Salvar os dados no Lakehouse
    save_to_lakehouse(transformed_df, f"{LAKEHOUSE_PATH}/ordem_servico_transformed.parquet")

if __name__ == "__main__":
    main()
