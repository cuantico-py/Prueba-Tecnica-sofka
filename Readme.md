#Prueba Técnica – Training Calidad 


Preguntas a resolver: 
 --
 Conceptos Generales
1. Defina en sus palabras   ¿que es la calidad de software.?

Es la forma de presentar código limpio, se presenta como la recopilación de buenas prácticas en el desarrollo de software y los atributos deseables de estos, esta calidad implica una estructura organizativa, un control de defectos y características de calidad como Fiabilidad, Operabilidad, Seguridad, , Mantenibilidad entro otros 


2. Explique la diferencia entre un sistema de control de versiones centralizado y
un sistema de control de versiones distribuido.


Los sistemas de control de versiones centralizados se basan en la idea de que hay una única copia "central" de su proyecto en algún lugar (probablemente en un servidor), y los programadores "confirmarán" sus cambios en esta copia central.
Los sistemas centralizados suelen ser más fáciles de entender y usar
Puede otorgar control de nivel de acceso a nivel de directorio
 ![Alt text] (https://github.com/cuantico-py/Prueba-Tecnica-sofka/tree/master/imagenes/a.png)
![Screenshot](a.png)

En el control de versiones distribuidas, cada desarrollador "clona" una copia de un repositorio y tiene el historial completo del proyecto en su propio disco duro. Esta copia (o "clon") tiene todos los metadatos del original
El rendimiento de los sistemas distribuidos es mejor
Ramificar y fusionar es mucho más fácil
Con un sistema distribuido, no es necesario estar conectado a la red todo el tiempo (el repositorio de código completo se almacena localmente en la PC)


3. ¿Cuál es el comando utilizado en git para clonar un proyecto?

4. ¿Qué realizan los siguientes comandos de git?

a. git add -miClase

 
b. git add -A
c. git status
d. git pull
e. git push
f. git commit -m “Hola”
g. git log
5. Describa en desarrollo de software que es la herencia y que es el polimorfismo 


 Algoritmos y Lógica de Programación
Construya los siguientes algoritmos en su lenguaje de programación preferido y
envíelos de acuerdo a las instrucciones dadas en el correo de la prueba, puede
utilizar Bases de Datos, Frontend, Backend, lo que queremos es que nos muestres
que sabes y el talento que tienes.

1. Determine el valor de un pasaje en avión, conociendo la distancia a recorrer, el número de
días de estancia, y sabiendo que, si la distancia a recorrer es superior a 1000 Km y el
número de días de estancia es superior a 7, la línea aérea le hace un descuento del 30%.
(el precio por km. es de $35.00) 


2. Un BOING 747 tiene una capacidad de carga para equipaje de aproximadamente 18.000
kg. Confeccione un algoritmo que controle la recepción de equipajes para este avión,
sabiendo que:
 • Un bulto no puede exceder la capacidad de carga del avión ni tampoco exceder los 500
Kg.
• El valor por kilo del bulto es:
 - de 0 a 25 Kg. cero pesos
 - de 26 a 300 Kg. 1500 pesos por kilo de equipaje.
 - de 301 a 500 Kg. 2500 pesos por kilo de equipaje
Para un vuelo cualquiera se pide:
a) Número total de bultos ingresados para el vuelo
b) Peso del bulto más pesado y del más liviano
c) Peso promedio de los bultos
d) Ingreso en pesos y en dólares por concepto de carga. Construya una tabla de
seguimiento con no menos de 15 bultos para 
