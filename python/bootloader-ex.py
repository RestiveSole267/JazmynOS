from time import sleep

logo = ("""
░░░░░██╗░█████╗░███████╗███╗░░░███╗██╗░░░██╗███╗░░██╗░█████╗░░██████╗
░░░░░██║██╔══██╗╚════██║████╗░████║╚██╗░██╔╝████╗░██║██╔══██╗██╔════╝
░░░░░██║███████║░░███╔═╝██╔████╔██║░╚████╔╝░██╔██╗██║██║░░██║╚█████╗░
██╗░░██║██╔══██║██╔══╝░░██║╚██╔╝██║░░╚██╔╝░░██║╚████║██║░░██║░╚═══██╗
╚█████╔╝██║░░██║███████╗██║░╚═╝░██║░░░██║░░░██║░╚███║╚█████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░╚═════╝░
                       A modern operating system                                   
                              BUILD 100
""")

print('[0.36945] NET RTL8139 MAC 52-54-00-12-34-56')
sleep(1)
print('[0.36945] ATA 0:0 QEMU HARDDISK QMOOOO1 (32 MB)')
sleep(1)
print('[0.36945] MFS Superblock found in ATA 0:0')
sleep(2)
print(logo)
user = input("Username: ")
passw = input("Password: ")
