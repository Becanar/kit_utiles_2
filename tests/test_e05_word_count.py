import pytest
from src.strings import word_count


@pytest.fixture
def texto():
    """Fixture que devuelve un texto de ejemplo."""
    return "Hola, hola... ¿Qué tal? Tal vez bien: hola!"


def test_word_count(texto):
  
    resultado = word_count(texto)

    assert resultado["hola"] == 3
    assert resultado["tal"] == 2
    assert resultado["qué"] == 1
    assert "inexistente" not in resultado
