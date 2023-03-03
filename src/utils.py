

def sudo_convert(command: str, user_password: str) -> str:
    """ Конвертирует команду 'sudo' в формат с подстановкой пароля."""
    return command.replace("sudo", f"echo {user_password} | sudo -S")
