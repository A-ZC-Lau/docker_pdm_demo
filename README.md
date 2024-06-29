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
