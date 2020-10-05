docker stop museumwarehouse_mysql-target_1
docker rm museumwarehouse_mysql-target_1
docker volume prune -f
docker image rm museumwarehouse_mysql-target