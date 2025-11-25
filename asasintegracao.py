import requests
import webbrowser  # importa o módulo para abrir o navegador

def gerar_link_pagamento():
    url = "https://api-sandbox.asaas.com/v3/paymentLinks"

    payload = {
    "billingType": "CREDIT_CARD",
    "chargeType": "INSTALLMENT",
    "name": "sabrina",
    "value": 100,
    "maxInstallmentCount": 2
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "access_token": "$aact_hmlg_000MzkwODA2MWY2OGM3MWRlMDU2NWM3MzJlNzZmNGZhZGY6OjRhODg1OWFiLTY5NjgtNGZkMy04YWVjLTUwZWZkZTUyMmRmNzo6JGFhY2hfYzg5MzhlNzYtNGZjMy00NzdhLWFiNjMtNjVlMDhhOGU2Zjlh"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Converte para dicionário
    data = response.json()
    print(data)

    # Extrai a URL
    payment_url = data.get("url")

    if payment_url:
        print("URL obtida:", payment_url)
        webbrowser.open_new_tab(payment_url)  # Abre em nova guia
    else:
        print("Campo 'url' não encontrado na resposta.")


# Chamada da função
gerar_link_pagamento()
