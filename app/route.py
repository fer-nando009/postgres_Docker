from app import app
from flask import Flask, request
from vigilanciaDB import *
import json


@app.route("/")
def accepted():
    return "Servicio en linea"

@app.route("/add_suc", methods = ['POST'])
def add_suc():
    data = json.loads(request.data)
    sucursal = agregarSucursal(data["nombre"], data["calle"], data["num"], data["alcaldia_municipio"], data["estado"], data["cp"], data["numCamaras"])
    return sucursal

@app.route("/add_cam", methods = ['POST'])
def add_cam():
    data = json.loads(request.data)
    camara = agregarCamara(data["idCamara"], data["descripcion"], data["idSucursalfk"])
    return camara
