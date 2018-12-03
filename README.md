# iReporter
web application  

[![Coverage Status](https://coveralls.io/repos/github/waihigakanini/iReporter/badge.svg?branch=ft-edit-redflag-%23162297465)](https://coveralls.io/github/waihigakanini/iReporter?branch=ft-edit-redflag-%23162297465)
[![Build Status](https://travis-ci.org/waihigakanini/iReporter.svg?branch=ft-edit-redflag-%23162297465)](https://travis-ci.org/waihigakanini/iReporter) [![Maintainability](https://api.codeclimate.com/v1/badges/4cf68f45754d4bafa352/maintainability)](https://codeclimate.com/github/waihigakanini/iReporter/maintainability)

### Project Overview
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

### TECH/FRAMEWORK USED
- Python
- HTML
- CSS
- Flask
- Postgres
- Javascript

### FEATURES AND ENDPOINTS

|Resource urls                                    | Method     | Description               |
|-------------------------------------------------|------------|---------------------------|
| /api/v1/incident                                |   POST     | Create an Incident        |
| /api/v1/incident                                |   GET      | Get all incidences        |
| /api/v1/incident/id                             |   GET      | Get an Incident by Id     |
| /api/v1/incident/id                             |   DELETE   | Delete an incident        |
| /api/v1/incident/id/comments                    |   PATCH    | Edit an incident comment  |
| /api/v1/incident/id/location                    |   PATCH    | Edit an incident location |
| /api/v1/auth/signup                             |   POST     | Signup a user             |
| /api/v1/auth/login                              |   POST     | Login a user              |
| /api/v1/auth/logout                             |   POST     | Sigout a user             |


### INSTALLATION
- Create the directory where you want to clone the repository.(iReporter)
- Move into that directory and clone the repository as shown in the process below
    - mkdir repository
    - cd into the repository(in our case the iReporter repository)
    - git clone the repository url (https://github.com/waihigakanini/iReporter.git)
#### Step 1
   - python3 -m venv ireporter
   - source ireporter/bin/activate (to activate virtual env)
   - pip install -r requirements.txt (install app dependencies)
### Step 2. run the app
   - To start the app run the command below
   - python run.py
   - Test the endpoints in the next section with Postman

### TESTS
- To test the app run the command below
- py.test --cov=app test/ (to test and give coverage)
- You should see an image like below alt Tests image

![screenshot from 2018-12-03 19-33-17](https://user-images.githubusercontent.com/45232680/49396790-08614380-f74b-11e8-98f1-a7386325835d.png)

### Hosting
This app is hosted at Heroku 
https://dashboard.heroku.com/apps/infinite-meadow-22437/deploy/github

### OWNER

This app was built by Loise waihiga Kanini 




