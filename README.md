# import_into_pass
This little python script helps you to migrate from browser-integrated password managers to pass the standard unix password manager.

usage: python import_into_pass.py [-h] [-f] filename

Import password file into **pass**, the standard unix password manager.

positional arguments:
  filename     Filename of password-file

options:
  -h, --help   show this help message and exit
  -f, --force  Overwrite existing passwords without asking

# Example:
Import from passwords.csv
```shell
python import_into_pass.py passwords.csv
```
Import from folder/passwords.csv, overwriting existing passwords
```shell
python import_into_pass.py -f folder/passwords.csv
```
