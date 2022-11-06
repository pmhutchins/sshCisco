from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("Please enter your SSH username: ")
PASS = getpass("Please enter your SSH password: ")

device = {
    "ip": "192.168.1.10",
    "username": USERNAME,
    "password": PASS,
    "device_type": "cisco_ios",
}

c = ConnectHandler(**device)
