import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, ARRAY, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import desc


Base = declarative_base()

class Reporte(Base):
    __tablename__ = 'reporte'
    folio = Column(String, ForeignKey('deteccion.idBox'), primary_key=True)
    fechaHora = Column(DateTime, nullable=False)
    idCamarafk = Column(String, ForeignKey('camara.idCamara'))
    masculino = Column(Boolean)
    adulto = Column(Boolean)
    lentes = Column(Boolean)
    gorra = Column(Boolean)
    mochila = Column(Boolean)

    
class Camara(Base):
    __tablename__ = 'camara'
    idCamara = Column(String, primary_key=True)
    descripcion = Column(String)
    idSucursalfk = Column(Integer, ForeignKey('sucursal.idSucursal'))
  
class Sucursal(Base):
    __tablename__ = 'sucursal'
    idSucursal = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    calle = Column(String(250), nullable=False)
    num = Column(String(250), nullable=False)
    alcaldia_municipio = Column(String(250), nullable=False)
    estado = Column(String(250), nullable=False)
    cp = Column(String(250), nullable=False)
    numCamaras = Column(Integer, nullable=False)

class Deteccion(Base):
    __tablename__ = 'deteccion'
    idBox = Column(String, primary_key=True) #autoincremento solo para Integer type
    fechaHora = Column(DateTime, nullable=False)
    idCamarafk = Column(String, ForeignKey('camara.idCamara'))
    clase = Column(Float)
    box = Column(ARRAY(Integer))
    confidence = Column(Float)
    idBucket = Column(String)

engine = create_engine('postgresql+psycopg2://ESOSWEYES:ESOSWEYES@{0}:5432/vigilancia'.format('postgres'))
#engine = create_engine('sqlite:///base_test.db')
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

def agregarSucursal(nombre, calle, num, alcaldia_municipio, estado, cp, numCamaras):
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    sucursal = Sucursal(nombre=nombre, calle=calle, num=num, alcaldia_municipio=alcaldia_municipio, estado=estado, cp=cp, numCamaras=numCamaras)
    session.add(sucursal)
    session.commit()
    session.close()
    return "La sucursal fue agregada con exito"

def agregarCamara(idCamara, descripcion, idSucursalfk):
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    camara = Camara(idCamara=idCamara, descripcion=descripcion, idSucursalfk=idSucursalfk)
    session.add(camara)
    session.commit()
    session.close()
    return "La camara fue agregada con exito"

