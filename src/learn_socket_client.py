import socket  # for sockets
import sys  # for exit

# 创建socket套接字
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET IPv4地址族
# socket.AF_INET6 IPv6地址族

# 创建TCP Socket：
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 创建UDP Socket：
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit();

print('Socket Created')
host = 'http://www.zhihu.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    # could not resolve
    print
    'Hostname could not be resolved. Exiting'
    sys.exit()

print('Ip address of ' + host + ' is ' + remote_ip)
# Connect to remote server
s.connect((remote_ip, port))
print('Socket Connected to ' + host + ' on ip ' + remote_ip)
# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
try:
    # Set the whole string
    s.sendall(message)
except socket.error:
    # Send failed
    print('Send failed')
    sys.exit()

print('Message send successfully')
# Now receive data
reply = s.recv(4096)  # 参数是接收的数据长度
print(reply)
s.close()
