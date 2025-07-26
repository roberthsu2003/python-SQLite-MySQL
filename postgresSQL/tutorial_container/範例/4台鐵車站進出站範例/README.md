# Python 與 PostgreSQL 學習專案

這是一個專為初學者設計的 Python 與 PostgreSQL 學習專案，通過建立一個簡單的台鐵資料查詢系統，幫助學生學習如何使用 Python 連接資料庫並進行基本操作。

## 專案概述

本專案開發一個命令列介面 (CLI) 應用程式，讓使用者可以查詢台鐵車站資訊和進出站人數資料。專案分為多個學習步驟，每個步驟都有明確的學習重點和詳細的程式碼說明。

## 技術需求

- Python 3.x
- PostgreSQL 資料庫
- psycopg2 套件
- 資料表：「台鐵車站資訊」和「每日各站進出站人數」

## 功能特點

1. 查詢所有車站資訊
2. 查詢特定地區的車站
3. 查詢車站進出站人數
4. 統計分析功能

## 學習步驟

本專案分為以下學習步驟：

1. [環境設置與資料庫連接](steps/step1.md)
2. [建立命令列介面 (CLI)](steps/step2.md)
3. [查詢車站資訊](steps/step3.md)
4. [查詢進出站人數資料](steps/step4.md)
5. [統計分析功能](steps/step5.md)

## 如何開始

1. 確保已安裝 Python 3.x
2. 安裝必要的套件：
   ```bash
   pip install psycopg2-binary
   ```
3. 確保 PostgreSQL 資料庫已設置並包含必要的資料表
4. 執行主程式：
   ```bash
   python main.py
   ```

## 資料庫設定

本專案使用 MCP 的 vscode_postgres server 連接到 PostgreSQL 資料庫。資料庫連線設定如下：

```python
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "raspberry",
    "host": "host.docker.internal",
    "port": "5432"
}
```

## 資料表結構

### 台鐵車站資訊

| 欄位名稱 | 資料類型 | 說明 |
|---------|---------|------|
| stationCode | INTEGER | 車站代碼 |
| stationName | VARCHAR | 車站名稱 |
| name | VARCHAR | 車站名稱 |
| stationAddrTw | VARCHAR | 車站地址 |
| stationTel | VARCHAR | 車站電話 |
| gps | VARCHAR | GPS 座標 |
| haveBike | CHAR(1) | 是否提供自行車服務 (Y/N) |

### 每日各站進出站人數

此表的結構需要根據實際資料調整，但預期包含以下欄位：

- 車站代碼
- 日期
- 進站人數
- 出站人數

## 學習資源

- [Python 官方文件](https://docs.python.org/3/)
- [PostgreSQL 官方文件](https://www.postgresql.org/docs/)
- [psycopg2 官方文件](https://www.psycopg.org/docs/)