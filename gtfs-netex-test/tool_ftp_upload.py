from ftplib import FTP_TLS
import os
import paramiko
from configuration import ftpconns
# Example configuration dictionary
from aux_logging import *

def upload_to_ftps(filepath, myconfig):
    # Extract configuration details
    config=ftpconns["myconfig"]
    server = config['server']
    directory = config['directory']
    username = config['username']
    password = config['password']
    protocol = config.get('protocol')
    port = config.get('port', 21)  # Default to port 21 if not specified

    if protocol=='ftps':
        # Connect to the FTPS server
        ftps = FTP_TLS()
        ftps.connect(server, port)
        ftps.login(username, password)
        ftps.prot_p()  # Secure data connection

        # Change to the specified directory
        ftps.cwd(directory)

        # Get the filename from the filepath
        filename = os.path.basename(filepath)

        # Open the file in binary mode and upload it
        with open(filepath, 'rb') as file:
            ftps.storbinary(f'STOR {filename}', file)

        # Close the FTPS connection
        ftps.quit()
    elif protocol=="sftp":
        filename = os.path.basename(filepath)
        # Set up the SFTP client
        transport = paramiko.Transport((server, port))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        try:
            # Change to the specified directory
            sftp.chdir(directory)

            # Open the file in binary mode and upload it
            with open(filepath, 'rb') as file:
                sftp.putfo(file, filename)
        finally:
            # Close the SFTP connection
            sftp.close()
            transport.close()
    else:
        log_all("Only ftps and sftp supported")






if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Compresses a NeTEx file')
    parser.add_argument('file', type=str, help='file name to upload')
    parser.add_argument('myconfig', type=str,  help='Config to use from the ftp conns dict in the configurations')
    args = parser.parse_args()
    upload_to_ftps(args.file, args.myconfig)