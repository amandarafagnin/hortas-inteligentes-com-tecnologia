# Projeto: Hortas Inteligentes
# Disciplina: Atividades Extensionistas II - UNINTER

import random
from datetime import datetime

def verificar_irrigacao(umidade):
    if umidade < 40:
        return "Irrigação necessária"
    else:
        return "Umidade adequada"

# Simulação de leitura de sensor
umidade_solo = random.randint(20, 80)

print("=" * 40)
print("SISTEMA DE MONITORAMENTO DA HORTA")
print("=" * 40)
print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Umidade do Solo: {umidade_solo}%")
print(f"Status: {verificar_irrigacao(umidade_solo)}")
print("=" * 40)
