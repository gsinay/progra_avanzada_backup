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

    #mybtessecuencia
    m_bytes = mensaje[4: 4 + largo]
    m_bytes_secuencia.extend(m_bytes)

    #secuencia codificada
    largo_secuencia = largo  * 2
    bytes = mensaje[-largo_secuencia:]
    secuencia_codificada.extend(bytes)

    #mreducido es lo que sobra
    reducido = mensaje[4 + largo: -2 * largo]
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
    listas_separadas = separar_msg_encriptado(mensaje)
    secuencia = decodificar_secuencia(listas_separadas[2])
    bytes_secuencia = listas_separadas[0]
    m_reducido = listas_separadas[1]
    bytes_retorno = bytearray()
    for elemento_range in range(len(m_reducido)):
        bytes_retorno.extend(m_reducido[elemento_range: elemento_range + 1])
    
    for indice in secuencia:
        elemento_a_append = bytes_secuencia[0]
        bytes_secuencia = bytes_secuencia[1:]
        bytes_retorno.insert(indice, elemento_a_append)
    
    return bytes_retorno



if __name__ == "__main__":
    #mensaje = bytearray(b'\x00\x00\x00\x04"a}a{tm": 1\x00\x01\x00\x05\x00\n\x00\x03')
    #desencriptado = desencriptar(mensaje)
    #diccionario = deserializar_diccionario(desencriptado)
    #print(diccionario)

    print(desencriptar(
            bytearray(b'\x00\x00\x00\x02\x02\x03\x02\x01\x05\x00\x02\x00\x03')))