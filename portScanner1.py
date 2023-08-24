import socket

""" Primeiro programa PORTSCANNER """

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.05)

ip = input("Digite o host ou ip a ser verificado: ")
port = int(input("Digite a porta a ser verificada: "))

code = client.connect_ex((ip, port))
print(code)

if code == 0:
    print('Porta Aberta!')
else:
    print('Porta Fechada!')
