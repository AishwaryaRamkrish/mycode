#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request as ub
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    groundctrl = ub.urlopen(MAJORTOM)

    helmet = groundctrl.read()
    # print(helmet)
    helmetson = json.loads(helmet.decode("utf-8"))
    # print(type(helmetson))

    print(f"People in space: {helmetson['number']}")
    # print(f"People in space: {helmetson['people'][]}")

    for a in helmetson['people']:
        print(f"{a['name']} on the {a['craft']}")





if __name__ == "__main__":
    main()
