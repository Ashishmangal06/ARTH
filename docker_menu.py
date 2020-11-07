import os

os.system("tput setaf 1")
print("\t\t\tWelcome to Docker Terminal User Interface")
os.system("tput setaf 7")

print("\t\t\t-----------------------------------------")

while True:
  print("Do You want to perform your job(y/n) : ", end='')
  choice = input()

  if(choice=="N" or choice=='n'):
    exit()
  else:
    print("kindly enter the location(remote/local): ", end='')
    location=input()

    if location == "remote":
      remoteIP = input("Enter your IP : ")


    print("""
        press1: To install docker
        press2: To start docker
        press3: To search image
        press4: To pull docker image
        press5: To check images available
        press6: To run a container
        press7: To check container status
        press8: To start a stopped container
        press9: To check image logs
        press0: To exit
        """)
    print("Enter your choice : " , end="")
    ch = input()
    print(ch)

    if location == "local":
      if int(ch) == 1:
        os.system("yum install docker-ce --nobest")
      elif int(ch) == 2:
        os.system("systemctl start docker")
        os.system("systemctl enable docker")
      elif int(ch) == 3:
        print("Which image you want to search : ", end='')
        image_name = input()
        os.system("docker search {}" .format(image_name))
      elif int(ch) == 4:
        print("which image you want to pull : ", end='')
        image_name = input()
        print("Enter image tag : ", end='')
        image_tag = input()
        os.system("docker pull {}:{}" .format(image_name , image_tag))
      elif int(ch) == 5:
        os.system("docker images")
      elif int(ch) == 6:
        print("write the image name with tag you want to run : ", end='')
        image_name = input()
        print("Enter name of container : ", end='')
        cont_name = input()
        os.system("docker run -dit --name {} {}" .format(cont_name , image_name))
      elif int(ch) == 7:
        os.system("docker ps -a")
      elif int(ch) == 8:
        print("Enter the container name : ", end='')
        cont_name = input()
        os.system("docker start {}" .format(cont_name))
      elif int(ch) == 9:
        print("Enter container name : ", end='')
        cont_name = input()
        os.system("docker logs {}" .format(cont_name))
      elif int(ch) == 0:
        print("Thank you for using this terminal")
        exit()
      else:
        print("option not supported")

      input("Enter to continue.........")
      os.system("clear")

    elif location == "remote":
      if int(ch) == 1:
        os.system("ssh {0} yum install docker-ce --nobest" .format(remoteIP))
      elif int(ch) == 2:
        os.system("ssh {0} systemctl start docker" .format(remoteIP))
        os.system("ssh {0} systemctl enable docker" .format(remoteIP))
      elif int(ch) == 3:
        print("Which image you want to search : ", end='')
        image_name = input()
        os.system("ssh {0} docker search {}" .format(image_name , remoteIP))
      elif int(ch) == 4:
        print("which image you want to pull : ", end='')
        image_name = input()
        print("Enter image tag : ", end='')
        image_tag = input()
        os.system("ssh {0} docker pull {}:{}" .format(image_name , image_tag , remoteIP))
      elif int(ch) == 5:
        os.system("ssh {0} docker images" .format(remoteIP))
      elif int(ch) == 6:
        print("write the image name with tag you want to run : ", end='')
        image_name = input()
        print("Enter name of container : ", end='')
        cont_name = input()
        os.system("ssh {0} docker run -dit --name {} {}" .format(cont_name , image_name , remoteIP))
      elif int(ch) == 7:
        os.system("ssh {0} docker ps -a" .format(remoteIP))
      elif int(ch) == 8:
        print("Enter the container name : ", end='')
        cont_name = input()
        os.system("ssh {0} docker start {}" .format(cont_name , remoteIP))
      elif int(ch) == 9:
        print("Enter container name : ", end='')
        cont_name = input()
        os.system("ssh {0} docker logs {}" .format(cont_name , remoteIP))
      elif int(ch) == 0:
        print("Thank you for using docker container")
        exit()
      else:
        print("option not supported")

    else:
      print("location not supported")
