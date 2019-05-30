# Modulo para el manejo de fechas en español para Python

El módulo en este repositorio está diseñado para el manejo de fechas en python, con un mínimo de funcionalidades para su uso facil y rapido. Este modulo esta en idioma español y la manera de usarlo, es la siguiente

Para descargar, basta con clonar este repositorio en la carpeta de tu proyecto, no incluye dependencias fuera del python, así

```
➜  git clone https://github.com/JQLaverde/ISCFinal.git
```

Para importar el proyecto y poder usarlo en python. Para instanciar un objeto de la clase Fecha, se debe pasar una tupla con los valores de (año, mes, dia) o con los valores de (año, mes, dia, hora, minutos, segundos), en caso de no pasar hora, minutos y segundos, estos se asumen como ceros por defecto

```python
import fechas

fecha = fechas.Fecha((2019, 5, 22))

print(fecha)
```
```
(2019, 5, 22, 0, 0, 0)
```

### Funcionalidad suma y resta de cantidades de tiempo

Si tienes una fecha y deseas restar ya sean años, meses, días, horas, minutos o segundos, basta con simplemente declarar tu objeto fecha y llamar al método sumar o restar de alguno de los ítems anteriormente mencionados, estos métodos retornar otro objeto de la clase Fecha con la suma o resta realizada, ejemplo: Si deseamos sumar o restar años

```python
import fechas

fecha = fechas.Fecha((2019, 5, 22))

fechaSumaAnos = fecha.sumarAnos(5)
fechaRestaAnos = fecha.restarAnos(10)

print(fechaSumaAnos)
print(fechaRestaAnos)

```
```
(2024, 5, 22, 0, 0, 0)
(2009, 5, 22, 0, 0, 0)
```
### Funcionalidad distancia en dias entre dos fechas

Esta funcionalidad te permite saber cuantos días transcurrieron entre una fecha y otra, retorna un entero con este dato

```python
import fechas

fechaInicial = fechas.Fecha((1998, 8, 16))
fechaFinal = fechas.Fecha((2019, 5, 29))

distanciaEnDias = fechaInicial.calcularDistanciaEnDias(fechaFinal)

print(distanciaEnDias)

```
```
7590
```

### Funcionalidad restar fechas

Es posible con este módulo, restar dos fechas, simplemente con el símbolo '-', lo cual retorna un objeto de la clase Fecha con la información de los años, meses, días, horas, minutos y segundos que separan a esas dos fechas

```python
import fechas

fechaInicial = fechas.Fecha((1998, 8, 16))
fechaFinal = fechas.Fecha((2019, 5, 29))

restaFechas = fechaFinal - fechaInicial

print(restaFechas)

```
```
(20, 9, 13, 0, 0, 0)
```

### Funcionalidad instanciar objeto Hoy

Con este paquete, se puede instanciar un objeto llamado Hoy que tiene los mismos métodos y atributos que los objetos de la clase Fecha, solo que para este, no es necesario pasarle los atributos, ya que al instanciarlo, estos se cargan con los datos de la fecha y hora actual

```python
import fechas

ahora = fechas.Hoy()

print(ahora)

```
```
(2019, 5, 30, 8, 53, 39)
```


