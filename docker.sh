docker pull postgres;
docker run -p 5432:5432 -e POSTGRES_USER=postgres-user -e POSTGRES_PASSWORD=password -d -v my-postgres-data:/var/lib/postgresql/data --name custom-name postgres:latest;
docker run -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=some@gmail.com -e PGADMIN_DEFAULT_PASSWORD=somepassword -v my-data:/var/lib/pgadmin -d dpage/pgadmin4
