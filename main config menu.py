from main_namenode import namenode_configuration
from main_datanode import datanode_configuration
import os

while True:
    os.system("clear")
    print('''\tAutomated cluster setup
    1. Configure system as namenode
	2. Configure system as datanode
	3. Start Namenode (if system is already configured as namenode) 
	4. Start Datanode (if system is already configured as datanode)
	5. Get the report of the cluster created
	6. Exit
	''')

    user_input = int(input("Enter your choice: "))
    if user_input == 6:
        exit()
    else:
        login = input("You would like to run this command in local or remote system (enter r or l): ")

        if login == "l":
            if user_input == 1:
                namenode_configuration()
                print("\nDone The system has now been setup as Namenode ")
            elif user_input == 2:	
                datanode_configuration()
                print("\nDone The system has now been setup as Datanode")
            elif user_input == 3:	
                os.system("hadoop-daemon.sh start namenode")
                os.system("jps")
            elif user_input == 4:	
                os.system("hadoop-daemon.sh start namenode")
                os.system("jps")
            elif user_input == 5:
                os.system("hadoop dfsadmin -report")
            elif user_input == 6:
                exit()
            else:
                print("Invalid Choice from menu")                
        elif login == "r":
            remote_ip = input("Enter the IP of the system you want to login to: ")
            if user_input == 1:
                os.system("ssh root@{ip} 'cd /root/Desktop/arth-python && python3 namenode.py && hadoop namenode -format'".format(ip = remote_ip))
                print("\nDone The system has now been setup as Namenode")	
            elif user_input == 2:
                os.system("ssh root@{ip} 'cd /root/Desktop/arth-python && python3 datanode.py'".format(ip = remote_ip))
                print("\nDone The system has now been setup as Datanode")
            elif user_input == 3:
                os.system("ssh root@{ip} 'hadoop-daemon.sh start namenode && jps'".format(ip = remote_ip))
            elif user_input == 4:
                os.system("ssh root@{ip} 'hadoop-daemon.sh start datanode && jps'".format(ip = remote_ip))
            elif user_input == 5:
                os.system("hadoop dfsadmin -report")
            elif user_input == 6:
                exit()
            else:
                print("Invalid Choice from menu")
    input("Please press enter to continue..")