## Development environment

### Min
- [ ] venv
    ```
    sudo apt install python3-venv python3-django python3-mysqldb
    python3 -m venv --system-site-packages --symlinks --clear --upgrade-deps .venv # --upgrade
    source .venv/bin/activate
    pip install graphene_django
    ```

- [ ] MySQL
    ```bash
    sudo apt install mysql-server
    sudo /etc/init.d/mysql start # status
    sudo mysql
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




## Tools and libraries to use

### Language
- [x] Python 3.10 (latest)

### Framework
- [x] Django 4.2 (latest)

### Tests
- [x] Django [defaults](https://docs.djangoproject.com/en/4.2/topics/testing/)

### Database
- [x] MySQL Community 8.1.0

### API
- [ ] GraphGL
- [ ] Autodocument in OpenAPI format (if applicable)

### Caching
- [x] [Dummy (dev min)](https://docs.djangoproject.com/en/4.2/topics/cache/#dummy-caching-for-development)
- [ ] Memcached for DB reads
- [ ] Redis for metrics

### Development
- [ ] git (min?)

### Build & CI
- [ ] docker or podman
- [x] GitHub Actions
- [ ] codestyle?
- [ ] linting?

### OPS
- [ ] provisioning?
- [ ] bot/chatops?




## Tasks
- [ ] stop polish notes at what is min

### DB schema / Models
- [ ] use something like mermaid / Plant UML
- [ ] storable and readable as text
- [ ] renderable by available OSS tools

### Design routes & API
- [ ] think about versioning
- [ ] do not forget about healthchecks

### Enlist features to implement
- [ ] add new car
- [ ] update car
- [ ] remove car
- [ ] list cars
- [ ] check availability and reserve the car
- [ ] see cars availability
- [ ] see (upcoming) car reservations

### Establish minimal dev env
- [x] prepare environment
- [x] init the app
    ```
    django-admin startproject api .
    ./manage.py startapp cars
    ```
- [x] run blank app
    ```
    ./manage.py runserver
    ```
- [ ] run empty tests

### Prepare database
- [x] create db(s)
- [x] database connection
- [ ] models
- [ ] migrations
    ```bash
    ./manage.py makemigrations
    ./manage.py migrate
    ```
- [ ] seeds
    ```bash
    ./manage.py loaddata cars
    ```
    see the `cars/fixtures/cars.json` file

### Run API server
- [x] `/graphql` for cars

### Develop test cases
- [ ] unit tests
- [ ] API calls

#### Backlog
- [ ] linting
- [ ] coverage
- [ ] think about long-running, performance & scaleability tests

### Develop features
- [ ] minimal
- [ ] bonus

### Establish CI
- [ ] GitHub Actions

### Documentation
- [ ] generate API docs
- [ ] dev env provisioning
- [ ] project presentation

### Develop extra features
- [ ] finalize notes
- [ ] groom and complete backlogs



## Project conventions


### Directories layout

- [ ] `./app-api-django` django app & its default layout
- [ ] docs

#### Tooling / scripts
- [ ] dev env provisioning
- [ ] app build (container image)
- [ ] CI settings

##### Backlog: other scripts and configs
- [ ] infra with tf + azure
- [ ] stage/prod envs
- [ ] maintenance

### Documentation
- [ ] what to document
- [ ] how to document


### Configuration
- [ ] min: `ENV`

#### Backlog
- [ ] to be able to update dynamically
- [ ] configurations service (server)


### Secrets
- [ ] min: `.env`-alike

#### Backlog
- [ ] to be able to update dynamically
- [ ] secrets service (server)


### Logging
- [ ] what to log with `DEBUG`
- [ ] what to log with `INFO`
- [ ] (best practices) mandatory logging of all catched errors

#### Backlog
- [ ] errbit-alike errors server
- [ ] logs aggregation server & agent(s)

### Performance metrics
- [ ] what to count
- [ ] how to collect
- [ ] how to expose

### Caching strategy
- [ ] GraphQL caching specifics?
- [ ] can use [template fragment caching](https://docs.djangoproject.com/en/4.2/topics/cache/#template-fragment-caching)?

### Development

- [ ] coding standarts
- [ ] naming conventions
- [ ] [Commenting Showing Intent [CSI]](https://standards.mousepawmedia.com/en/latest/csi.html)

### Releases
- [ ] versioning
- [ ] branching
- [ ] backporting

### Tasks & Issues management
- [ ] use github issues & other GH features?
