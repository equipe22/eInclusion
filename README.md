# eInclusion web app and REDCap Hook

eInclusion aims at making possible to display private information (first name, last name, date of birth, identifier)  without storing these information in REDCap.

eInclusion is designed as a data base with an API, and two user interface :
* A REDCap hook
* A web application

The code is organized in 3 folders :
* Hook: php files for the REDCap hook
* Backend: SQL script for the creation of the database and python3 flask API
* Frontend: python3 flask application

## TODO

eInclusion is a ongoing work, many functionalities are still needed:
### Critical:
* Securing the communication between interfaces and the backend using JWT
* adding the login page using LDAP on the web app
* adding access control to user allowed

### Optional:
* add data through the web app
