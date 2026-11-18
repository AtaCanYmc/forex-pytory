import re
import pytest
from unittest.mock import patch
import sys
from forex_pytory import __version__
from forex_pytory.cli.main import main


def test_package_version():
    assert isinstance(__version__, str)
    assert re.match(r"^\d+\.\d+\.\d+", __version__)


def test_cli_help(capsys):
    with pytest.raises(SystemExit) as exc:
        with patch.object(sys, "argv", ["forex-scraper", "--help"]):
            main()
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "--source" in captured.out
    assert "--date" in captured.out
    assert "--format" in captured.out


def test_cli_invalid_date(capsys):
    with pytest.raises(SystemExit) as exc:
        with patch.object(sys, "argv", ["forex-scraper", "--date", "invalid-date"]):
            main()
    assert exc.value.code == 1
    captured = capsys.readouterr()
    assert "Invalid date format" in captured.out
