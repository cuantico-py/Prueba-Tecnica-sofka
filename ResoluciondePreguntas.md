1. Defina en sus palabras   ¿que es la calidad de software.?

Es la forma de presentar código limpio, se presenta como la recopilación de buenas prácticas en el desarrollo de software y los atributos deseables de estos, esta calidad implica una estructura organizativa, un control de defectos y características de calidad como Fiabilidad, Operabilidad, Seguridad, , Mantenibilidad entro otros 



2. Explique la diferencia entre un sistema de control de versiones centralizado y
un sistema de control de versiones distribuido.

Los sistemas de control de versiones centralizados se basan en la idea de que hay una única copia "central" de su proyecto en algún lugar (probablemente en un servidor), y los programadores "confirmarán" sus cambios en esta copia central.
- Los sistemas centralizados suelen ser más fáciles de entender y usar
- Puede otorgar control de nivel de acceso a nivel de directorio

![a](https://user-images.githubusercontent.com/64481383/92192293-43fed500-ee2b-11ea-8ea4-cc0585d1a6f2.png)

 
 

En el control de versiones distribuidas, cada desarrollador "clona" una copia de un repositorio y tiene el historial completo del proyecto en su propio disco duro. Esta copia (o "clon") tiene todos los metadatos del original
- El rendimiento de los sistemas distribuidos es mejor
- Ramificar y fusionar es mucho más fácil
- Con un sistema distribuido, no es necesario estar conectado a la red todo el tiempo (el repositorio de código completo se almacena localmente en la PC)

![b](https://user-images.githubusercontent.com/64481383/92192503-bc659600-ee2b-11ea-822d-e51a70539980.png)




3. ¿Cuál es el comando utilizado en git para clonar un proyecto?

Puedes clonar un repositorio con:  
###git clone [url]. 

4. ¿Qué realizan los siguientes comandos de git?

a. git add -miClase

  Agrega un cambio en el directorio de trabajo al área de preparación(stagin area). 
  Le dice a Git que desea incluir actualizaciones para el  archivo ("-miClase) en
 la próxima confirmación. Sin embargo, git add no afecta realmente 
 al repositorio de manera significativa; 

b. git add -A 
Si quieres saltarte el área de preparación, Git te ofrece un atajo sencillo. Añadiendo la opción -a al comando git commit harás que Git prepare automáticamente todos los archivos rastreados antes de confirmarlos, ahorrándote el paso de git add:
c. git status
d. git pull
e. git push
f. git commit -m “Hola”
g. git log
5. Describa en desarrollo de software que es la herencia y que es el polimorfismo 


