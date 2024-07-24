#sys.exit() function causes execution before the actual exit.

import sys
while True:
    print("Trying to exit before it actually exits. :)")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed " + response+ ".")
