Constant Demo Site

To run:

docker-compose up -d --build

docker-compose exec api python manage.py run_tests

http://localhost:1337

http://localhost:1337/api

docker-compose down -v


Notes:

- loans file contains a duplicate primary, 25, and is missing the key 24.  assumed it was a typo error, not an actual challenge, and changed the entry aftr 23 to 24.  if this was real world, would have to discuss data with db or biz owners, but primary keys should not be pre-determined in any case.

- requirements show the endpoint /loans/<lender_id> with no trailing slash.  Implementing with trailing slash.


