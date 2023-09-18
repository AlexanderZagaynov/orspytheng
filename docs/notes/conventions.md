## Project conventions


### Directories layout

- [ ] `./api` django project & its default layout
- [ ] `./cars` django app & its default layout
- [ ] `./reservations` django app & its default layout
- [ ] `./docs` **TBD**

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
    ```python
    def some_function():
        """
        _summary_

        Args:
            value (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return something
    ```


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
