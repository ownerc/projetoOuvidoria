use sistema_ouvidoria;

create table Ouvidoria (
    codigo int auto_increment,
    manifestacao varchar(500) NOT NULL,
    tipo varchar(20) NOT NULL,
    PRIMARY KEY(codigo)
);

DELETE FROM OUVIDORIA WHERE CODIGO = 1;
ALTER TABLE Ouvidoria AUTO_INCREMENT = 0;