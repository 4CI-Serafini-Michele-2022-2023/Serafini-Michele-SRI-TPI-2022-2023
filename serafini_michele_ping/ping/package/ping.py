import os
import subprocess

if __name__=="__main__":
    fd = os.popen("ping 8.8.8.8 >> provaa.txt",'w')
    with open('output.txt', 'w') as output:
        process = subprocess.Popen('ping 127.0.0.1', stdout=output)
        process.communicate()