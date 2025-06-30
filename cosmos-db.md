# emulator for cosmos db
1. Run a new container using the container image and the following configuration:
docker run \
    --publish 8081:8081 \
    --publish 10250-10255:10250-10255 \
    --name azure-cosmos-emulator \
    --detach \
    mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest

2. Navigate to https://localhost:8081/_explorer/index.html to access the data explorer.
