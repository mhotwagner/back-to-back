### BACK-TO-BACK

##### Python/Django Backend for Backstage Code Screen

#### Quickstart
*Assumes psql, pyenv, pip, virtualenv, and virtualenvwrapper installed.*

Clone the Repo, setup the virtualenv and install requirements
```
$ git clone git@github.com/mhotwagner/back-to-back
$ mkvirtualenv back-to-back -p $(pyenv which python3)
$ pip install -r requirements.txt
```

Make your local database and migrate the app
```
$ createdb back-to-back-local
$ make migrate
```

### Run tests
`make test`


