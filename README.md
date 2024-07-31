# import_into_pass
This little python script helps you to migrate from browser-integrated password managers to pass the standard unix password manager.

### Usage:
```shell
python import_into_pass.py [-h] [-f] FILENAME
```

Import password file into **pass**, the standard unix password manager.

### Positional arguments:
- *FILENAME*: filename of password-file


### Options:
-   -h, --help:   show help message and exit
-   -f, --force:  overwrite existing passwords without asking

### Example:
Import from *passwords.csv*, prompting before overwriting if the password-name already exists:
```console
foo@bar:~$ python import_into_pass.py passwords.csv
An entry already exists for 192.168.0.1. Overwrite it? [y/N] y
Add given password for interaction.7pass.de to store.
 1 file changed, 0 insertions(+), 0 deletions(-)
 rewrite i192.168.0.1.gpg (100%)
```
Import from *folder/passwords.csv*, silently overwriting existing passwords:
```console
foo@bar:~$ python import_into_pass.py -f folder/passwords.csv
Add given password for interaction.7pass.de to store.
 1 file changed, 0 insertions(+), 0 deletions(-)
 rewrite i192.168.0.1.gpg (100%)
```
