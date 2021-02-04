import wmi

f = wmi.WMI()
print("pid  Process name")
try:
    for process in f.Win32_Process():
        if process.Name == "pycharm64.exe":
            process.Terminate()
        else:
            print("No such process running")
except:
    print("Some error happened...")



