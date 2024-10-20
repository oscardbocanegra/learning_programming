DROP DATABASE IF EXISTS libreria_cf;
CREATE DATABASE libreria_cf;

USE libreria_cf;

-- If we don't want NULL values, we will add (NOT NULL) in the conditions, 
-- as we can see in the following code

-- And now if we want a unique value, it is the same as NULL but in this case we will use UNIQUE
-- With UNSIGNED we can use only positive numbers
-- When we need a primary key we will use 

CREATE TABLE autores( 
    autor_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
    nombre VARCHAR(25) NOT NULL, 
    apellido VARCHAR(25) NOT NULL, 
    seudonimo VARCHAR(50) UNIQUE,
    genero ENUM('M', 'F'), 
    fecha_nacimiento DATE NOT NULL, 
    pais_origen VARCHAR(40) NOT NULL
);

--INSERT INTO autores (nombre, apellido, genero, fecha_nacimiento, pais_origen)
--VALUES  ('David', 'Capera', 'M', '2004-04-20', 'Colombia'),
--        ('Juan', 'Bocanegra', 'M', '2014-08-16', 'Mexico'),
--        ('Luisa', 'Raigoza', 'F', '2005-02-12', 'Argentina'),
--        ('Aura', 'Bocanegra', 'F', '2003-08-30', 'Polonia');

CREATE TABLE libros(
    libro_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    autor_id INT UNSIGNED NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    descripcion VARCHAR(250),
    paginas INT UNSIGNED,
    fecha_publicacion DATE NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id)
);



INSERT INTO autores (nombre, apellido, seudonimo, genero, fecha_nacimiento, pais_origen)
VALUES  ('Stephen', 'King', 'Richard Bachman', 'M', '2003-08-30', 'USA'),
        ('Mark', 'Mandon', 'MK', 'M', '1988-03-03', 'Mexico');

INSERT INTO libros (autor_id, titulo, fecha_publicacion)
VALUES  (1, 'Carrie', '1974-01-01'),
        (1, 'El misterio de Salems Lot', '1975-01-01'),
        (1, 'El resplandor', '1977-01-01'),
        (2, 'The subtle art of not giving a fuck', '2016-01-01'),
        (2, 'Will', '2021-01-01'),
        (2, 'Everything is fucked', '2024-01-01');

ALTER TABLE libros ADD ventas INT UNSIGNED NOT NULL;

SELECT * FROM autores;
SELECT * FROM libros;
