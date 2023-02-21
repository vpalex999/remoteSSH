# remoteSSH
## Windows

01. Установить Python https://www.python.org/downloads/
02. Проверка версии Python
```
  py -V
```
03. Скачать файлы скрипта https://github.com/Serge-GHSHCH/remoteSSH локально, например в директорию ../remoteSSH
04. Открыть CMD (win+R)
05. Переместиться в нашу директорию remoteSSH
```
  cd ../remoteSSH
```
06. Создать локальный набор переменных окружения (после выполнения команды появится папка env)
```
  py -m venv env
```
07. Активировать локальный набор переменных окружения (после выполнения в командной строке видим (env))
```
  env\Scripts\activate.bat
```
08. Проверить работу менеджера пакетов (выведет список установленных пакетов и их версии)
```
  pip list
```
09. Установить необходимые модули, которые показаны в файле requirements.txt
```
  pip install -r requirements.txt
```
10. Получить SHA-ключи для будущих подключений.
	Для этого нужно подключиться по ssh к каждому из целевых серверов.
	Например, так:
```
  ssh root@38.242.233.94
```
11. Настроить наш скрипт.
	Открыть remote_ssh.py в редакоре.
	Для полей, показанных ниже задать соответствующие значения для подключения и выполнения команд, а за тем и сохранить:
	* username = 'логин'
	* password = 'пароль'
	* url = 'IP-адрес'
	* command_list = [список команд]
12. Запустить скрипт и дождаться его выполнения
```
  py remote_ssh.py
```

## Linux

  01  python -V
  02  python3 -V
  03  git
  04  pwd
  05  ls -la
  06  git clone https://github.com/Serge-GHSHCH/remoteSSH.git
  07  ls -la
  08  cd remoteSSH/
  09  python3 -m venv env
  10  sudo apt install python3.8-venv
  11  python3 -m venv env
  12  ls -la
  13  activate env/bin/activate
  14  source env/bin/activate
  15  pip list
  16  pip install -r requirements.txt
  17  mc
  18  python remote_ssh.py

 
