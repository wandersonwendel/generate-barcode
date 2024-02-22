from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController

# Cria uma espécie de espelho/fantasma do Barcode
@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_value = "image_path"

    # Retorna um valor fictício pra não ficar gerando sempre as imagens, durante o teste
    mock_create_barcode.return_value = mock_value

    tag_creator_controller = TagCreatorController()

    # Cria a tag com o nome atribuido em mock_value
    result = tag_creator_controller.create(mock_value)

    # Verificando se os campos são esses
    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    # Verificando se os valores dos campos batem
    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{mock_value}.png'
