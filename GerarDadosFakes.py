import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurações
np.random.seed(42)  # Para reprodutibilidade
num_rows = 5000  # Número de linhas
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)

# Gerar IDs únicos
order_ids = range(1, num_rows + 1)

# Gerar datas de envio e entrega
dates_sent = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(num_rows)]
dates_delivered = [date + timedelta(days=np.random.randint(1, 15)) for date in dates_sent]

# Quantidade enviada e entregue
quantities_sent = np.random.randint(10, 200, size=num_rows)
quantities_delivered = [sent - np.random.randint(0, 10) if np.random.rand() > 0.1 else sent for sent in quantities_sent]

# Distância (em km)
distances = np.random.randint(50, 1500, size=num_rows)

# Transportadora (fictícia)
carriers = np.random.choice(['Transportadora A', 'Transportadora B', 'Transportadora C'], size=num_rows)

# Criar DataFrame
data = pd.DataFrame({
    'ID Pedido': order_ids,
    'Data de Envio': dates_sent,
    'Data de Entrega': dates_delivered,
    'Quantidade Enviada': quantities_sent,
    'Quantidade Entregue': quantities_delivered,
    'Distância (km)': distances,
    'Transportadora': carriers
})

# Salvar em arquivo CSV
file_path = '/mnt/data/Dados_Logistica_Ficticios.csv'
data.to_csv(file_path, index=False, sep=';')

file_path
