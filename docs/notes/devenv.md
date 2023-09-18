## Development environment

### Min
- [x] venv
    ```bash
    sudo apt install python3-venv python3-mysqldb
    python3 -m venv --system-site-packages --symlinks --clear --upgrade-deps .venv # --upgrade
    source .venv/bin/activate
    pip install --require-virtualenv --requirement requirements.txt
    ```

- [x] MySQL
    #### with ubuntu/debian
    ```bash
    sudo apt install mysql-server
    sudo /etc/init.d/mysql start # status
    sudo mysql
    ```
    #### with podman/docker (when data dir exists already)
    ```bash
    podman run --name orspytheng_mysql --volume .mysql:/var/lib/mysql --publish 127.0.0.1:3306:3306 --detach mysql:8.1
    ```
    ```mysql
    CREATE DATABASE orspytheng_development CHARACTER SET utf8;
    CREATE USER 'orspytheng_app' IDENTIFIED BY 'orspytheng_pass';
    GRANT ALL PRIVILEGES ON `orspytheng\_%` .  * TO 'orspytheng_app'@'%';
    FLUSH PRIVILEGES;
    exit
    ```
    ```bash
    ./manage.py migrate
    ```

### Backlog
- [ ] cloud dev env (GH codespaces?)
- [ ] vscode config / devcontainer / workspace
- [ ] podman/docker-compose for local env
- [ ] cache server
- [ ] reverse proxy server
