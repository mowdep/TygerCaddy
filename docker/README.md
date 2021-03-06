TygerCaddy Docker Container
===========================

This container aims to be easy to understand, easy to backup/restore, and easy to operate.

Any suggestions on improving this containers ease of use are welcome.

Running TygerCaddy
------------------

      docker run -d -p 80:80 -p 443:443 -p 9090:9090 --name tygercaddy \
        -v $PWD/data/config:/apps/TygerCaddy/TygerCaddy/data \
        -v $PWD/data/certs:/root/.caddy \
        morph1904/tygercaddy


Then point your browser to http://127.0.0.1/ and login with the provided credentials

Building TygerCaddy
-------------------

First clone the repo and cd to it

    docker build -t morph1904/tygercaddy docker/.

Building TygerCaddy as a developer
----------------------------------

First we need to clean any existing images:

    docker image rm $(docker images -aq)

Then build and tag the containers:

    docker build --build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
                 --build-arg VCS_REF=`git rev-parse --short HEAD` \
                 --build-arg VERSION=`cat VERSION.txt` \
                 -t morph1904/tygercaddy:latest \
                 -f docker/Dockerfile docker/.

Push the containers:

    docker push morph1904/tygercaddy:latest

Poll the stats counter to update:

    curl -X POST https://hooks.microbadger.com/images/morph1904/tygercaddy/H1IJ26NFLGCXubTEOCkGpWDam9Q\=
