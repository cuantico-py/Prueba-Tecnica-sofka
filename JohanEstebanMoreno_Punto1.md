##1. Defina en sus palabras   ¿que es la calidad de software.?

Es la forma de presentar código limpio, se presenta como la recopilación de buenas prácticas en el desarrollo de software y los atributos deseables de estos, esta calidad implica una estructura organizativa, un control de defectos y características de calidad como fiabilidad, operabilidad, seguridad, , mantenibilidad entro otros 



##2. Explique la diferencia entre un sistema de control de versiones centralizado y un sistema de control de versiones distribuido.

Los sistemas de control de versiones centralizados se basan en la idea de tener una única copia 
"central" de su proyecto en algún lugar (probablemente en un servidor local), y los desarroladores  "confirmarán" sus
 cambios
 se diferencia del sistema distribuido por : 
- Los sistemas centralizados suelen ser más fáciles de entender y usar
- Puede otorgar control de nivel de acceso a nivel de directorio

![a](https://user-images.githubusercontent.com/64481383/92192293-43fed500-ee2b-11ea-8ea4-cc0585d1a6f2.png)
####(Imagen tomada de la web)
 
 

En el control de versiones distribuidas, cada desarrollador "clona" una copia de un repositorio y tiene 
el historial completo del proyecto en su propio disco duro. Esta copia o ("clon") tiene todos los 
metadatos del original
caracteristicas que lo diferencian 
- El rendimiento de los sistemas distribuidos es mejor
- Ramificar y fusionar es mucho más fácil
- Con un sistema distribuido, no es necesario estar conectado a la red todo el tiempo (el repositorio de código completo se almacena localmente en la PC)

![b](https://user-images.githubusercontent.com/64481383/92192503-bc659600-ee2b-11ea-822d-e51a70539980.png)
####(Imagen tomada de la web)



##3. ¿Cuál es el comando utilizado en git para clonar un proyecto?

Puedes clonar un repositorio con:  
### "git clone [url]" 

##4. ¿Qué realizan los siguientes comandos de git?

##a. git add -miClase

Agrega un cambio en el directorio de trabajo al área de preparación(stagin area). 
Le dice a Git que desea incluir actualizaciones de versiones  para el  archivo ("-miClase) en
la próxima confirmación.

##b. git add -A 

Si no se proporciona <una rura especifica> cuando se usa la opción (-A), se actualizan todos los archivos de todo
 el árbol de trabajo 

##c. git status
Me muestra las rutas que tienen diferencias entre el archivo de índice y el "local Repo", 
las rutas que tienen diferencias entre el árbol de trabajo y el archivo de índice y las rutas en el árbol de trabajo que no son rastreadas por Git
 (y no son ignoradas por gitignore

##d. git pull
se usa para actualizar el  repositorio local al commit más nuevo, para bajar y fusionar los cambios remotos.

##e. git push
Se usa para subir o enviar los cambios del repositorios local al repositorio remoto

##f. git commit -m “Hola”
se usa para crear (commit) como una version en el repositorio local el "-m" indica que tiene un mensaje ( es una descripcion del cambio que se hizo)
y pone un "Hola" 

##g. git log
es para obtener el commit id

##5. Describa en desarrollo de software que es la herencia y que es el polimorfismo 

Herencia:
es una forma de reutilización de código, donde se puede "heredar" 
las características y comportamientos de una clase superior . de una clase base, su código puede ser reutilizado por las
 clases derivadas.
 
 Polimorfismo
 sta característica es posible definir varios métodos o comportamientos de un
  objeto bajo un mismo nombre, de forma tal que es posible modificar los parámetros del método, 
  o reescribir su funcionamiento, 
 o incrementar más funcionalidades a un método.


