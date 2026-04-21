# 先建一个数据目录，防止数据丢失
1. mkdir -p ~/docker-data/postgres

# 启动 PostgreSQL 容器（带持久化数据，删容器也不会丢数据）
2. docker run -d \
  --name llmops-postgres \
  --restart=always \
  -p 5432:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=mydevpass123 \
  -e POSTGRES_DB=devdb \
  -v ~/docker-data/postgres:/var/lib/postgresql/data \
  postgres:16

# 验证容器是否正常运行
3.  docker ps

# 常见容器管理命令
docker stop llmops-postgres    关闭数据库
docker start llmops-postgres   启动数据库
docker exec -it llmops-postgres psql -U postgres -d devdb  进入数据库
docker restart llmops-postgres 重启
docker logs -f llmops-postgres 数据库日志
docker ps -a 查看所有容器
docker images 查看本地镜像
docker rmi XXX  删除不用的镜像


最终总结（最关键）
这条命令运行后，你会得到：
✅ 一个运行中的 PostgreSQL 16 数据库
✅ 用户名：postgres
✅ 密码：mydevpass123
✅ 数据库名：devdb
✅ 地址：localhost:5432
✅ 数据永久保存，不会丢失
✅ 开机自启动


你的数据都存在 Docker 容器挂载的 ~/docker-data/postgres 目录里，只要不删除这个目录，数据就不会丢。****