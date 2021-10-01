import sys
import os
import requests
from requests import status_codes
from requests.api import request


def main():
    print("""\u001b[34m
         _    _  ______   ___    ___   ____   ____
        | |__| ||__  __| / __\  / _ \ |  _ \ |
        |  __  |   | |  | |__  | |_| || |_| ||----
        |_|  |_|   |_|	 \___/  \___/ |____/ |____   

    \u001b[0m""")

    #get file input
    fileinput = input("""\u001b[33mTarget filename: \u001b[0m""")

    #get status code
    getStat = input("""\u001b[33mStatus code output (200 = 1, 302 = 2, 403 = 3, 404 = 4, all = 5): \u001b[0m""")

    #output name
    ofile = input("""\u001b[33mOutput filename with extension : \u001b[0m""")
    print("")

    if getStat == "5":
        with open(fileinput) as f:
            for line in f :
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        print(line.strip() + """\u001b[32m - 200\u001b[0m""")
                    elif r.status_code == 404:
                        print(line.strip() + """\u001b[31m - 404\u001b[0m""")
                    elif r.status_code == 302:
                        print(line.strip() + """\u001b[31m - 302\u001b[0m""")
                    elif r.status_code == 403:
                        print(line.strip() + """\u001b[31m - 403\u001b[0m""")

                    with open(ofile, 'a') as o:
                        o.write(line.strip() + ' - ' + str(r.status_code) + '\n') 
                except requests.ConnectionError:
                    pass

    #process 200
    if getStat == "1":
        with open(fileinput) as f:
            for line in f :
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        print(line.strip() + """\u001b[32m - 200\u001b[0m""")
                        with open(ofile, 'a') as o:
                            o.write(line.strip() + '\n')
                    elif r.status_code == 404:
                        pass
                    elif r.status_code == 301:
                        pass
                    elif r.status_code == 403:
                        pass
                except requests.ConnectionError:
                    pass

    #process 302
    if getStat == "2":
        with open(fileinput) as f:
            for line in f :
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        pass
                    elif r.status_code == 404:
                        pass
                    elif r.status_code == 302:
                        print(line.strip() + """\u001b[31m - 302\u001b[0m""")
                        with open(ofile, 'a') as o:
                            o.write(line.strip() + '\n')
                    elif r.status_code == 403:
                        pass
                except requests.ConnectionError:
                    pass

    #process 403
    if getStat == "3":
        with open(fileinput) as f:
            for line in f :
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        pass
                    elif r.status_code == 404:
                        pass
                    elif r.status_code == 302:
                        pass
                    elif r.status_code == 403:
                        print(line.strip() + """\u001b[31m - 403\u001b[0m""")
                        with open(ofile, 'a') as o:
                            o.write(line.strip() + '\n')
                except requests.ConnectionError:
                    pass
    
    #process 404
    if getStat == "4":
        with open(fileinput) as f:
            for line in f :
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        pass
                    elif r.status_code == 404:
                        print(line.strip() + """\u001b[31m - 404\u001b[0m""")
                        with open(ofile, 'a') as o:
                            o.write(line.strip() + '\n')
                    elif r.status_code == 302:
                        pass
                    elif r.status_code == 403:
                        pass
                except requests.ConnectionError:
                    pass

if __name__ == "__main__":
    main()
