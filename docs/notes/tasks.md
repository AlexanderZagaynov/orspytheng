## Tasks
- [ ] stop polish notes at what is min

### DB schema / Models
- [x] MermaidJS: `./docs/erd.md`
- [x] storable and readable as text
- [x] renderable by available OSS tools

### Design routes & API
- [ ] think about versioning
- [ ] do not forget about healthchecks


### Enlist features to implement

#### Cars
- [x] list cars
- [x] add new car
- [ ] update car
- [ ] remove car

#### Reservations
- [ ] see cars availability
- [ ] reserve the car
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
- [ ] admin user
    ```bash
    ./manage.py createsuperuser
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
