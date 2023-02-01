import time
import getpass
import sys
#from pexpect import pxssh
import paramiko

#VETOR DE IPS
vetip = ["192.168.121.10","192.168.121.11","192.168.121.12","192.168.121.13","192.168.121.14","192.168.121.15"]

#USUARIO DE ACESSO
usr = "ubnt"
psswd = "ubnt"

#Command
command1 = 'reboot'

for host in vetip:
        try:
                cli = paramiko.SSHClient()
                cli.load_system_host_keys()
                cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                cli.connect(host, port=22, username=usr, password=psswd)
                time.sleep(7)

                stdin1, stdout1, stderr1 = cli.exec_command(command1)
                print(f'Reiniciado Antena {host}')
                time.sleep(1)
        except TimeoutError:
                print(f'Antena {host} Não foi possível estabelecer uma conexão SSH')

        finally:
                cli.close()
