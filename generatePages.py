import os
import colorama
import json
import sys

arglist = sys.argv

# Check if config files exist
FoundCount = 0
ConfigFilesCount = 6
checkDirTreeNavbar = os.path.exists(os.path.join(os.getcwd(), 'config', 'navbar', 'default.json'))
if checkDirTreeNavbar == True:
    print(f'{colorama.Fore.GREEN}Found {colorama.Fore.RESET}navbar {colorama.Fore.GREEN}config!')
    FoundCount += 1
else:
    print(f'{colorama.Fore.RED}Couldn\'t find {colorama.Fore.RESET}navbar {colorama.Fore.RED}config!')
checkDirTreePages = os.path.exists(os.path.join(os.getcwd(), 'config', 'pages', 'default.json'))
if checkDirTreePages == True:
    print(f'{colorama.Fore.GREEN}Found {colorama.Fore.RESET}pages {colorama.Fore.GREEN}list!')
    FoundCount += 1
else:
    print(f'{colorama.Fore.RED}Couldn\'t find {colorama.Fore.RESET}pages {colorama.Fore.RED}list!')
checkDirTreePages = os.path.exists(os.path.join(os.getcwd(), 'config', 'pages', 'metatags.json'))
if checkDirTreePages == True:
    print(f'{colorama.Fore.GREEN}Found {colorama.Fore.RESET}metatags {colorama.Fore.GREEN}list!')
    FoundCount += 1
else:
    print(f'{colorama.Fore.RED}Couldn\'t find {colorama.Fore.RESET}metatags {colorama.Fore.RED}list!')
checkDirTreeScripts = os.path.exists(os.path.join(os.getcwd(), 'config', 'scripts', 'default.json'))
if checkDirTreeScripts == True:
    print(f'{colorama.Fore.GREEN}Found {colorama.Fore.RESET}scripts {colorama.Fore.GREEN}list!')
    FoundCount += 1
else:
    print(f'{colorama.Fore.RED}Couldn\'t find {colorama.Fore.RESET}scripts {colorama.Fore.RED}list!')
checkDirTreeSidebar = os.path.exists(os.path.join(os.getcwd(), 'config', 'sidebar', 'default.json'))
if checkDirTreeSidebar == True:
    print(f'{colorama.Fore.GREEN}Found {colorama.Fore.RESET}sidebar {colorama.Fore.GREEN}config!')
    FoundCount += 1
else:
    print(f'{colorama.Fore.RED}Couldn\'t find {colorama.Fore.RESET}sidebar {colorama.Fore.RED}config!')
checkDirTreeStyles = os.path.exists(os.path.join(os.getcwd(), 'config', 'styles', 'default.json'))
if checkDirTreeStyles == True:
    print(f'{colorama.Fore.GREEN}Found {colorama.Fore.RESET}styles {colorama.Fore.GREEN}list!')
    FoundCount += 1
else:
    print(f'{colorama.Fore.RED}Couldn\'t find {colorama.Fore.RESET}styles {colorama.Fore.RED}list!')

if FoundCount != ConfigFilesCount:
    print(f'\n\n{colorama.Fore.RED}Found {colorama.Fore.RESET}{FoundCount}{colorama.Fore.RED} files, but expected to find {colorama.Fore.RESET}{ConfigFilesCount}{colorama.Fore.RED}. Please add the missing {colorama.Fore.RESET}{ConfigFilesCount -FoundCount}{colorama.Fore.RED} files, or {colorama.Fore.RESET}edit the python file{colorama.Fore.RED}.')
    exit(1)

print(colorama.Fore.RESET)
# Read configs and start generating the pages
def readConfig(type):
    if type == 'metatags':
        f = open(os.path.join(os.getcwd(), 'config', 'pages', 'metatags.json'), "r")
        configJson = f.read()
        f.close()
        config = json.loads(configJson)
        return config
    else:
        f = open(os.path.join(os.getcwd(), 'config', type, 'default.json'), "r")
        configJson = f.read()
        f.close()
        config = json.loads(configJson)
        return config

