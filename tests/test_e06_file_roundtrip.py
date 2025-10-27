from src.files import save_lines, load_lines

def test_save_and_load_roundtrip(tmp_path):

    path = tmp_path / "archivo.txt"
    lines = ["uno", "dos", "tres"]

    save_lines(path, lines)
    resultado = load_lines(path)

    assert resultado == lines


def test_load_empty_file(tmp_path):
   
    path = tmp_path / "vacio.txt"
    path.write_text("", encoding="utf-8")  # crea un archivo vacío

    resultado = load_lines(path)

    assert resultado == []
