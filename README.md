# Hang-py 🐍

El juego del ahorcado en tu terminal !!!

![Preview Gif](https://raw.githubusercontent.com/Renzofbn/hang-py/main/preview.gif)

# Instalación:

## Requisitos

- [Python3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Descarga [Hang-py](https://github.com/Renzofbn/hang-py/archive/refs/heads/main.zip) y descomprímelo en tu carpeta de preferencia.
O también puedes abrir una terminal en tu carpeta de preferencia y clonar el repositorio :

```
git clone https://github.com/Renzofbn/hang-py.git
```
## Windows

### Auto-Instalación

* Si es necesario descomprime la carpeta, luego ejecuta el ``` Windows_Installer ``` . Este script creará (solo si no existe) la carpeta **Games** y copiará
el script ``` hangpy ``` en tu carpeta **System32** . Finalmente, cierra y abre tu terminal.
* Para abrir el juego ejecuta el comando ``` hangpy ``` en tu terminal de preferencia.

## Linux
Asumiendo que Bash es tu Shell predeterminada :
* Mueve la carpeta a tu directorio de preferencia y copia la ruta del archivo ``` main.py ```.
* Edita ``` ~/.bashrc ``` en tu editor preferido (puede que necesites permisos root), y Agrega una nueva línea con:
```
alias hangpy="cd RUTA_DEL_ARCHIVO_MAIN.PY && python main.py && cd ~"
```
* Donde RUTA_DEL_ARCHIVO_MAIN.PY es la ruta que copiaste en el paso 1 y finalmente cierra y abre tu terminal.
* Para abrir el juego ejecuta el comando ``` hangpy ``` en tu terminal de preferencia.

## Licencia

Hangpy tiene la licencia MIT. [Lee la licencia para más información](https://github.com/Renzofbn/hang-py/blob/main/LICENSE).