def generatePage(pagename):
    pagecontent = ""
    if readConfig('metatags')["addDoctype"] == "true":
        pagecontent += "<!DOCTYPE html>"
        pagecontent += f"\n<html lang=\"{readConfig('metatags')['lang']}\">"
        pagecontent += "\n<head>"
    pagecontent += f"\n<meta charset=\"{readConfig('metatags')['charset']}\">"
    pagecontent += f"\n<meta name=\"description\" content=\"{readConfig('metatags')['description']}\">"
    pagecontent += f"\n<meta name=\"keywords\" content=\"{readConfig('metatags')['keywords']}\">"
    pagecontent += f"\n<meta name=\"author\" content=\"{readConfig('metatags')['author']}\">"
    pagecontent += f"\n<meta name=\"viewport\" content=\"{readConfig('metatags')['viewport']}\">"
    if readConfig('styles')['headLink1'] != "":
        pagecontent += f"\n<link href=\"{readConfig('styles')['headLink1']}\" rel=\"stylesheet\" crossorigin=\"anonymous\">"
    if readConfig('styles')['headLink2'] != "":
        pagecontent += f"\n<link href=\"{readConfig('styles')['headLink2']}\" rel=\"stylesheet\" crossorigin=\"anonymous\">"
    if readConfig('styles')['headLink3'] != "":
        pagecontent += f"\n<link href=\"{readConfig('styles')['headLink3']}\" rel=\"stylesheet\" crossorigin=\"anonymous\">"
    if readConfig('styles')['headLink4'] != "":
        pagecontent += f"\n<link href=\"{readConfig('styles')['headLink4']}\" rel=\"stylesheet\" crossorigin=\"anonymous\">"
    if readConfig('styles')['headLink5'] != "":
        pagecontent += f"\n<link href=\"{readConfig('styles')['headLink5']}\" rel=\"stylesheet\" crossorigin=\"anonymous\">"
    pagecontent += f"\n<title>{readConfig('metatags')['title']}</title>"
    pagecontent += "\n</head>"
    pagecontent += f"\n<body style=\"{readConfig('metatags')['bodyCss']}\">\n"
    try:
        f = open(os.path.join(os.getcwd(), 'config', 'pages', f'{pagename}.vsml'), "r")
        pagecontent += f.read()
        f.close()
    except FileNotFoundError:
        print(f"{colorama.Fore.RED}VSML was unable to find the file {colorama.Fore.RESET}pages/{pagename}.vsml{colorama.Fore.RED}. Please check your {colorama.Fore.RESET}pages {colorama.Fore.RED}directory.")
        exit(1)
    if readConfig('scripts')['bodyScript1'] != "":
        pagecontent += f"\n<script src=\"{readConfig('scripts')['bodyScript1']}\" crossorigin=\"anonymous\"></script>"
    if readConfig('scripts')['bodyScript2'] != "":
        pagecontent += f"\n<script src=\"{readConfig('scripts')['bodyScript2']}\" crossorigin=\"anonymous\"></script>"
    if readConfig('scripts')['bodyScript3'] != "":
        pagecontent += f"\n<script src=\"{readConfig('scripts')['bodyScript3']}\" crossorigin=\"anonymous\"></script>"
    if readConfig('scripts')['bodyScript4'] != "":
        pagecontent += f"\n<script src=\"{readConfig('scripts')['bodyScript4']}\" crossorigin=\"anonymous\"></script>"
    if readConfig('scripts')['bodyScript5'] != "":
        pagecontent += f"\n<script src=\"{readConfig('scripts')['bodyScript5']}\" crossorigin=\"anonymous\"></script>"
    pagecontent += "\n</body>"
    pagecontent += "\n</html>"
    outFolderExists = os.path.exists(os.path.join(os.getcwd(), 'out', pagename))
    if outFolderExists == False:
        os.mkdir(os.path.join(os.getcwd(), 'out', pagename))
    f = open(os.path.join(os.getcwd(), 'out', pagename, 'index.html'), "w")
    f.write(pagecontent)
    f.close()
    return pagecontent








try:
    generatePage(arglist[1])
    print(f'{colorama.Fore.GREEN}VSML created the page {colorama.Fore.RESET}{arglist[1]}{colorama.Fore.GREEN} successfully!')
except IndexError:
    print(f'{colorama.Fore.RED}VSML needs the name of the page to create.')
    exit(1)