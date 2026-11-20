# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias, en este caso las librerías requests y tabulate

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**



## Antes de ejecutar los scripts

- **Credenciales del controlador:** los scripts usan el usuario `cisco` y la clave `cisco123!`. Si en tu Network Controller creaste otro usuario, cambialos en `01_get-ticket.py` y en `04_tabulate.py`.
- **Ticket (X-Auth-Token):** `02_get-network-device.py` y `03_get-host.py` traen escrito un ticket de ejemplo que **no va a funcionar** en tu Packet Tracer, porque el controlador genera uno nuevo en cada sesión y vence. Ejecutá primero `01_get-ticket.py`, copiá el ticket que muestra y reemplazalo en el header `X-Auth-Token` de esos dos scripts. `04_tabulate.py` no necesita este paso: pide el ticket solo.

##¿Que hace cada script?
Scripts del proyecto (TP N° 4)
Todos los scripts interactúan con la Northbound API del Network Controller de Cisco Packet Tracer (http://localhost:58000/api/v1):

src/01_get-ticket.py (cátedra): Envía una petición POST a /api/v1/ticket con las credenciales del controlador para obtener el serviceTicket necesario para autenticar el resto de las consultas.
src/02_get-network-device.py (cátedra): Realiza un GET a /api/v1/network-device enviando el ticket en el header X-Auth-Token y muestra en consola el hostname, platformId e IP de gestión de cada dispositivo descubierto. (Nota: al llegar al router ISP, que por consigna está en estado Wrong credential, lanza KeyError: 'hostname' porque el controlador no pudo obtener su hostname por SSH).
src/03_get-host.py (cátedra): Realiza un GET a /api/v1/host con el X-Auth-Token y lista en consola los hosts detectados por el controlador junto con su IP, MAC e interfaz de conexión.
src/04_tabulate.py (cátedra): Obtiene el ticket automáticamente y consulta /api/v1/network-device y /api/v1/host para mostrar la información formateada en tablas mediante la librería tabulate.
src/05_export_csv.py (script propio): Se autentica automáticamente contra /api/v1/ticket, consulta todos los dispositivos de red (/api/v1/network-device) y hosts (/api/v1/host) manejando de forma segura los campos opcionales con .get() (incluyendo equipos en Wrong credential), y exporta el inventario completo al archivo inventario_red.csv.