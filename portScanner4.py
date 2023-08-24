import nmap

scanner = nmap.PortScanner()

print(f"Seja bem vindo ao Dio Scanner!")
print(f"<----------------------------->")

ip = input(f"Digite o IP a ser varrido: ")
print(f"O IP digitado foi: {ip}")
type(ip)


def Menu():
    menu = input("""\n  Escolha o tipo de varredura:
    1) -> Varredura do tipo SYN
    2) -> Varredura do tipo UDP
    3) -> Varredura do tipo Intensa
    Digite a opção escolhida: """).strip()

    print(f"\nA opção escolhida foi: {menu}")

    while menu == "1" or "2" or "3":
        if menu == "1":
            scanner.scan(ip, '1-2048', '-v -sS')
            print(f"Versão do NMAP {scanner.nmap_version()}")
            print(scanner.scaninfo())
            print(f"Status do IP: {scanner[ip].state()}")
            print(f"Protocolo: {scanner[ip].all_protocols()}")
            print()
            print(f"Portas Abertas: {scanner[ip]['tcp'].keys()}")
            break
        elif menu == "2":
            scanner.scan(ip, '1-2048', '-v -sU')
            print(f"Versão do NMAP {scanner.nmap_version()}")
            print(scanner.scaninfo())
            print(f"Status do IP: {scanner[ip].state()}")
            print(f"Protocolo: {scanner[ip].all_protocols()}")
            print()
            print(f"Portas Abertas: {scanner[ip]['udp'].keys()}")
            break
        elif menu == "3":
            scanner.scan(ip, '1-2048', '-v -sC')
            print(f"Versão do NMAP {scanner.nmap_version()}")
            print(scanner.scaninfo())
            print(f"Status do IP: {scanner[ip].state()}")
            print(f"Protocolo: {scanner[ip].all_protocols()}")
            print()
            print(f"Portas Abertas: {scanner[ip]['tcp'].keys()}")
            break
        else:
            print(f"\nDigite somente valores de 1 á 3, tente novamente:")
            Menu()


Menu()
