from typing import List
import json
from errors import JsonError, SequenceError


def deserializar_diccionario(mensaje_codificado: bytearray) -> dict:
    try:
        string = mensaje_codificado.decode('utf-8')
        return json.loads(string)
    except json.JSONDecodeError:
        raise JsonError


def decodificar_largo(mensaje: bytearray) -> int:
    bytes_decodificar = mensaje[0:4]
    numero = int.from_bytes(bytes_decodificar, byteorder='big')
    return numero


def separar_msg_encriptado(mensaje: bytearray) -> List[bytearray]:
    m_bytes_secuencia = bytearray()
    m_reducido = bytearray()
    secuencia_codificada = bytearray()
    # Completar
    largo = decodificar_largo(mensaje)
    print(largo)
    #mybtessecuencia
    m_bytes = mensaje[4: 4 + largo]
    m_bytes_secuencia.extend(m_bytes)

    #secuencia codificada
    largo_secuencia = largo * 2
    bytes = mensaje[-largo_secuencia:]
    secuencia_codificada.extend(bytes)

    #mreducido es lo que sobra
    reducido = mensaje[4 + largo: largo - largo_secuencia]
    m_reducido.extend(reducido)



    return [m_bytes_secuencia, m_reducido, secuencia_codificada]


def decodificar_secuencia(secuencia_codificada: bytearray) -> List[int]:
    # Completar
    chunk = 2 #largo del chunk
    secuencia = [] #secuencia decodificada
    for i in range(0, len(secuencia_codificada), chunk):
        secuencia.append(int.from_bytes(secuencia_codificada[i:i + chunk], byteorder='big'))
    return secuencia
    


def desencriptar(mensaje: bytearray) -> bytearray:
    # Completar
    pass


if __name__ == "__main__":
    #mensaje = bytearray(b'\x00\x00\x00\x04"a}a{tm": 1\x00\x01\x00\x05\x00\n\x00\x03')
    #desencriptado = desencriptar(mensaje)
    #diccionario = deserializar_diccionario(desencriptado)
    #print(diccionario)

    print(separar_msg_encriptado(
            bytearray(b'\x00\x00\x00\x02\x01\x03\x00\x02\x05\x00\x01\x00\x03')))
