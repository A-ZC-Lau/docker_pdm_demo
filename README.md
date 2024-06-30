# build

docker build -t de_pdm .

# run and otherwise

docker run --name de_pdm_container -p 8080:8080 -dt -v .:/app de_pdm

docker stop de_pdm_container

docker rm de_pdm_container

# VSCode intellisense

install "Dev Containers"

# Windows docker

If vmmem starts taking up unreasonable amounts of CPU, close docker then run `wsl --shutdown` in powershell to remove it. 

# volume notes

Bind mounting REPLACES whatever is inside the container's destination with your local files, thus if any files are created inside the destination during the build, it will be replaced by local files (even deleted)
