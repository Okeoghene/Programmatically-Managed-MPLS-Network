#!/usr/bin/python3
from netmiko import ConnectHandler
from getpass import getpass as passwd
import logging
import traceback
import sys

# Logging setup
logging.basicConfig(
    filename='netmiko_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("netmiko")

try:
    #getting the user password and enable password
    passphrase = passwd("Please enter User password: ")
    enable_passphrase = passwd("Please enter Enable password: ")

    #ip_inventory and config file path
    router_ips = "./vars/router_ips.txt"
    config_file = "./vars/config_file.txt"

    #load files
    def load_file(file_name):
        try:
            with open(file_name, "r") as file:
                lines = [line.strip() for line in file.readlines()]
                if not lines:
                    raise ValueError(f"{file_name} is empty.")
                return lines
        except Exception as e:
            print(f"Error loading file {file_name}: {e}")
            sys.exit(1)

    def create_ip_objects(ip):
        return {
            "device_type": "cisco_ios",
            "host": ip,
            "username": "omba",
            "password": passphrase,
            "secret": enable_passphrase
        }

    def updating_router(ip, config_lines):
        try:
            print(f"Creating connection object for {ip}...")
            ip_object = create_ip_objects(ip)
            print(f" Connecting to {ip}...")
            connection = ConnectHandler(**ip_object)
            print(f" Connected to {ip}...")
            connection.enable()
            print(f" In Config mode for {ip}...")
            commands = connection.send_config_set(config_lines)
            print(f" Commands have been sent to {ip}...")
            connection.disconnect()
            print(f" Disconnect {ip}...")
        except Exception as e:
            print(f"Error updating router {ip}: {traceback.format_exc()}")

    def main():
        ips = load_file(router_ips)
        config_lines = load_file(config_file)
        for ip in ips:
            updating_router(ip, config_lines)

    if __name__ == "__main__":
        main()
        
except Exception as e:
    logger.error(f"An error occurred: {e}")
    print("Error encountered. Check logs for details.")