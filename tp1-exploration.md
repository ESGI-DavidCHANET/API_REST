# API_REST -- TP1
## 1 ##

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>docker run -d --name web1 --label adminapi.managed=true nginx:alpine
830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>docker run -d --name intrus nginx:alpine
e570fb9ea4a1c9157e9fe518840e1bb5959ca9a3c14133592730dddb024f6b20

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
e570fb9ea4a1   nginx:alpine   "/docker-entrypoint.…"   17 seconds ago   Up 16 seconds   80/tcp    intrus
830fcda23bef   nginx:alpine   "/docker-entrypoint.…"   18 seconds ago   Up 18 seconds   80/tcp    web1
