import socket
import sys

server_address = "127.0.0.1"
port = 40000

def main():
    sock = try_connection()
    connected = True
    listen()

    menu()

def try_connection() -> socket:
    #tenta conectar a porta
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_address, port))
        return sock
    except (ConnectionRefusedError,TimeoutError):
        print("couldnt connect to server")
        sys.exit(1)

def listen():
    #escuta o servidor
    global sock
    global connected
    while connected:
        try:    
            data = sock.recv(4096)
            if not data:
                #encerra a escuta se o servidor interrompe a conexao
                not connected
                break

            packet = data.decode('utf-8', errors='replace').strip()
            #necessario decidirmos o que fazer com os pacotes recebidos

        except:
            #essa execao acontece quando o socket do client fecha
            not connected
            break

def menu():
    while connected:
        print("\n\nEscolha a opcao:\n")
        print("[1] enviar uma mensagem ao servidor\n")
        print("[2] requisitar uma operacao do servidor\n")
        print("[0] sair\n")

        op = input()
        match op:
            case "1":
                #o usuario insere o conteudo
                content = input()
                #o client cria um pacote com as informacoes relevantes e o conteudo inserido pelo usuario e o envia ao servidor
                packet = f"{info} {content}"
                sock.sendall(packet.encode("utf-8"))

            case "2":
                #manda um comando já programado ao servidor
                sock.sendall(b"COMANDO QUALQUER")

            case "0":
                sock.close
                not connected
                break

            case __:
                print("opcao invalida")



if __name__ == "__main__":
    main()