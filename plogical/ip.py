#!/usr/local/CyberCP/bin/python
import os
import os.path
import sys
import django

class IPManager:
    __machineIP_file_read = False
    IPv4 = []
    IPv6 = []
    
    @staticmethod
    def ReadMachineIPFile():
        try:
            ipFile = "/etc/cyberpanel/machineIP"
            f = open(ipFile)
            for line in f:
                line = line.lstrip()

                # Allow the entire line to be commented out
                if line.startswith('#'):
                    continue

                # Check if the ip is an IPv4 address by the lack of a colon
                if line.find(':') != -1:
                    IPManager.IPv4.append(line)
                else:
                    IPManager.IPv6.append(line)

            return 1
        except:
            return 0

    @staticmethod
    def GetIPv4Addresses():
        return IPManager.IPv4

    @staticmethod
    def GetIPv6Addresses():
        return IPManager.IPv6


