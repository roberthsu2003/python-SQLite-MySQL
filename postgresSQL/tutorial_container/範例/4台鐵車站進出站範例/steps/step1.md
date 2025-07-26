# 步驟 1：環境設置與資料庫連接

## 學習重點
- Python 環境設置
- 安裝 psycopg2 套件
- 建立與 PostgreSQL 資料庫的連接
- 基本的錯誤處理

## 環境準備

### 1. 安裝必要的套件
首先，我們需要安裝 `psycopg2` 套件，這是 Python 連接 PostgreSQL 資料庫的驅動程式：

```bash
pip install psycopg2-binary
```

> 注意：我們使用 `psycopg2-binary` 而不是 `psycopg2`，因為前者是預編譯的二進制版本，安裝更加簡單。

### 2. 建立主程式檔案
創建一個名為 `main.py` 的檔案，這將是我們的主程式：

## 程式碼說明

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
台鐵資料查詢系統 - 主程式
這是一個簡單的命令列介面程式，用於查詢台鐵車站資訊和進出站人數
"""

import psycopg2
import sys

# 資料庫連線設定
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "raspberry",
    "host": "host.docker.internal",
    "port": "5432"
}

def connect_to_database():
    """連接到 PostgreSQL 資料庫"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"資料庫連線錯誤: {e}")
        return None

def main():
    """主程式"""
    conn = connect_to_database()
    if not conn:
        print("無法連接到資料庫，程式結束")
        sys.exit(1)

    print("成功連接到資料庫！")

    # 測試連接是否成功
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL 資料庫版本: {db_version[0]}")

    # 關閉連接
    cursor.close()
    conn.close()
    print("資料庫連接已關閉")

if __name__ == "__main__":
    main()
```

## 程式碼解析

1. **引入必要的套件**：
   - `psycopg2`：用於連接 PostgreSQL 資料庫
   - `sys`：用於系統相關操作，如程式退出

2. **資料庫連線設定**：
   - 使用字典儲存資料庫連線參數
   - 包含資料庫名稱、使用者名稱、密碼、主機和連接埠

3. **連接資料庫函數**：
   - `connect_to_database()` 函數嘗試連接到資料庫
   - 使用 `try-except` 結構處理可能的連接錯誤
   - 成功時返回連接物件，失敗時返回 `None`

4. **主程式**：
   - 嘗試連接資料庫
   - 如果連接失敗，程式結束
   - 如果連接成功，顯示資料庫版本
   - 最後關閉資料庫連接

## 執行結果

成功連接時的輸出應該類似：

```
成功連接到資料庫！
PostgreSQL 資料庫版本: PostgreSQL 14.5 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 10.2.1 20210130, 64-bit
資料庫連接已關閉
```

連接失敗時的輸出可能是：

```
資料庫連線錯誤: could not connect to server: Connection refused
無法連接到資料庫，程式結束
```

## 練習

1. 修改程式碼，讓使用者可以輸入資料庫連線參數（如主機名稱、使用者名稱和密碼）。
2. 擴展程式碼，顯示資料庫中的所有表格名稱。
3. 嘗試連接到不同的資料庫，觀察錯誤訊息並改進錯誤處理。

## 延伸閱讀

- [psycopg2 官方文件](https://www.psycopg.org/docs/)
- [PostgreSQL 官方文件](https://www.postgresql.org/docs/)
- [Python 錯誤處理最佳實踐](https://docs.python.org/3/tutorial/errors.html)