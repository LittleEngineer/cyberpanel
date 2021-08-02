#!/usr/local/CyberCP/bin/python
import os
import os.path
import sys
import django

class IPManager:
    __machineIP_file_read = 0
    __ipv4_addresses = []
    __ipv6_addresses = []
    
    @staticmethod
    def __readMachineIPFile():
        try:
            ipFile = "/etc/cyberpanel/machineIP"
            data = open(ipFile).readlines()
            for line in data:
                line = line.strip()

                # Allow the entire line to be commented out
                #if line.startswith('#'):
                #    continue

                # Check if the ip is an IPv4 address by the lack of a colon
                if line.find(':') == -1:
                    IPManager.__ipv4_addresses.append(line)
                else:
                    IPManager.__ipv6_addresses.append(line)

            IPManager.__machineIP_file_read = 1
            return 1
        except:
            return 0

    @staticmethod
    def getIPv4Addresses():
        if IPManager.__machineIP_file_read == 0:
            if IPManager.__readMachineIPFile() == 0:
                return ["192.168.100.1"]
        return IPManager.__ipv4_addresses

    @staticmethod
    def getIPv6Addresses():
        if IPManager.__machineIP_file_read == 0:
            if IPManager.__readMachineIPFile() == 0:
                return None
        return IPManager.__ipv6_addresses

    @staticmethod
    def getIPAddresses():
        if IPManager.__machineIP_file_read == 0:
            if IPManager.__readMachineIPFile() == 0:
                return ["192.168.100.1"]
        return IPManager.__ipv4_addresses + IPManager.__ipv6_addresses


