DROP DATABASE libreria_cf;
CREATE DATABASE libreria_cf;


USE libreria_cf;

-- If we don't want a NULL values, we will add (NOT NULL) in the conditions, 
-- as we can see in the following code

-- And now if we want a unique value, is the same as NULL but in this case we will use UNIQUE
-- Wtih UNSIGNED we can use only positve numbers
-- When we need a primary key we will use 

CREATE TABLE autores( 
    autor_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
    nombre VARCHAR(25)  NOT NULL, 
    apellido VARCHAR(25)  NOT NULL, 
    seudonimo VARCHAR(50) UNIQUE,
    genero ENUM("M", "F"), 
    fecha_nacimiento DATE  NOT NULL, 
    pais_origen VARCHAR(40)  NOT NULL
);

INSERT INTO autores (nombre, apellido, genero, fecha_nacimiento, pais_origen)
VALUES  ("David", "Capera", "M", "2004-04-20", "Colombia" ),
        ("Juan", "Bocanegra", "M", "2014-08-16", "Mexico" ),
        ("Luisa", "Raigoza", "F", "2005-02-12", "Argentina" ),
        ("Aura", "Bocanegra", "F", "2003-08-30", "Polonia" );

INSERT INTO autores (nombre, apellido, seudonimo ,genero, fecha_nacimiento, pais_origen)
VALUES ("Stephen", "King", "Richard Bachman" ,"M", "2003-08-30", "USA" );


SELECT * FROM autores;