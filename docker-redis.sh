REDIS_CONFIG='port 7000
cluster-enabled yes
cluster-config-file /home/redis/nodes.conf
cluster-node-timeout 5000
appendonly yes'

docker service create --name redis \
  -p 7000:7000 \
  -e REDIS_CONFIG="$REDIS_CONFIG" \
  -e REDIS_CONFIG_FILE="/home/redis/config/redis.conf" \
  redis:3.2.6-alpine sh -c 'mkdir -p /home/redis/config; mkdir -p $(dirname $REDIS_CONFIG_FILE) && echo "$REDIS_CONFIG" > $REDIS_CONFIG_FILE && cat $REDIS_CONFIG_FILE && redis-server $REDIS_CONFIG_FILE'
sleep 2
docker service ps redis

