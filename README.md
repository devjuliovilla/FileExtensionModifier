# File extension modifier
---

Un script simple hecho en python para modificar la extensión de múltiples archivos.

## Ejecución

```bash
python file-extension-modifier.py
```

## Crear ejecutable

1. Instalar pyinstaller
```bash
pip install pyinstaller
```

2. Crear el archivo ejecutable.
```bash
pyinstaller --onefile file-extension-modifier.py
```

**NOTA**

Si el comando anterior **NO** funciona, intentar con el siguiente:
```bash
py -3.11 -m PyInstaller --onefile file-extension-modifier.py
```