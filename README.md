### BACK-TO-BACK

##### Python/Django Backend for Backstage Code Screen

This app serves as Michael Hotwagner's submission to the code screen for Backstage.
The problem definition this code solves can be found [here](problem.txt) 

#### Quickstart
*Assumes psql, pyenv, pip, virtualenv, and virtualenvwrapper installed.*

Clone the Repo, setup the virtualenv and install requirements
```
git clone git@github.com/mhotwagner/back-to-back
mkvirtualenv back-to-back -p $(pyenv which python3)
workon back-to-back
pip install -r requirements.txt
```

Make your local database and migrate the app
```
createdb back-to-back-local
make migrate
```

Run the local server
```
make start
```

Go get your calculation!
`http://localhost:8000/calculate/?number=100`

### Run tests
`make test`


