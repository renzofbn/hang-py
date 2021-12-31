# Hang-py 🐍

El juego del ahorcado en tu terminal !!!

![Preview Gif](https://raw.githubusercontent.com/Renzofbn/hang-py/main/preview.gif)

# Instalación:

## Requisitos
(click para ir a la página de descarga)

- [Python3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Descarga [Hang-py](https://github.com/Renzofbn/hang-py/archive/refs/heads/main.zip) y descomprímelo en tu carpeta de preferencia o puedes clonar el repositorio usando Git:

```
git clone https://github.com/Renzofbn/hang-py.git
```
## Windows

### Auto-Instalación

* Si es necesario descomprime la carpeta de [Hang-py](https://github.com/Renzofbn/hang-py/archive/refs/heads/main.zip), o puedes instalar el instalador [aquí](https://github.com/Renzofbn/hang-py/releases/download/hang_py_v0.35/Windows_Installer.bat). Luego ejecuta el ```Windows_Installer.bat``` . Este script creará (solo si no existe) la carpeta **Games** y copiará
el script ``` hangpy ``` en tu carpeta **System32** . Finalmente, cierra y abre tu terminal.

## Linux
Asumiendo que Bash es tu Shell predeterminada :
* Mueve la carpeta a tu directorio de preferencia y copia la ruta del archivo ``` main.py ```.
* Edita ``` ~/.bashrc ``` en tu editor preferido (puede que necesites permisos root), y Agrega una nueva línea con:
```
alias hangpy="cd RUTA_DEL_ARCHIVO_MAIN.PY && python main.py && cd ~"
```
* Donde RUTA_DEL_ARCHIVO_MAIN.PY es la ruta que copiaste en el paso 1 y finalmente cierra y abre tu terminal.

# Uso:
Para abrir el juego ejecuta el comando ``` hangpy ``` en tu terminal de preferencia.

## Licencia

Hangpy tiene la licencia MIT. [Lee la licencia para más información](https://github.com/Renzofbn/hang-py/blob/main/LICENSE).
