from cerberus import Validator

# dados a serem validados
body = {
    "data": {
        "elemento1": 123.98,
        "elemento2": "olaMundo"
    }
}

# Definindo um esquema que descreve a estrutura e as restrições dos dados que deseja validar
body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "required": True, "empty": False },
            "elemento2": { "type": "string", "required": True, "empty": True },
            "elemento3": { "type": "string", "required": False, "empty": False },
        }
    }
})

# Schema validando o body
response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print('Body Ok')
