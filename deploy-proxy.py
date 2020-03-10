import os
from cloudmesh.common.util import banner
import sys

"""
ProxyPi is a class that will instantiate a Pi as a proxy server using squid3 as depicted in:

https://www.techrepublic.com/article/how-to-install-and-configure-squid-proxy-server-on-linux/

This class will automate the process linked through class initialization and management methods.

Use 'curl -x http://<squid-proxy-server-IP>:3128  -I http://google.com' to verify it is working

Ensure you are in root user (sudo su) mode.
"""


class ProxyPi:
    """
    Usage:

    TODO

    """

    # Installs squid
    # allow localnet http_access
    def __init__(self, verbose=False):
        self.verbose = verbose
        if verbose:
            print("sudo apt-get install squid3")
        self.install_squid()
        self.allow_localnet()
        self.restart_squid()

    # Writes a config file to /etc/squid/piproxy.conf and includes it in the main default file (if it exists)
    # Otherwise it creates the necessary files
    def conf_proxy(self):
        # Create the config file if they exist
        try:
            os.system("sudo touch /etc/squid/conf.d/piproxy.conf")

        except BaseException:
            raise Exception(
                "There is something wrong with your squid installation")

        config = \
            """
        shutdown_lifetime = 5 seconds
        http_access allow localnet
        """

        with open('/etc/squid/conf.d/piproxy.conf', 'w') as proxy_file:
            proxy_file.writelines(config)

        self.restart_squid()

    def install_squid(self):
        banner("Installing Squid")
        os.system("sudo apt-get install squid3")
        banner("Finishined installation of Squid")

    def start_squid(self):
        if self.verbose:
            banner("Starting Squid Sever!")
        os.system("sudo service squid start")

    def start_squid(self):
        if self.verbose:
            banner("Stopping Squid Sever!")
        os.system("sudo service squid stop")

    def restart_squid(self):
        os.system("sudo service squid restart")


"""
def main():
    proxy = ProxyPi(verbose=True)

main()
"""
