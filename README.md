## Environment Setup

- Create virtualenv in the project directory, so that you can find 
the project and its virtualenv in a single place.

## Packages
- python 3.5.1
- flask
- python-dotenv
- flask-wtf
- flask-sqlalchemy
- flask-migrate


## Tips
- Sometimes mac python behaing strangely. if `flask run` not loading microblog package but all good skelton and code then try as `python3 -m flask run` command. 
- If environment is codenvy then enable SSH Port forwarding to access localbrowser to see the changes 
```ssh -L 5000:localhost:5000 -p 39912 -i key user@node13.codenvy.io```
