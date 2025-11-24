import mercadopago

#def gerar_link_pagamento():
sdk = mercadopago.SDK("")

request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '1'
}

payment_data = {
        "items": [
            {"id": "1", "title": "Camisa", "quantity": 1, "currency_id": "BRL", "unit_price": 259.99}
        ],
        "back_urls": {
            "success": "http://127.0.0.1:5000/compracerta",
            "failure": "http://127.0.0.1:5000/compraerrada",
            "pending": "http://127.0.0.1:5000/compraerrada",
        },
        "auto_return": "all"
}
result = sdk.preference().create(payment_data, request_options)
payment = result["response"]

print(payment)

    #link_iniciar_pagamento = payment["init_point"]
    #return link_iniciar_pagamento