import subprocess
import sys


def run_cli(*args):
    return subprocess.run(
        [sys.executable, '-m', 'toolkit', *args],
        capture_output=True, text=True, check=False,

    )


def test_calc_cli():
    result = run_cli('calc', '2+2')
    assert result.returncode == 0
    assert result.stdout.strip() == '4.0'

def test_convert_cli():
    result = run_cli('convert', '5', '--from', 'km', '--to', 'm')
    assert result.returncode == 0
    assert result.stdout.strip() == '5000.0'