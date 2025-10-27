import pandas as pd
from paquete_proyecto.ejemplo import resumen_columna

def test_resumen_columna_ok():
    df = pd.DataFrame({"x": [1, 2, 3, 4]})
    r = resumen_columna(df, "x")
    assert round(r.media, 3) == 2.5
    assert round(r.desvio, 3) == 1.291  # std muestral con ddof=1

def test_resumen_columna_missing():
    df = pd.DataFrame({"x": [1, None, 3, 4]})
    r = resumen_columna(df, "x")
    assert r.media > 0 and r.desvio > 0

def test_resumen_columna_inexistente():
    df = pd.DataFrame({"x": [1, 2, 3]})
    try:
        resumen_columna(df, "y")
        assert False, "Debió lanzar ValueError"
    except ValueError:
        assert True