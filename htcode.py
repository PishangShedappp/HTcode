import sys
import os
import requests
from requests import status_codes
from requests.api import request

os.system("color")

COLOR = {
    "BANNER": "\u001b[34m",
    "YELLOW": "",
    "GREEN": "",
    "RED": "",
    "ENDC": "",
}


def main():
    print(COLOR["BANNER"], """
         _    _  ______   ___    ___   ____   ____
        | |__| ||__  __| / __\  / _ \ |  _ \ |
        |  __  |   | |  | |__  | |_| || |_| ||----
        |_|  |_|   |_|	 \___/  \___/ |____/ |____   

    """, COLOR["ENDC"])

    # get file input
    fileinput = input(COLOR["YELLOW"], """Target filename: """, COLOR["ENDC"])

    # get status code
    getStat = input(COLOR["YELLOW"],"""Status code output (200 = 1, 302 = 2, 403 = 3, 404 = 4, all = 5): """, COLOR["ENDC"])

    # output name
    ofile = input(COLOR["YELLOW"],"""Output filename with extension : """, COLOR["ENDC"])
    print("")

    if getStat == "5":
        with open(fileinput) as f:
            for line in f:
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        print(line.strip() + COLOR["GREEN"],""" - 200""",COLOR["ENDC"])
                    elif r.status_code == 404:
                        print(line.strip() + COLOR["RED"],""" - 404""",COLOR["ENDC"])
                    elif r.status_code == 302:
                        print(line.strip() + COLOR["RED"],""" - 302""",COLOR["ENDC"])
                    elif r.status_code == 403:
                        print(line.strip() + COLOR["RED"],""" - 403""",COLOR["ENDC"])

                    with open(ofile, 'a') as o:
                        o.write(line.strip() + ' - ' +
                                str(r.status_code) + '\n')
                except requests.ConnectionError:
                    pass

    # process 200
    if getStat == "1":
        with open(fileinput) as f:
            for line in f:
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        print(line.strip() + COLOR["GREEN"],""" - 200""",COLOR["ENDC"])
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

    # process 302
    if getStat == "2":
        with open(fileinput) as f:
            for line in f:
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        pass
                    elif r.status_code == 404:
                        pass
                    elif r.status_code == 302:
                        print(line.strip() + COLOR["RED"],""" - 302""",COLOR["ENDC"])
                        with open(ofile, 'a') as o:
                            o.write(line.strip() + '\n')
                    elif r.status_code == 403:
                        pass
                except requests.ConnectionError:
                    pass

    # process 403
    if getStat == "3":
        with open(fileinput) as f:
            for line in f:
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        pass
                    elif r.status_code == 404:
                        pass
                    elif r.status_code == 302:
                        pass
                    elif r.status_code == 403:
                        print(line.strip() + COLOR["RED"],""" - 403""",COLOR["ENDC"])
                        with open(ofile, 'a') as o:
                            o.write(line.strip() + '\n')
                except requests.ConnectionError:
                    pass

    # process 404
    if getStat == "4":
        with open(fileinput) as f:
            for line in f:
                r = requests.get(line.strip())
                try:
                    if r.status_code == 200:
                        pass
                    elif r.status_code == 404:
                        print(line.strip() + COLOR["RED"],""" - 404""",COLOR["ENDC"])
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
