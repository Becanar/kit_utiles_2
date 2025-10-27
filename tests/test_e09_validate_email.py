import pytest
from src.strings import validate_email


@pytest.mark.parametrize(
    "email",
    [
        "user@example.com",
        "nombre.apellido@dominio-es.org",
        "u_1-2@dominio.net",
    ],
)
def test_validate_email_valid(email):
    assert validate_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "sin_arroba.com",     
        "user@dominio.",    
        "user@dominio.c",    
        "@dominio.com",      
        "user@.com",        
        "user@dominio.corporateemailtoolong", 
    ],
)
def test_validate_email_invalid(email):
    assert validate_email(email) is False
