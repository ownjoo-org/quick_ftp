from argparse import ArgumentParser
from ftplib import FTP


def main(
        host: str,
        method: str,
        local_file: str,
        remote_file: str,
        username: str = None,
        password: str = None,
) -> None:
    ftp = FTP(host)
    ftp.encoding = 'utf-8'
    ftp.login(user=username, passwd=password)
    if method == 'get':
        with open(local_file, 'wb') as file:
            ftp.retrbinary(f'RETR {remote_file}', file.write)
    if method == 'put':
        with open(local_file, 'rb') as file:
            ftp.storbinary(f'STOR {remote_file}', file)
    ftp.dir()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--username',
        default=None,
        type=str,
        required=False,
        help='The username to use for authentication',
    )
    parser.add_argument(
        '--password',
        default=None,
        type=str,
        required=False,
        help='The password for the username',
    )
    parser.add_argument(
        '--host',
        default=None,
        type=str,
        required=True,
        help='The host to connect to: FQDN or IP',
    )
    parser.add_argument(
        '--get',
        action='store_true',
        default=False,
        required=False,
        help="Get file",
    )
    parser.add_argument(
        '--put',
        action='store_true',
        default=False,
        required=False,
        help="Put file",
    )
    parser.add_argument(
        '--local_file',
        default=None,
        type=str,
        required=True,
        help="path to local file"
    )
    parser.add_argument(
        '--remote_file',
        default=None,
        type=str,
        required=True,
        help="path to remote file"
    )
    args = parser.parse_args()

    host: str = args.host
    username: None | str = None
    password: None | str = None
    local_file: str = args.local_file
    remote_file: str = args.remote_file
    method: None | str = None
    try:
        if not method:
            method = 'get' if args.get else None
    except Exception:
        pass
    try:
        if not method:
            method = 'put' if args.put else None
    except Exception:
        pass
    if not method:
        raise ValueError(f'please specify either --get or --put')
    try:
        username = args.username
        password = args.password
    except Exception as exc_parse_creds:
        print(f'Credentials not parsed: continuing anonymously...')

    main(
        host=host,
        method=method,
        local_file=local_file,
        remote_file=remote_file,
        username=username,
        password=password,
    )
