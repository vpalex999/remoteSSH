"""
Usage:
    remote_ssh config <filename>

Options:
    <filename>      the configuration file (*.yaml)
"""
import asyncio
from typing import Any, Dict, List
import asyncssh
import sys
from docopt import docopt

from src.config import Config
from src.utils import sudo_convert


async def echo_node(node_config: Dict[str, Any], commands: List[str]) -> None:
    url = node_config["url"]
    username = node_config["username"]
    password = node_config["password"]

    async with asyncssh.connect(
            url, password=password, username=username) as conn:
        for command in commands:
            result = await conn.run(sudo_convert(command, password), check=True)

            if result.exit_status == 0:
                print(
                    f"node {url} command '{command}':\n{result.stdout}")
            else:
                print(f"node {url}: {result.stderr}",
                      end='', file=sys.stderr)
                print(f"node {url}: Program exited with status {result.exit_status}",
                      file=sys.stderr)


async def main() -> None:
    arguments = docopt(__doc__)  # type: ignore
    print(arguments)

    if arguments.get('config'):
        config = Config.from_file(arguments["<filename>"])
        print(str(config))

        echo_tasks: List[asyncio.Task] = []

        for node in config.nodes:
            echo_tasks.append(asyncio.create_task(
                echo_node(node, config.commands)))

        [await task for task in echo_tasks]

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (OSError) as exc:
        sys.exit('SSH connection failed: ' + str(exc))
    except (asyncssh.Error) as err:
        sys.exit('SSH command failed: ' + str(err))
