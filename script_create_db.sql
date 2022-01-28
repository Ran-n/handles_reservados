CREATE IF NOT EXISTS TABLE "xenero" (
    "id_xenero" TEXT UNIQUE NOT NULL,
    "nome"      TEXT UNIQUE,
    CONSTRAINT xeneroPK PRIMARY KEY ("id_xenero")
);

CREATE IF NOT EXISTS TABLE "entidade" (
    "id_entidade"       TEXT UNIQUE NOT NULL,
    "nome"              TEXT NOT NULL,
    "data_nacemento"    INTEGER,
    "data_falecemento"  INTEGER,
    "id_xenero"         TEXT,
    "fotografia"        TEXT,
    CONSTRAINT entidadePK PRIMARY KEY ("id_entidade"),
    CONSTRAINT entidadeFK1 FOREIGN KEY ("id_xenero") REFERENCES "xenero"("id_xenero") ON DELETE CASCADE ON UPDATE CASCADE MATCH [FULL]
);

CREATE IF NOT EXISTS TABLE "alias" (
    "id_alias"  INTEGER NOT NULL UNIQUE,
    "valor_alias"   TEXT UNIQUE,
    "id_entidade"   TEXT,
    CONSTRAINT "aliasFK1" FOREIGN KEY("id_entidade") REFERENCES "entidade"("id_entidade") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
    CONSTRAINT "aliasPK" PRIMARY KEY("id_alias")
);

CREATE IF NOT EXISTS TABLE "estado" (
    "id_estado"     TEXT UNIQUE NOT NULL,
    "nome_estado"   TEXT UNIQUE NOT NULL,
    CONSTRAINT estadoPK PRIMARY KEY ("id_estado")
);

CREATE IF NOT EXISTS TABLE "lingua" (
    "id_lingua"     TEXT UNIQUE NOT NULL,
    "nome_lingua"   TEXT UNIQUE NOT NULL,
    CONSTRAINT linguaPK PRIMARY KEY ("id_lingua")
);

CREATE IF NOT EXISTS TABLE "area" (
    "id_area"           TEXT UNIQUE NOT NULL,
    "nome_area"         TEXT UNIQUE NOT NULL,
    "descricion"        TEXT,
    CONSTRAINT areaPK PRIMARY KEY ("id_area")
);

CREATE IF NOT EXISTS TABLE "entidade_area" (
    "id_entidade"   TEXT NOT NULL,
    "id_area"       TEXT NOT NULL,
    "data_inicio"   INTEGER,
    "data_fin"      INTEGER,
    CONSTRAINT entidade_areaPK PRIMARY KEY ("id_area", "id_entidade"),
    CONSTRAINT entidade_areaFK1 FOREIGN KEY ("id_area") REFERENCES "area"("id_area") ON DELETE CASCADE ON UPDATE CASCADE MATCH [FULL],
    CONSTRAINT entidade_areaFK2 FOREIGN KEY ("id_entidade") REFERENCES "entidade"("id_entidade") ON DELETE CASCADE ON UPDATE CASCADE MATCH [FULL]
);

CREATE IF NOT EXISTS TABLE "entidade_estado" (
    "id_entidade"   TEXT NOT NULL,
    "id_estado"     TEXT NOT NULL,
    "data_inicio"   INTEGER,
    "data_fin"      INTEGER,
    CONSTRAINT entidade_estadoPK PRIMARY KEY ("id_entidade", "id_estado"),
    CONSTRAINT entidade_estadoFK1 FOREIGN KEY ("id_entidade") REFERENCES "entidade"("id_entidade") ON DELETE CASCADE ON UPDATE CASCADE MATCH [FULL],
    CONSTRAINT entidade_estadoFK2 FOREIGN KEY ("id_estado") REFERENCES "estado"("id_estado") ON DELETE CASCADE ON UPDATE CASCADE MATCH [FULL]
);

CREATE IF NOT EXISTS TABLE "entidade_lingua" (
    "id_entidade"   TEXT NOT NULL,
    "id_lingua"     TEXT NOT NULL,
    "data_inicio"   INTEGER,
    CONSTRAINT entidade_linguaPK PRIMARY KEY ("id_entidade", "id_lingua"),
    CONSTRAINT entidade_estadoFK1 FOREIGN KEY ("id_entidade") REFERENCES "entidade"("id_entidade") ON DELETE CASCADE ON UPDATE CASCADE MATCH [FULL],
    CONSTRAINT entidade_estadoFK2 FOREIGN KEY ("id_lingua") REFERENCES "lingua"("id_lingua") ON DELETE CASCADE ON UPDATE CASCADE MATCH [FULL]
);
