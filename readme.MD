# idea here
* play around with fastapi and other trending python technologies

### try out fast-api with regular web develop ideas
- basic endpoints (create and fetch)
- background flows (quotes update)
- 

# how to run app
- manually: `ENV=dev fastapi dev main` (db is available on docker as well)
- docker: ```docker compose up --no-deps --watch``` **

# how to run tests (tests connect to db as well)
- `cd tests`
- `PYTHONPATH=.. pytest`


# TODO
- it seems server & mongo arent running together inside docker (cant connect and get to timeout)