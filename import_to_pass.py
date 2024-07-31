import argparse
import subprocess
import textwrap
from typing import List



def import_password(url : str, username : str, password : str, force=False) -> None:
    """Imports passwords to pass.
    
    Uses 'url/username' as password-name, where 'url' the input url stripped from prefixes.
    force=False (default): Asks if you want to change the password, if an entry already exists.
    force=True: Changes passwords, if entry already exists.
    """  
    password_name = prepare_passname(url, username)
    if not force:
        if find_passname(password_name):
            print(f"An entry already exists for {password_name}. Overwrite it? [y/N]", end=" ")
            if input() != "y":
                return
     
    command = [f"pass insert --echo -f {password_name}"]
    
    process = subprocess.Popen(
        command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    stdout, stderr = process.communicate(input=f"{password}\n")
    print(f"{stdout}{stderr}")
    
    return


def find_passname(passname : str) -> bool:
    """Returns True if "passname" exists in password store
    """ 
    if "/" in passname:
        passname = passname.split("/")
        command = [f"pass ls {passname[0]+"/"}"]
        passname = passname[1]
    else:
        command = [f"pass find {passname}"]
        
    tree = subprocess.getoutput(command)

    return tree.find("─ " + passname) != -1
    
    
def prepare_passname(url : str, username : str) -> str:
    """Returns "url/username" if "username" exists, else "url".
    "url" gets stripped from prefixes like "https://www."
    """
    password_name = url.removeprefix("https://").removeprefix("http://").removeprefix("www.")
    if username:
        password_name += "/" + username
    return password_name


def read_csv(fname: str) -> tuple[List[str], List[str]]:
    """Parse csv-file given by filename fname.
    
    Returns tuple (header, data) consisting of lists of str."""
    
    with open(fname) as f:
        data = []; row = []; header = []
        rawheader = f.readline().split(",")
        for item in rawheader:
            header.append(item.rstrip("\n").strip('"'))
        
        item = ""
        escaped = False
        byte = f.read(1)
        while byte:
            if not escaped:
                if byte == '\n':
                    row.append(item)
                    item = ""
                    data.append(row)
                    row = []
                    byte = f.read(1)
                    continue
                if byte == '"':
                    escaped = True
                    byte = f.read(1)
                    continue
                if byte == ',':
                    row.append(item)
                    item = ""
                    byte = f.read(1)
                    continue
            elif escaped:
                if byte == '"':
                    byte = f.read(1)
                    if byte != '"':
                        escaped = False
                        continue
            
                item += byte
            byte = f.read(1)
        return (header, data)


def main(args):
    # Parse csv
    try:
        header, data = read_csv(args.filename)
    except FileNotFoundError:
        print(f"No such file or directory: {args.filename}")
        return
    except:
        print("Could not parse csv-file")
        return

    # Get header indices
    for index, item in enumerate(header):
        if item == "username":
            USER = index
        if item == "password":
            PASS = index
        if item == "url":
            URL = index

    # Import passwords
    for row in data:
        import_password(row[URL], row[USER], row[PASS], force=args.force)


def bold(s : str) -> str:
    return f"\033[1m{s}\033[0m"
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f'Import password file to {bold('pass')}, the standard unix password manager.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            f'''Example:
            Import from passwords.csv
            \t{bold("import_to_pass.py passwords.csv")}
            Import from folder/passwords.csv, overwriting existing passwords
            \t{bold("import_to_pass.py -f folder/passwords.csv")}
            ''')
    )
    parser.add_argument('-f', '--force',
                        action='store_true', help='Overwrite existing passwords without asking')
    parser.add_argument('filename', help='Filename of password-file')
    args = parser.parse_args()
    main(args)
   