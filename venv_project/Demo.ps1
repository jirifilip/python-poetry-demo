if (Test-Path ".venv") {
    Remove-Item -Recurse ".venv"
}

python -m venv .venv


