# [Bind Shell with password in Python]()
You don't need to install anything.
- Run the victim.py (victim machine), simply write:
    ```
    python victim.py
    ```
    **Note: To hide the console change victim.py to victim.pyw:**

- Run attacker.py in your machine :
    ```
    python attacker.py
    ```
- It will ask for host and port (default port: 2002)
  -In my case:
  - <p align="left">
     <img src="https://github.com/sky9262/shellBit/blob/main/bind_shell/img/Step1.png?raw=true">
    </p>

- Now if victim.py is running, It will ask for password (default: open@bind)
  - <p align="left">
     <img src="https://github.com/sky9262/shellBit/blob/main/bind_shell/img/Step2.png?raw=true">
    </p>
- After successfully authentication you will get a shell
