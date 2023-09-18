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
- [x] update car
- [x] remove car

#### Reservations
- [ ] reserve the car
- [ ] see reservations
- [ ] reservation validator
- [ ] filter by car
- [ ] filter upcoming / by period


### Establish minimal dev env
- [x] prepare environment
- [x] init the app
    ```bash
    django-admin startproject api .
    ./manage.py startapp cars
    ./manage.py startapp reservations
    ```
- [x] run blank app
    ```bash
    ./manage.py runserver
    ```
- [x] run empty tests
    ```bash
    ./manage.py test
    ```

### Prepare database
- [x] create db(s)
- [x] database connection
- [x] admin user
    ```bash
    ./manage.py createsuperuser
    ```
- [x] models: `Car`
- [x] models: `Reservation`
- [x] migrations
    ```bash
    ./manage.py makemigrations
    ./manage.py migrate # migrate <app> zero
    ```
- [x] seeds
    ```bash
    ./manage.py loaddata cars
    ./manage.py loaddata reservations
    ```
    see the `<app>/fixtures/<data>.json` file

### Run API server
- [x] `/graphql` for cars

### Develop test cases
- [x] unit tests
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
- [ ] document methods / autogenerate docs

### Develop extra features
- [ ] finalize notes
- [ ] groom and complete backlogs
