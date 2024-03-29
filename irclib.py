import socket
class IRC:
  def __init__(self, host, port, nick, channel):
    self.socket = socket.socket()
    self.socket.connect((host, port))
    send()
  def send(self, text):
    self.socket.send(bytes(text))
HOST = "irc.libera.chat"
PORT = 6667
NICK = "TechDude"
#PASSWORD = os.getenv("PASSWORD")
CHANNEL = "##techdudeserver"
#CHANNEL = "##BlockySurvival"
SERVER = ""
readbuffer = ""

send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
send(bytes("USER %s %s %s :%s\r\n" % (NICK, NICK, NICK, NICK), "UTF-8"))
send(bytes("JOIN {}\r\n".format(CHANNEL), "UTF-8"))
readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
temp = str.split(readbuffer, "\n")
readbuffer = temp.pop()
for line in temp:
    SERVER = str.rstrip(line)[1:].split()[0]
    print(str.rstrip(line))
while 1:
    readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()
    for line in temp:
        print(str.rstrip(line))
        message = str.rstrip(line).split(" PRIVMSG {} :".format(CHANNEL))
        if "PING" in line:
            send("PONG :{}\r\n".format(SERVER).encode("utf-8"))
        msg = message[-1]
        tokens = msg.split()
        if msg == "$hello":
            send("PRIVMSG {} :Hello!\r\n".format(CHANNEL).encode("utf-8"))
