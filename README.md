# Challenge-Python-L1


Servidor HTTP simple sin uso de frameworks(flask ,django, etc)

Este servidor responde a solicitudes tipo GET de acuerdo a las especificaciones solo tenemos un endpoint el cual a su vez consume una API REST externa para
la extraccion  y clasifcacion de datos asociados a paises , de acuerdo a esto para poder ejecutar el proyecto debemos hacer lo siguiente



# INSTALACION [LINUX]

clonar el proyecto en su repositorio local y desplazarse hasta ese directorio , posteriormente crear un entorno virtual para instalar las dependencias 

> python3 -m venv venv

luego debera activar el entorno virtual anteriormente creado

> . venv/bin/activate  o bien usando el comando   source venv/bin/activate


una vez activado el entorno virtual debera instalar las dependencias por lo que en la raiz del proyecto ejecutar el siguiente comando

> pip install -r requirements.txt o bien  el comando   pip3 install -r requirements.txt


una vez instaladas las dependencias correr el script main.py  

> python main.py   o bien el comando python3.py

una vez ejecutado podra ir al url  http://127.0.0.1:8000/      y obtendra la respuesta en formato JSON de acuerdo a las especificaciones


al hacer la solicitud de tipo GET en este endpoint , en su directorio local se generara un archivo data.json que tendra la informacion vista desde el navegador
pero en un archivo JSON

si desea tambien puede realizar la solicitud GET desde la linea de comandos 
> curl http://127.0.0.1:8000/

# FUNCIONAMIENTO
![alt text](https://github.com/sebas1017/Challenge-Python-L1/blob/main/APIREST.PNG?raw=true)
