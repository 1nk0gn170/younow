import urllib.request
import json
import os

def main():

    os.system("cls")

    print("                                             YouNow Resolver by Inkognito")

    eing = input("\n\nName: ")
    print("")

    resp = urllib.request.urlopen(f"https://api.younow.com/php/api/broadcast/info/user={eing}").read()

    obj = json.loads(resp.decode("UTF-8"))

    try:
        for i in obj["user"]:
            print(i + ": " + str(obj["user"][i]))
    except:
        print("Der Benutzer ist offline oder er existiert nicht.")
        input()
        main()

    input()
    main()

main()