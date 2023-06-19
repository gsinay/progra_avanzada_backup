
import pickle

def encriptar(msg: bytearray, N: int) -> bytearray:
   
    desplazamiento = N % len(msg) #por si el desplazamiento es mas grande al mensaje
    mensaje_movido = msg[-desplazamiento:] + msg[:-desplazamiento]
    mensaje_movido[0], mensaje_movido[N] = mensaje_movido[N], mensaje_movido[0]
    return mensaje_movido

def desencriptar(msg: bytearray, N: int) -> bytearray:
    desplazamiento = N % len(msg) #por si el desplazamiento es mas grande al mensaje
    msg[0], msg[N] = msg[N], msg[0]
    mensaje_movido = msg[desplazamiento:] + msg[:desplazamiento]
    return mensaje_movido

def codificar(msg: bytearray) -> bytearray:
    largo = len(msg)
    mensaje_codificado = largo.to_bytes(4, byteorder="little")

    #calcular cantidad de chunks
    largo_chunk = 128
    cantidad_chunks = (largo + largo_chunk -1 ) // largo_chunk

    #codificar cada chunk
    for i in range(cantidad_chunks):
        inicio_de_chunck = i * largo_chunk
        fin_de_chunck = min(inicio_de_chunck + largo_chunk, largo)

        # armar el chunck y llenarlo de 0s con ljust si es necesario
        chunk = msg[inicio_de_chunck : fin_de_chunck]
        chunk = chunk.ljust(largo_chunk, b'\x00')

        # agregar el id del chunck en big endian al chunck codificado
        chunk_id = i.to_bytes(4, 'big')
        mensaje_codificado += chunk_id + chunk
    return mensaje_codificado

def decodificar(msg: bytearray) -> bytearray:
    largo = int.from_bytes(msg[:4], byteorder="little")
    mensage_codificado= msg[4:]

    #dividir mensaje en chuncks de 128 bytes + 4 de identificacion
    largo_chunk = 128
    cuenta_chunck = len(msg) // (largo_chunk + 4)
    mensaje_decoficado = bytearray()

    #decodificar cada chunk
    for i in range(cuenta_chunck):
        inicio_de_chunck = (i * (largo_chunk + 4)) + 4
        fin_de_chunck = inicio_de_chunck + largo_chunk

        # obtener el chunck y remover los 0 adicionales si es que hay
        chunk = mensage_codificado[inicio_de_chunck:fin_de_chunck]
        chunk = chunk.rstrip(b'\x00')

        # añadir el chunck al mensaje
        mensaje_decoficado += chunk

    return mensaje_decoficado


def encriptar_y_codificar(msg, N: int) -> bytearray:
    #serializamos el mensaje
    bytes = pickle.dumps(msg)
    bytes_en_array = bytearray(bytes)
    msg_encriptado = encriptar(bytes_en_array, N)
    msg_codificado = codificar(msg_encriptado)
    return bytearray(msg_codificado)

def decodificar_y_desencriptar(msg: bytearray, N: int) -> bytearray:
    msg_desencriptado = decodificar(msg)
    msg_desencriptado = desencriptar(msg_desencriptado, N)
    #deserializamos el mensaje en chunks
    msg_desencriptado = pickle.loads(msg_desencriptado)
    return msg_desencriptado




if __name__ == "__main__":
    # Testear encriptar
    N = 1
    msg_original = bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04\x05')
    msg_esperado = bytearray(b'\x01\x05\x02\x03\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04')
    msg_encriptado = encriptar(msg_original, N)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")
    
    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado, N)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")