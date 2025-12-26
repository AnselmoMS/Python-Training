"""Service that fetches currency quotations.

This module provides a single helper `obter_cotacoes` that returns a
string representation of USD and EUR quotations in BRL. The function is
lightweight and returns a user-friendly error message on failure.
"""

import requests


def obter_cotacoes() -> str:
    """Fetch current USD and EUR quotations (in BRL) and return a formatted string.

    Returns a short string like "USD: R$ 5.00 | EUR: R$ 5.50" or an error message
    if the request or parsing fails.
    """
    try:
        # API gratuita que não exige chave (Economia Awesome API)
        url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
        response = requests.get(url)

        # O .json() já transforma a resposta em um dicionário
        dados = response.json()

        dolar = dados["USDBRL"]["bid"]
        euro = dados["EURBRL"]["bid"]

        return f"USD: R$ {float(dolar):.2f} | EUR: R$ {float(euro):.2f}"
    except Exception:
        return "Erro ao carregar cotações"


if __name__ == "__main__":
    print("Buscando valores...")
    print(obter_cotacoes())