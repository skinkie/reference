from ftplib import FTP_TLS
import os
from configuration import ftpconns
# Example configuration dictionary


def upload_to_ftps(filepath, myconfig):
    # Extract configuration details
    config=ftpconns["myconfig"]
    server = config['server']
    directory = config['directory']
    username = config['username']
    password = config['password']
    port = config.get('port', 21)  # Default to port 21 if not specified

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




if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Compresses a NeTEx file')
    parser.add_argument('file', type=str, help='file name to upload')
    parser.add_argument('myconfig', type=str,  help='Config to use from the ftpconns dict in the configurations')
    args = parser.parse_args()
    upload_to_ftps(args.file, args.myconfig)