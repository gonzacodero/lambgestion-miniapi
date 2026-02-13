![Swagger Docs](assets/docs.png)

# LambGestion Mini API

Mini API REST en Python con FastAPI (demo backend) para gestionar clientes.

## Features
- `GET /health` → estado del servicio
- `GET /clientes` → listar clientes
- `POST /clientes` → crear cliente
- Swagger/OpenAPI automático en `/docs`

## Requisitos
- Python 3.11+

## Instalación (Windows)

~~~powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
~~~

## Ejecutar

~~~powershell
python -m uvicorn app.main:app --reload
~~~

