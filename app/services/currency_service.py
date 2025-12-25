import requests

def obter_cotacoes():
    try:
        # API gratuita que não exige chave (Economia Awesome API)
        url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
        response = requests.get(url)
        
        # O .json() já transforma a resposta em um dicionário (tipo um TJSONObject)
        dados = response.json()
        
        dolar = dados['USDBRL']['bid']
        euro = dados['EURBRL']['bid']
        
        return f"USD: R$ {float(dolar):.2f} | EUR: R$ {float(euro):.2f}"
    except Exception as e:
        return "Erro ao carregar cotações"

# Teste rápido
if __name__ == "__main__":
    print("Buscando valores...")
    print(obter_cotacoes())