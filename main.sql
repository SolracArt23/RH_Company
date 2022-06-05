--Funcion de tablas
CREATE TABLE public."Tabla3" (
   id SERIAL PRIMARY KEY,
   nombre   character varying(255),
   pk   bigint   NOT NULL,
   fecha   date   NOT NULL,
   comprobante   boolean
)

CREATE TABLE public."Tabla1" (
   id2 SERIAL PRIMARY KEY,
   nombre   character varying(255),
   pk   bigint   NOT NULL,
   fecha   date   NOT NULL
)
CREATE TABLE public."Tabla2" (
   id2 SERIAL PRIMARY KEY,
   nombre   character varying(255),
   pf   bigint   NOT NULL,
   comprobante   boolean
)
--Funcion de guardado
CREATE FUNCTION Agregar_tbls() returns Trigger
as
$$
    BEGIN
    INSERT INTO "Tabla2"(nombre,pf,comprobante) VALUES(NEW.nombre,NEW.pk,New.comprobante);
    INSERT INTO "Tabla1"(nombre,pk,fecha) VALUES(NEW.nombre,NEW.pk,NEW.fecha);
    return new;
    END
$$
language plpgsql;

CREATE FUNCTION actualizar_tbl() returns Trigger
as
$$
    BEGIN
   
    Update FROM "Tabla2"(nombre,pf,comprobante) VALUES(NEW.nombre,NEW.pf,New.comprobante) WHERE id2=(SELECT id FROM "Tabla3");
    Update FROM "Tabla1"(nombre,pk,fecha):= (NEW.nombre,NEW.pk,NEW.fecha) WHERE id2=(SELECT id FROM "Tabla3");
    return new;
    END
$$
language plpgsql;

--Funcion de Delete
CREATE FUNCTION ELiminar_tbl() returns Trigger
as
$$
    BEGIN
    DELETE FROM "Tabla2" WHERE  id2 = (SELECT id FROM "Tabla3") 
    DELETE FROM "Tabla1" WHERE  id2 = (SELECT id FROM "Tabla3") 
    END
$$
language plpgsql;




--Trigger de carga
CREATE trigger insertar AFTER INSERT ON "Tabla3"
FOR EACH ROW

execute procedure Agregar_tbl();

--Trigger de Update
CREATE trigger actualizar ertar AFTER DELETE ON "Tabla3"
FOR EACH ROW

execute procedure ELiminar_tbl();