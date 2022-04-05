from operator import truediv
import re
import math

class CalcIPv4:
    """
    Calculates IPv4 networks

     Usage mode 1:
     calc_ipv4 = CalcIPv4(ip='192.168.0.128', prefix=10)

     Usage mode 2:
     calc_ipv4 = CalcIPv4(ip='192.168.0.128', mask='255.255.255.0')
    """

    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        if mascara is None and prefixo is None:
            raise ValueError('Need to send mask or prefix')

        if mascara and prefixo:
            raise ValueError('Need to send mask or prefix, not both.')
        
        
        # if math.isnan(ip):
            #raise ValueError('You cannot use character to calc IP')

        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        if self._prefixo is None:
            return

        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('Invalid IP.')

        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return

        if not self._valida_ip(valor):
            raise ValueError('Invalid Net Mask.')

        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)

        if not hasattr(self, 'prefix'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        if valor is None:
            return

        try:
            valor = int(valor)
        except:
            raise ValueError('Prefix must be an integer.')

        if valor > 32 or valor < 0:
            raise TypeError('Prefix neet to have 32Bits.')

        self._prefixo = valor
        self._mascara_bin = (valor * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True
        else:
            print("Wrong format. Try Again. IP shoud be ex 10.0.0.1 mask 255.0.0.0 or prefix ex 30")

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(bloco))[2:].zfill(8) for bloco in blocos]
        blocos_bin_str = ''.join(blocos_bin)
        qtd_bits = len(blocos_bin_str)

        if qtd_bits > 32:
            raise ValueError('IP or Mask is longer than 32 bits.')

        return blocos_bin_str

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)

def IPcalc():
         # Com prefixo

        while True:
            prefixormask=input("Do you Want to use Prefix or Masc? Use (P) to Prefix or (M) to mask: ")
            if prefixormask=='p' or prefixormask=='P' and math.isnan(prefixormask) ==False:
                try:
                    myip=input("Type the IP Address/Network (ex:192.168.1.0): ")
                    mymask=input("Type the prefix (ex:30): ")
                    calc_ipv4_1 = CalcIPv4(ip=myip, prefixo=mymask)
                    print('#' * 80)
                    print(f'IP: {calc_ipv4_1.ip}')
                    print(f'Network Mask: {calc_ipv4_1.mascara}')
                    print(f'Network: {calc_ipv4_1.rede}')
                    print(f'Broadcast: {calc_ipv4_1.broadcast}')
                    print(f'Prefix: {calc_ipv4_1.prefixo}')
                    print(f'Number of network IPs: {calc_ipv4_1.numero_ips}')
                    print('#' * 80)
                    exitmode=input("To quit press [Q] or [q]. To continue using IP Calc -> Press any key : ")
                    if exitmode == 'Q' or exitmode=='q':
                        print("You exit from IP calc")
                        break
                except ValueError:
                    print("Oops!  That was no valid IP or Prefix format.  Please try again....")

        
     # Com máscara
            elif prefixormask=='m' or prefixormask=='M' and math.isnan(prefixormask) ==False:
                try:
                    myip=input("Type the IP Address or Network (ex:192.168.1.0): ")
                    mymask=input("Type the Mask (ex:255.255.255.0): ")
                    calc_ipv4_2 = CalcIPv4(ip=myip, mascara=mymask)
                    print('#' * 80)
                    print(f'IP: {calc_ipv4_2.ip}')
                    print(f'Network Mask: {calc_ipv4_2.mascara}')
                    print(f'Network: {calc_ipv4_2.rede}')
                    print(f'Broadcast: {calc_ipv4_2.broadcast}')
                    print(f'Prefix: {calc_ipv4_2.prefixo}')
                    print(f'Number of network IPs: {calc_ipv4_2.numero_ips}')
                    print('#' * 80)
                    exitmode=input("To quit press [Q] or [q]. To continue using IP Calc -> Press any key : ")
                    if exitmode == 'Q' or exitmode=='q':
                        print("You exit from IP calc")
                        break
                except ValueError:
                    print("Oops!  That was no valid IP or Mask format.  Please try again...")
                    
            else:
                print("Invalid choice, please type 'P' or 'M'.")
                print("Please Start IP Calc again :) !!")
def main():
    IPcalc()
if __name__ == '__main__':
    main()