# import_into_pass
This little python script helps you to migrate from browser-integrated password managers to pass the standard unix password manager.

1. Export saved passwords:
- Chrome: https://support.google.com/chrome/answer/95606?hl=en&ref_topic=7438325&sjid=7360092539830032143-EU#zippy=%2Cshow-edit-delete-or-export-saved-passwords
- Firefox: https://support.mozilla.org/en-US/kb/export-login-data-firefox

2. Initialize **pass**:
https://www.passwordstore.org/

3. Run this script
   
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
Import from *passwords.csv*, prompting before overwriting if a password-name already exists:
```console
foo@bar:~$ python import_into_pass.py passwords.csv
An entry already exists for 192.168.0.1. Overwrite it? [y/N] y
Add given password for interaction.7pass.de to store.
 1 file changed, 0 insertions(+), 0 deletions(-)
 rewrite 192.168.0.1.gpg (100%)
```
Import from *folder/passwords.csv*, silently overwriting existing passwords:
```console
foo@bar:~$ python import_into_pass.py -f folder/passwords.csv
Add given password for interaction.7pass.de to store.
 1 file changed, 0 insertions(+), 0 deletions(-)
 rewrite 192.168.0.1.gpg (100%)
```
