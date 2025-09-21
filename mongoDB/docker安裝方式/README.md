# 使用Docker安裝MongoDB方式

## 目錄
- [方法一：使用Docker Compose（推薦）](#方法一使用docker-compose推薦)
- [方法二：使用Docker命令直接運行](#方法二使用docker命令直接運行)
- [方法三：使用Dockerfile自定義鏡像](#方法三使用dockerfile自定義鏡像)
- [方法四：使用Docker Hub官方鏡像](#方法四使用docker-hub官方鏡像)
- [常見問題與解決方案](#常見問題與解決方案)

---

## 方法一：使用Docker Compose（推薦）

### 1. 創建docker-compose.yml文件

```yaml
version: '3.8'

services:
  mongodb:
    image: mongo:latest
    container_name: mongodb_container
    restart: always
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password123
      MONGO_INITDB_DATABASE: mydatabase
    volumes:
      - mongodb_data:/data/db
      - ./init-scripts:/docker-entrypoint-initdb.d
    networks:
      - mongodb_network

volumes:
  mongodb_data:

networks:
  mongodb_network:
    driver: bridge
```

### 2. 創建初始化腳本（可選）

在`init-scripts`目錄下創建`init.js`：

```javascript
// 創建用戶和數據庫
db = db.getSiblingDB('mydatabase');
db.createUser({
  user: 'myuser',
  pwd: 'mypassword',
  roles: [
    {
      role: 'readWrite',
      db: 'mydatabase'
    }
  ]
});

// 創建示例集合
db.createCollection('users');
db.users.insertOne({
  name: 'John Doe',
  email: 'john@example.com',
  created_at: new Date()
});
```

### 3. 啟動MongoDB

```bash
# 啟動服務
docker-compose up -d

# 查看日誌
docker-compose logs -f mongodb

# 停止服務
docker-compose down
```

---

## 方法二：使用Docker命令直接運行

### 1. 基本運行命令

```bash
# 運行MongoDB容器
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  mongo:latest
```

### 2. 帶數據持久化的運行命令

```bash
# 創建數據卷
docker volume create mongodb_data

# 運行MongoDB容器（帶數據持久化）
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  -v mongodb_data:/data/db \
  mongo:latest
```

### 3. 管理容器

```bash
# 查看運行中的容器
docker ps

# 查看MongoDB日誌
docker logs mongodb

# 進入MongoDB容器
docker exec -it mongodb mongosh

# 停止容器
docker stop mongodb

# 刪除容器
docker rm mongodb
```

---

## 方法三：使用Dockerfile自定義鏡像

### 1. 創建Dockerfile

```dockerfile
FROM mongo:latest

# 設置工作目錄
WORKDIR /data/db

# 複製初始化腳本
COPY init-scripts/ /docker-entrypoint-initdb.d/

# 設置權限
RUN chmod +x /docker-entrypoint-initdb.d/*.sh

# 暴露端口
EXPOSE 27017

# 啟動MongoDB
CMD ["mongod"]
```

### 2. 構建和運行

```bash
# 構建鏡像
docker build -t custom-mongodb .

# 運行自定義鏡像
docker run -d \
  --name custom-mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  custom-mongodb
```

---

## 方法四：使用Docker Hub官方鏡像

### 1. 拉取官方鏡像

```bash
# 拉取最新版本
docker pull mongo:latest

# 拉取特定版本
docker pull mongo:6.0

# 查看可用標籤
docker search mongo
```

### 2. 運行不同版本的MongoDB

```bash
# 運行MongoDB 6.0
docker run -d \
  --name mongodb-6 \
  -p 27017:27017 \
  mongo:6.0

# 運行MongoDB 5.0
docker run -d \
  --name mongodb-5 \
  -p 27018:27017 \
  mongo:5.0
```

---

## 常見問題與解決方案

### 1. 端口衝突

**問題**：端口27017已被佔用

**解決方案**：
```bash
# 使用不同端口
docker run -d \
  --name mongodb \
  -p 27018:27017 \
  mongo:latest

# 或停止佔用端口的服務
sudo lsof -i :27017
sudo kill -9 <PID>
```

### 2. 數據持久化問題

**問題**：容器重啟後數據丟失

**解決方案**：
```bash
# 使用命名卷
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -v mongodb_data:/data/db \
  mongo:latest

# 使用主機目錄
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -v /host/path:/data/db \
  mongo:latest
```

### 3. 權限問題

**問題**：無法寫入數據目錄

**解決方案**：
```bash
# 設置正確的權限
sudo chown -R 999:999 /host/path
sudo chmod -R 755 /host/path
```

### 4. 連接問題

**問題**：無法從外部連接MongoDB

**解決方案**：
```bash
# 檢查容器狀態
docker ps

# 檢查端口映射
docker port mongodb

# 檢查防火牆設置
sudo ufw allow 27017
```

### 5. 內存不足

**問題**：MongoDB容器因內存不足而停止

**解決方案**：
```bash
# 限制容器內存使用
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  --memory="2g" \
  --memory-swap="4g" \
  mongo:latest
```

---

## 連接測試

### 使用MongoDB Shell連接

```bash
# 進入容器
docker exec -it mongodb mongosh

# 或直接連接
docker exec -it mongodb mongosh "mongodb://admin:password123@localhost:27017"
```

### 使用Python連接

```python
from pymongo import MongoClient

# 連接MongoDB
client = MongoClient('mongodb://admin:password123@localhost:27017/')

# 測試連接
try:
    client.admin.command('ping')
    print("成功連接到MongoDB!")
except Exception as e:
    print(f"連接失敗: {e}")
```

---

## 最佳實踐

1. **使用Docker Compose**：便於管理和配置
2. **設置數據持久化**：避免數據丟失
3. **使用環境變量**：安全地管理密碼
4. **定期備份**：保護重要數據
5. **監控資源使用**：確保穩定性
6. **使用特定版本**：避免版本兼容性問題

---

## 相關資源

- [MongoDB官方Docker Hub](https://hub.docker.com/_/mongo)
- [Docker Compose文檔](https://docs.docker.com/compose/)
- [MongoDB官方文檔](https://docs.mongodb.com/)
- [PyMongo文檔](https://pymongo.readthedocs.io/)