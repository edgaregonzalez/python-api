# Clase 46 - Intro DevSecOps

Crear el entorno virtual.
```bash
python3 -m venv env
```
Activar el entorno.
```bash
source env/bin/activate
```
Instalar todas las dependencias
```bash
pip install -r requirements.txt
```
Freeze dependencies

```bash
pip freeze > requirements.txt
```

## Instalar y configurar pre-commit

```bash
pip install pre-commit
```

```bash
pip freeze > requirements.txt
```

```bash
touch .pre-commit-config.yaml
```

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.4.0  # Use the latest version
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-docstring-first

  - repo: https://github.com/psf/black
    rev: 21.5b2  # Use the latest version
    hooks:
      - id: black
        language_version: python3.8  # Ensure you specify your Python version

  - repo: https://github.com/PyCQA/flake8
    rev: 3.9.2  # Use the latest version
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.8.0  # Use the latest version
    hooks:
      - id: isort

```

```bash
pre-commit install
```
```bash
pre-commit run --all-files
```

## Instalar git-secret

## macOS

```bash
brew install git-secret
brew install gnupg

```

## Linux

```bash
sudo apt-get install git-secret
sudo apt-get install gnupg

```

## Windows

```bash
choco install git-secret
sudo apt-get install gnupg
```
## Generar un gpg key

```bash
gpg --full-generate-key
```

```bash
gpg --list-secret-keys --keyid-format LONG
```


## Configurar git-secret

```bash
git secret init
```

```bash
git secret tell [dirección de correo electrónico del usuario]
```

```bash
git secret add [archivo1] [archivo2] ...
```

```bash
git secret hide
```
```bash
git add *.secret
git commit -m "Add secrets"
git push origin main
```
