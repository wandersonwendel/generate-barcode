from src.views.http_types.http_response import HttpResponse

# Tratamento de erros
def handle_errors(error: Exception) -> HttpResponse:
    # Retornando as respostas de erros
    return HttpResponse(
        status_code = 500, # Erro genérico
        body = { # Dicionário com especificação do erro
            "errors": [{ # Lista erro
                "title": "Server Error", # Título do erro
                "detail": str(error) # Detalhe do erro (tranforma numa string)
            }]
        }
    )
