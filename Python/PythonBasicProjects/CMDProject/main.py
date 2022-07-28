import cmd
import subprocess

print('Python Cmd Application')
print('-----------------------')

def runCommand():
    while True:
        try:
            command = input('$ ')
            if command.lower() == 'exit':
                print('CMD Terminated ')
                break
            subprocess.run(command , shell=cmd)
        except:
            command = input('$ ')

runCommand()