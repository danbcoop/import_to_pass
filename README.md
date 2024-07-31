# import_into_pass
This little python script helps you to migrate from browser-integrated password managers to pass the standard unix password manager.

### Usage:
```python import_into_pass.py [-h] [-f] FILENAME```

Import password file into **pass**, the standard unix password manager.

### Positional arguments:
- *FILENAME*: filename of password-file


### Options:
-   -h, --help:   show help message and exit
-   -f, --force:  overwrite existing passwords without asking

### Example:
Import from passwords.csv
```shell
python import_into_pass.py passwords.csv
```
Import from folder/passwords.csv, overwriting existing passwords
```shell
python import_into_pass.py -f folder/passwords.csv
```
