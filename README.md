# build

docker build -t de_pdm .

# run and otherwise

docker-compose up -d

docker-compose stop # this just stops containers but doesn't remove them

# clean up

docker-compose down # cleans up everything created by the compose

# VSCode intellisense

install "Dev Containers"

# Windows docker

If vmmem starts taking up unreasonable amounts of CPU, close docker then run `wsl --shutdown` in powershell to remove it. 

# volume notes

Bind mounting REPLACES whatever is inside the container's destination with your local files, thus if any files are created inside the destination during the build, it will be replaced by local files (even deleted)
