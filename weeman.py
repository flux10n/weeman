#!/usr/bin/env python2

import sys
import optparse
from core.misc import printt
from core.config import user_agent as usera

def tests_pyver():
    if sys.version[:3] == "2.7" or "2" in sys.version[:3]:
        pass # All good
    elif "3" in sys.version[:3]:
        printt(1,"Weeman has no support for Python 3.")
    else:
        printt(1, "Your Python version is very old ..")

def tests_platform():
    if "linux" in sys.platform:
        #printt(3, "Running Weeman on linux ... (All good)")
        pass
    elif "darwin" in sys.platform:
        #printt(3, "Running Weeman on \'Mac\' (All good)")
        pass
    elif "win" in sys.platform:
        print("Sorry, there is no support for windows right now.")
        sys.exit(1)
    else:
        printt(3, "If \'Weeman\' runs sucsessfuly on your platform %s\nPlease let me (@Hypsurus) know!" %sys.platform)

def main():
    tests_pyver()
    tests_platform()
    parser = optparse.OptionParser()
    parser.add_option("-q", "--quiet", dest="quiet_mode_opt", action="store_true", default=False, help="Runs without displaying the banner.")
    parser.add_option("-p", "--profile", dest="profile", help="Load weeman profile.")
    options,r = parser.parse_args()

    if options.profile:
        from core.shell import shell_noint
        shell_noint(options.profile)
    else:
        from core.shell import shell
        shell()

if __name__ == '__main__':
    main()
