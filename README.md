# Requirements

Docker 28.1.4

# How to run

1. docker-compose up -d
2. visit http://127.0.0.1:8080/get (this will get some data from an api)
3. visit http://127.0.0.1:8080/view (this will show the first 10 results)

# docker commands

`docker-compose up -d` this runs all the listed containers in `docker-compose.yml`

`docker-compose stop` this just stops containers but doesn't remove them

`docker-down` this cleans up everything created by "up"

# VSCode intellisense

To maintain consistent extensions (and to prevent repeated installations), make sure extension installations are done into "devcontainer.json"

"Dev Containers" is also a necessary local extension installation in order to access the container data (and sync)

# Windows docker (known problems)

If vmmem starts taking up unreasonable amounts of CPU, close docker then run `wsl --shutdown` in powershell to remove it. 

# volume notes

Bind mounting REPLACES whatever is inside the container's destination with your local files, thus if any files are created inside the destination during the build, it will be replaced by local files (even deleted)
