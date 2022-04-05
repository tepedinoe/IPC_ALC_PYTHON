# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

# from random_numbers import append_random_words
import pytest
import  IP_NetWork_Calc 
from IP_NetWork_Calc import CalcIPv4
import random

def radom_ip():
    ip = ".".join(map(str, (random.randint(0, 255)
                            for _ in range(4))))
    return ip

def radom_mask():
    ip = ".".join(map(str, (random.randint(0, 255)
                            for _ in range(4))))
    return ip

def radom_prefix():
    n = random.randint(0,32)
    return n

def testcalcnetwork():
    calc_ipv4_1 = CalcIPv4(ip='192.168.0.128', prefixo=30)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.192')
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')
    
def testcalcnetwork2():
    IP= radom_ip()
    mask=radom_mask()
    prefix=radom_prefix()
    calc_ipv4_1 = CalcIPv4(IP, prefixo=prefix)
    print(radom_ip)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(IP, mascara=mask)
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')
    
def testcalcnetwork3():
    IP= radom_ip()
    mask=radom_mask()
    prefix=radom_prefix()
    calc_ipv4_1 = CalcIPv4(IP, prefixo=prefix)
    print(radom_ip)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(IP, mascara=mask)
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')

def testcalcnetwork4():
    IP= radom_ip()
    mask=radom_mask()
    prefix=radom_prefix()
    calc_ipv4_1 = CalcIPv4(IP, prefixo=prefix)
    print(radom_ip)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(IP, mascara=mask)
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')
    
def testcalcnetwork5():
    IP= radom_ip()
    mask=radom_mask()
    prefix=radom_prefix()
    calc_ipv4_1 = CalcIPv4(IP, prefixo=prefix)
    print(radom_ip)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(IP, mascara=mask)
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')
    
def testcalcnetwork6():
    calc_ipv4_1 = CalcIPv4(ip='192.168.0.128', prefixo=30)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.192')
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')
    
def testcalcnetwork7():
    IP= radom_ip()
    mask=radom_mask()
    prefix=radom_prefix()
    calc_ipv4_1 = CalcIPv4(IP, prefixo=prefix)
    print(radom_ip)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(IP, mascara=mask)
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')
    
def testcalcnetwork8():
    IP= radom_ip()
    mask=radom_mask()
    prefix=radom_prefix()
    calc_ipv4_1 = CalcIPv4(IP, prefixo=prefix)
    print(radom_ip)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(IP, mascara=mask)
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')

def testcalcnetwork9():
    IP= radom_ip()
    mask=radom_mask()
    prefix=radom_prefix()
    calc_ipv4_1 = CalcIPv4(IP, prefixo=prefix)
    print(radom_ip)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(IP, mascara=mask)
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')
    
def testcalcnetwork10():
    IP= radom_ip()
    mask=radom_mask()
    prefix=radom_prefix()
    calc_ipv4_1 = CalcIPv4(IP, prefixo=prefix)
    print(radom_ip)
    print(f'IP: {calc_ipv4_1.ip}')
    print(f'MASK: {calc_ipv4_1.mascara}')
    print(f'NETWORK: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefix: {calc_ipv4_1.prefixo}')
    print(f'The Numbers of IPs: {calc_ipv4_1.numero_ips}')
    calc_ipv4_2 = CalcIPv4(IP, mascara=mask)
    print(f'IP: {calc_ipv4_2.ip}')
    print(f'MASK: {calc_ipv4_2.mascara}')
    print(f'NETWORK: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefix: {calc_ipv4_2.prefixo}')
    print(f'The Numbers of IPs:: {calc_ipv4_2.numero_ips}')

#def test_append_random_words():
#    """Verify that the append_random_words function works correctly.
#    Parameters: none
#    Return: nothing
#    """
#    words_list = []
#    assert len(words_list) == 0
#
#    append_random_words(words_list)
#    assert len(words_list) == 1
#    for word in words_list:
#        assert isinstance(word, str)
#        assert len(word) >= 1
#
#    append_random_words(words_list, 3)
#    assert len(words_list) == 4
#    for word in words_list:
#        assert isinstance(word, str)
#        assert len(word) >= 1


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
