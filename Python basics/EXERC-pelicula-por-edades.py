'''
Película por edades

A partir de las siguientes especificaciones, crea la lógica para recomendar una película dependiendo de la edad dada por el usuario.
<table> 
<thead> 
<tr> 
<th>Rango de edad</th> 
<th>Película</th> 
</tr> </thead> 
<tbody> 
<tr> <td><= 16</td> <td>"Coco"*</td> </tr> 
<tr> <td>17 −− 25</td> <td>"Avengers: Endgame"</td> </tr> 
<tr> <td>26 −− 40</td> <td>"Matrix"</td> </tr> 
<tr> <td>41 −− 60</td> <td>"El libro verde"</td> </tr> 
<tr> <td>> 60</td> <td>"Un golpe con estilo"</td> </tr> 
</tbody> 
</table> 
'''

peliculas = {
    ( 0,  16) : 'Coco',
    (17,  25) : 'Avengers: Endgame',
    (26,  40) : 'Matrix',
    (41,  60) : 'El libro verde',
    (61, float("inf")) : 'Un golpe con estilo',
}

edad = int(input('Edad? >> '))
for edades, peli in peliculas.items():

     if edad >=edades[0] and edad <=edades[1]:
        #  print(f'Edad: {edad}\nPelicula: {peli}')
        print(f'::RECOMENDADOR POR EDADES::\nPelícula para tu edad ({edad}): "{peli}"\nEdades comprendidas entre {edades[0]} y {edades[1]} años')
        break