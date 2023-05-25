from typing import List
import json
from errors import JsonError, SequenceError


def serializar_diccionario(dictionary: dict) -> bytearray:
    # Completar
    try: 
        string = json.dumps(dictionary)
        return bytearray(string, 'utf-8')
    except TypeError:
        raise JsonError



def verificar_secuencia(mensaje: bytearray, secuencia: List[int]) -> None:
    # Completar
    largo = len(mensaje)
    for i in secuencia:
        if i > largo:
            raise SequenceError
    for i in range(len(secuencia)):
        for j in range(len(secuencia)):
            if i != j:
                if secuencia[i] == secuencia[j]:
                    raise SequenceError
    return None


def codificar_secuencia(secuencia: List[int]) -> bytearray:
    if len(secuencia) == 0:
        return bytearray()
    #secuencia.sort()
    bytearray_retorno = bytearray()
    for elemento in secuencia:
        elemento_bytes = elemento.to_bytes(2, byteorder='big')
        bytearray_retorno.extend(elemento_bytes)
    print(bytearray_retorno)
    return bytearray_retorno


def codificar_largo(largo: int) -> bytearray:
    # Completar
    bytearray_retorno = bytearray()
    elemento_bytes = largo.to_bytes(4, byteorder="big")
    bytearray_retorno.extend(elemento_bytes)
    return bytearray_retorno


def separar_msg(mensaje: bytearray, secuencia: List[int]) -> List[bytearray]:
    m_bytes_secuencia = bytearray()
    m_reducido = bytearray()
    # Completar

    return [m_bytes_secuencia, m_reducido]


def encriptar(mensaje: dict, secuencia: List[int]) -> bytearray:
    verificar_secuencia(mensaje, secuencia)

    m_bytes_secuencia, m_reducido = separar_msg(mensaje, secuencia)
    secuencia_codificada = codificar_secuencia(secuencia)

    return (
        codificar_largo(len(secuencia))
        + m_bytes_secuencia
        + m_reducido
        + secuencia_codificada
    )


if __name__ == "__main__":
    original = serializar_diccionario({"tama": 1})
    print(original)
    verificar_secuencia(original, [1, 2, 3])
    codificar_secuencia([1, 2, 3])
    #encriptado = encriptar(original, [1, 5, 10, 3])
    #print(original)
    #print(encriptado)
