import argparse
from bannermagic import printBannerPadding, printMessage

class ArgumentHandler:

    def __init__(self):
        self.printBanner()
        parser = self.ConfigureParser()
        args = parser.parse_args()
        self.verbosity = args.verbose
        self.url = args.url
        if args.manual_proxy_list:
            self.proxy_list = manual_proxy_list
        elif args.input_proxy_file:
            self.proxylist = args.input_proxy_file.read()
        self.enable_proxies = args.enabled_proxies
        self.proxy_depth = args.proxy_depth

    def printBanner(self):
        printBannerPadding('*')
        printMessage('LFITester')
        printMessage('Automated LFI Testing')
        printBannerPadding('*')

    def ConfigureParser(self):   
        parser = argparse.ArgumentParser(prog='LFITester.py', description='LFI Automated tester.', epilog='Proxies in the list must be in the following format: protocol://{proxyip} username:password (newline). If you dont have a authenticated proxy then skip the username:password entry and go for a new line')
        parser.add_argument('url', help='The url to test. The URL format must be http://[URL]?[something]=')
        parser.add_argument('-m', '--set-manual-proxy-list', dest="manual_proxy_list",  help="The proxy urls to add (The script expects proxies without authentication. For authenticated proxies use input files.", nargs='*')
        parser.add_argument('-v', '--verbose', action='count', help='Increase output verbosity', default=0)
        parser.add_argument('-p', '--enable-proxies', dest="enabled_proxies", action='store_true', help="Enable proxy redirection. Default proxies are free and you can change them. If you don't want the default proxies you can supply your own and this option will be overrided! Note that the the proxies will be picked at random for each request")
        parser.add_argument('-d', '--proxy-depth', dest="proxy_depth", type=int,  help="Set proxy depth. How many proxies do you want to proxy your requests through?", default=1)
        parser.add_argument('-l', '--list-proxies', dest="input_proxy_file", help='Input a list of proxies from an external file.', type=argparse.FileType('r'))

        return parser
