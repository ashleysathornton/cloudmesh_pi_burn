import os
from cloudmesh.common.util import banner
import sys

"""
ProxyPi is a class that will instantiate a Pi as a proxy server using squid3 as depicted in:

https://www.techrepublic.com/article/how-to-install-and-configure-squid-proxy-server-on-linux/

This class will automate the process linked through class initialization and management methods.
"""
class ProxyPi:
    """
    Usage:
    """
    def __init__(self, verbose=False):
        self.verbose = verbose
        if verbose:
            print("sudo apt-get install squid3")
        self.setup_squid()

    def setup_squid(self):
        self.install_squid()
        self.allow_localnet()
        self.restart_squid()

    def install_squid(self):
        banner("Installing Squid")
        os.system("sudo apt-get install squid3")
        banner("Finishined installation of Squid")

    def restart_squid(self):
        os.system("sudo service squid restart")

    def allow_localnet(self):
        # 1407#http_access allow localnet
        line = os.popen("sudo grep -n 'http_access allow localnet' /etc/squid/squid.conf").read().split()
        line_ref = line[0].split(":")[0] # ['1407', '#http_access']

        if self.verbose:
            banner(" ".join(line))

        with open('/etc/squid/squid.conf', 'r') as f:
            data = f.readlines()

        temp = line[0].split(":")

        if temp[1][0] != "#":
            # If the line is already uncommented, return
            if self.verbose:
                banner("http_access already allowed")
            return
            
        temp[1] = temp[1][1:]
        line[0] = temp[1]
        
        joined = " ".join(line)
        joined+="\n"
        data[int(line_ref)-1] = joined

        banner(f"Writing line {' '.join(line)}")

        try:
            with open('/etc/squid/squid.conf', 'w') as f:
                f.writelines(data)
        except IOError:
            sys.stderr.write('Error: Please be in root user \n')

            
            

        
        


def main():
    proxy = ProxyPi(verbose=True)

main()
