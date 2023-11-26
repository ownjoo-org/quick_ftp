# quick_ftp
### help
```
$ python3 main.py --help
usage: main.py [-h] [--username USERNAME] [--password PASSWORD] --host HOST [--get] [--put] --local_file LOCAL_FILE --remote_file REMOTE_FILE

options:
  -h, --help            show this help message and exit
  --username USERNAME   The username to use for authentication
  --password PASSWORD   The password for the username
  --host HOST           The host to connect to: FQDN or IP
  --get                 Get file
  --put                 Put file
  --local_file LOCAL_FILE
                        path to local file
  --remote_file REMOTE_FILE
                        path to remote file
```

### example
```
python3 main.py --username alice --password "Alice'sPassword" --host ftp.example.com --get --local_file example.txt 
--remote_file example.txt
```
