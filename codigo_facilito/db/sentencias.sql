DROP  DATABASE libreria_cf;
CREATE DATABASE libreria_cf;


USE libreria_cf;

CREATE TABLE autores( 
    autor_id INT, 
    nombre VARCHAR(25), 
    apellido VARCHAR(25), 
    genero CHAR(1), 
    fecha_nacimiento DATE, 
    pais_origen VARCHAR(40)
);

INSERT INTO autores (autor_id, nombre, apellido, genero, fecha_nacimiento, pais_origen)
VALUES  (1, "David", "Capera", "M", "2004-04-20", "Colombia" ),
        (2, "Juan", "Bocanegra", "M", "2014-08-16", "Mexico" ),
        (3, "Luisa", "Raigoza", "F", "2005-02-12", "Argentina" ),
        (4, "Aura", "Bocanegra", "M", "2003-08-30", "Polonia" );


SELECT * FROM autores;