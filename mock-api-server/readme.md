### DESCRIPTION
mock-api-server has 2 flask apps running simultaneously but separately.  
It means when you change something (like variables) via http request you won't see changes via https request and vice versa.  
But file sharing on the system works for both

### BUILD
```
docker-compose build
```
If you made any changes to api-mock service - rebuild it with the same above cmd

### RUN EVERYTHING
```
docker-compose up -d
```

### RUN TESTS
```
docker-compose run tests
```

### RUN INFINITE FOR DEBUG/PLAY
Replace entrypoint on tests service to infinite loop
```
docker-compose up -d
```

### CONNECT TO RUNNING DB
```
docker exec -it mock-db-server psql -U user -d mockdb
```

### SHUTDOWN
```
docker-compose down
```

### CHECK LOGS
```
docker logs YOUR_CONTAINER_NAME
or
docker logs YOUR_CONTAINER_ID
```

