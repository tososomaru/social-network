#!/bin/sh
#heroku container:push web
#heroku container:release web
#heroku open
docker buildx build --platform linux/amd64 -t app .
docker tag app registry.heroku.com/intense-fjord-98232/web
docker push registry.heroku.com/intense-fjord-98232/web
heroku container:release web -a intense-fjord-98232