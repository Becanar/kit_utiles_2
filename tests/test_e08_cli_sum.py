from src.cli import main


def test_main_with_numbers(capsys):
    
    argv = ["prog", "1,2,3"]

    main(argv)
    salida = capsys.readouterr().out.strip()

    assert salida == "6.0"


def test_main_without_args(capsys):

    argv = ["prog"]

    main(argv)
    salida = capsys.readouterr().out.strip()

    assert salida == "0"
