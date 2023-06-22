import api
import re
import requests
import time


class Yolanda:

    def __init__(self, host, port):
        self.base = f"http://{host}:{port}"
        self.regex_validador_fechas = '\d{1,2}\sde\s[a-zA-Z]+\sde\s(19\d{2}|20\d{2}|\d{2})' # TODO: Completar
        self.regex_extractor_signo = ''  # TODO: Completar

    def saludar(self) -> dict:
        # TODO: Completar
        respuesta = requests.get(f"{self.base}/")
        return {"status-code": respuesta.status_code, "saludo": respuesta.json()["result"]}


    def verificar_horoscopo(self, signo: str) -> bool:
        # TODO: Completar
        endpoint = "/signos"
        respuesta = requests.get(self.base + endpoint)
        return signo in respuesta.json()["result"]
        return "Completar"

    def dar_horoscopo(self, signo: str) -> dict:
        # TODO: Completar
        parametros = {"signo": signo}
        endpoint = "/horoscopo"
        respusta = requests.get(self.base + endpoint, params=parametros)
        return {"status-code": respusta.status_code, "mensaje": respusta.json()["result"]}

    def dar_horoscopo_aleatorio(self) -> dict:
        # TODO: Completar
        endpoint = "/aleatorio"
        respuesta = requests.get(self.base + endpoint)
        if respuesta.status_code != 200:
            return {"status-code": respuesta.status_code, "mensaje": respuesta.json()["result"]}
        else:
            enlace = respuesta.json()["result"]
            respuesta_nueva = requests.get(enlace)
            return {"status-code": respuesta_nueva.status_code, "mensaje": respuesta_nueva.json()["result"]}

    def agregar_horoscopo(self, signo: str, mensaje: str, access_token: str) -> str:
        # TODO: Completar
        my_header = {"authorization": access_token}
        endpoint = "/update"
        respuesta = requests.post(self.base + endpoint, headers=my_header, data = {"signo": signo, "mensaje": mensaje})
        if respuesta.status_code == 401:
            return "Agregar horoscopo no autorizado"
        elif respuesta.status_code == 400:
            return respuesta.json()["result"]
        else:
            return "La base de YolandaAPI ha sido actualizada"


    def actualizar_horoscopo(self, signo: str, mensaje: str, access_token: str) -> str:
        # TODO: Completar
        endpoint = "/update"
        my_header = {"authorization": access_token}
        respuesta = requests.put(self.base + endpoint, headers=my_header, data = {"signo": signo, "mensaje": mensaje})
        if respuesta.status_code == 401:
            return "Editar horoscopo no autorizado"
        elif respuesta.status_code == 400:
            return respuesta.json()["result"]
        else:
            return "La base de YolandaAPI ha sido actualizada"


    def eliminar_signo(self, signo: str, access_token: str) -> str:
        # TODO: Completar
        endpoint = "/remove"
        my_header = {"authorization": access_token}
        respuesta = requests.delete(self.base + endpoint, headers=my_header, data = {"signo": signo})
        if respuesta.status_code == 401:
            return "Eliminar signo no autorizado"
        elif respuesta.status_code == 400:
            return respuesta.json()["result"]
        else:
            return "La base de YolandaAPI ha sido actualizada"


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 4444
    DATABASE = {
        "acuario": "Hoy será un hermoso día",
        "leo": "No salgas de casa.... te lo recomiendo",
    }
    thread = api.Server(HOST, PORT, DATABASE)
    thread.start()

    yolanda = Yolanda(HOST, PORT)
    print(yolanda.saludar())
    print(yolanda.dar_horoscopo_aleatorio())
    print(yolanda.verificar_horoscopo("acuario"))
    print(yolanda.verificar_horoscopo("pokemon"))
    print(yolanda.dar_horoscopo("acuario"))
    print(yolanda.dar_horoscopo("pokemon"))
    print(yolanda.agregar_horoscopo("a", "aaaaa", "pepaiic2233"))
    print(yolanda.dar_horoscopo("a"))
