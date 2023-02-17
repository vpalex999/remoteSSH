import asyncio
import asyncssh
import sys


username = 'server1'
password = 'server1'

command_list = [
    "pwd",
    "ls -l",
    "echo server1 | sudo -S ls /root",
    "echo server1 | sudo -S systemctl status network-online.target",
    "mkdir test3",
    "mkdir test4",
    "pwd",
    "ls -l",
]

url = '192.168.200.7'


async def run_client(command: str) -> None:
    async with asyncssh.connect(url, password=password, username=username) as conn:
        result = await conn.run(command, check=True)

        if result.exit_status == 0:
            print(result.stdout, end='')
        else:
            print(result.stderr, end='', file=sys.stderr)
            print(f'Program exited with status {result.exit_status}',
                  file=sys.stderr)


try:
    for command in command_list:
        asyncio.get_event_loop().run_until_complete(run_client(command))
except (OSError) as exc:
    sys.exit('SSH connection failed: ' + str(exc))
except (asyncssh.Error) as err:
    sys.exit('SSH command failed: ' + err.stderr)
