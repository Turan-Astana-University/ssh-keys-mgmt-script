import paramiko
import openpyxl
import multiprocessing
from datetime import datetime
import commands

lst = [52, 54, 55, 56, 57, 58, 53,]
ssh = paramiko.SSHClient()

ssh.load_system_host_keys()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
workbook = openpyxl.Workbook()

sheet = workbook.active

def connect(hostname, username, password, command):
    print(hostname)
    cmd = command["command"]
    good_operation = command["200"]
    authentication = command["Authentication Error"]
    timeout = command["TimeOut Error"]
    try:
        ssh.connect(hostname, username=username, password=password) # Connect
        stdin, stdout, stderr = ssh.exec_command(cmd)

        # Excel
        print("готово")
        sheet[f"A{rng+1}"] = hostname
        sheet[f"B{rng+1}"] = good_operation
    except TimeoutError:
        print("TimeOut Error")
        sheet[f"A{rng+1}"] = hostname
        sheet[f"B{rng+1}"] = timeout

    except paramiko.ssh_exception.AuthenticationException:
        print("AuthenticationError Error")
        sheet[f"A{rng+1}"] = hostname
        sheet[f"B{rng+1}"] = authentication
        return "account"
    finally:
        ssh.close()

for rng, i in enumerate(lst):
    hostname = f"192.168.22.{i}"
    command = commands.shutdown()
    data = connect(hostname, 'User', "739146", command)
    if data == "account":
        data = connect(hostname, 'User', "TIT2023!", command)
        if data == "account":
            data = connect(hostname, 'User', "917346", command)
else:
    current_date_time = datetime.now()
    current_date = current_date_time.date()
    workbook.save(f'{current_date}_result.xlsx')