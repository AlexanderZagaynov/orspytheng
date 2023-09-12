## Development environment

### Min
- venv (`python -m venv --system-site-packages --symlinks --upgrade --upgrade-deps .venv`)
- MySQL (`apt install mysql-server`)

### Backlog
- cloud dev env
- vscode config / devcontainer / workspace
- podman/docker-compose for local env
- cache server
- reverse proxy server


## Tools and libraries to use

### Language
- Python 3.10 (latest)

### Framework
- Django 4.2 (latest)

### Tests
- Django [defaults](https://docs.djangoproject.com/en/4.2/topics/testing/)

### Database
- MySQL Community 8.1.0

### API
- Use GraphGL
- Autodocument in OpenAPI format (if applicable)

### Caching
- [Dummy (dev min)](https://docs.djangoproject.com/en/4.2/topics/cache/#dummy-caching-for-development)
- Memcached for DB reads
- Redis for metrics

### Development
-

### Build
-

### CI
-

### OPS
-


## Tasks

### DB schema / Model relations
- use something like mermaid / Plant UML
- storable and readable as text
- renderable by available OSS tools

### Design routes & API
- think about versioning
- do not forget about healthchecks

### Define test cases
- enlist features to test

### Establish minimal dev env
- prepare environment
- database connection
- run blank app
- run empty tests

### Develop test cases
- unit tests
- API calls

#### Backlog
- think about long-running & performance tests
- linting
- coverage


## Project conventions


### Directories layout

[x] `./app-api-django` django app & its default layout

[ ] docs

#### Tooling / scripts
[] dev env provisioning
- app build (container image)
- CI settings

##### Backlog: other scripts and configs
- infra with tf + azure
- stage/prod envs
- maintenance

### Documentation
- what to document
- how to document


### Configuration
- min: `ENV`

#### Backlog
- to be able to update dynamically
- configurations service (server)


### Secrets
- min: `.env`-alike

#### Backlog
- to be able to update dynamically
- secrets service (server)


### Logging
- what to log with `DEBUG`
- what to log with `INFO`
- (best practices) mandatory logging of all catched errors

#### Backlog
- errbit-alike errors server
- logs aggregation server & agent(s)

### Performance metrics
- what to count
- how to collect
- how to expose

### Caching strategy
- GraphQL caching specifics?
- can use [template fragment caching](https://docs.djangoproject.com/en/4.2/topics/cache/#template-fragment-caching)?

### Development

- coding standarts
- naming conventions
- [Commenting Showing Intent [CSI]](https://standards.mousepawmedia.com/en/latest/csi.html)

### Releases
- versioning
- branching
- backporting

### Tasks & Issues management
- use github issues & other GH features?
