import asyncio
import asyncssh
import sys

url = '192.168.200.7'
username = 'root'
password = 'pass'

command_list = [
    "echo [pass] | sudo -S systemctl stop ziesha",
    "cd $HOME/bazuka && git pull origin master && cargo update && cargo install --path .",
    "echo [pass] | sudo -S systemctl restart ziesha",
    "echo [pass] | sudo -S systemctl status ziesha",
    "echo [pass] | sudo -S journalctl -u ziesha",
]



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
    sys.exit('SSH command failed: ' + str(err))
