# import_to_pass
This little python script helps you to migrate from browser-integrated password managers to pass the standard unix password manager.

usage: python import_to_pass.py [-h] [-f] filename

Import password file to **pass**, the standard unix password manager.

positional arguments:
  filename     Filename of password-file

options:
  -h, --help   show this help message and exit
  -f, --force  Overwrite existing passwords without asking

# Example:
Import from passwords.csv
```import_to_pass.py passwords.csv```
Import from folder/passwords.csv, overwriting existing passwords
`import_to_pass.py -f folder/passwords.csv`
