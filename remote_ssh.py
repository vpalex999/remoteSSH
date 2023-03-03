"""
Usage:
    remote_ssh config <filename>

Options:
    <filename>      the configuration file (*.yaml)
"""
import asyncio
import asyncssh
import sys
from docopt import docopt

from src.config import Config
from src.utils import sudo_convert


async def run_client(config: Config) -> None:
    nodes = config.nodes
    commands = config.commands
    if len(nodes) > 0:
        for node in nodes:
            url = node["url"]
            username = node["username"]
            password = node["password"]

            for command in commands:
                async with asyncssh.connect(
                        url, password=password, username=username) as conn:
                    result = await conn.run(sudo_convert(command, password), check=True)

                    if result.exit_status == 0:
                        print(f"node {url} command '{command}':\n{result.stdout}")
                    else:
                        print(f"node {url}: {result.stderr}",
                              end='', file=sys.stderr)
                        print(f"node {url}: Program exited with status {result.exit_status}",
                              file=sys.stderr)


if __name__ == "__main__":
    arguments = docopt(__doc__)  # type: ignore
    print(arguments)

    if arguments.get('config'):
        config = Config.from_file(arguments["<filename>"])
        print(str(config))

        try:
            asyncio.run(run_client(config))
        except (OSError) as exc:
            sys.exit('SSH connection failed: ' + str(exc))
        except (asyncssh.Error) as err:
            sys.exit('SSH command failed: ' + str(err))
