CREATE TABLE proyectos (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nombre" TEXT NOT NULL,
    "descripcion" TEXT NOT NULL
);

CREATE TABLE "tablas" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "proyecto_id" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "checked" INTEGER NOT NULL DEFAULT (0),
    "quantity_master" INTEGER NOT NULL DEFAULT (0),
    "quantity_slave" INTEGER NOT NULL DEFAULT (0),
    "use_all" INTEGER NOT NULL DEFAULT (0),
    "condition" TEXT
);
CREATE TABLE conectores (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "proyecto_id" INTEGER NOT NULL,
    "tipo" INTEGER NOT NULL,
    "host" TEXT NOT NULL,
    "port" TEXT NOT NULL,
    "user" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "schema" TEXT NOT NULL
);
