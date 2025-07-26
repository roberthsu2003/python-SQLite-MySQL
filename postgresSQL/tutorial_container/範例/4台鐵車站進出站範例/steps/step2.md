# 步驟 2：建立命令列介面 (CLI)

## 學習重點
- 建立簡單的命令列介面
- 實現選單系統
- 使用者輸入處理
- 程式流程控制

## 程式碼說明

在這個步驟中，我們將擴展我們的程式，加入一個互動式的命令列介面，讓使用者可以選擇不同的功能。

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

def display_menu():
    """顯示主選單"""
    print("\n===== 台鐵資料查詢系統 =====")
    print("1. 查詢所有車站資訊")
    print("2. 查詢特定地區的車站")
    print("3. 查詢車站進出站人數")
    print("4. 統計分析")
    print("0. 離開系統")
    print("==========================")

def main():
    """主程式"""
    conn = connect_to_database()
    if not conn:
        print("無法連接到資料庫，程式結束")
        sys.exit(1)

    print("成功連接到資料庫！")

    while True:
        display_menu()
        choice = input("請選擇功能 (0-4): ")

        if choice == '0':
            print("感謝使用，再見！")
            break
        elif choice == '1':
            print("功能 1: 查詢所有車站資訊 (尚未實現)")
        elif choice == '2':
            print("功能 2: 查詢特定地區的車站 (尚未實現)")
        elif choice == '3':
            print("功能 3: 查詢車站進出站人數 (尚未實現)")
        elif choice == '4':
            print("功能 4: 統計分析 (尚未實現)")
        else:
            print("無效的選擇，請重新輸入")

    conn.close()
    print("資料庫連接已關閉")

if __name__ == "__main__":
    main()
```

## 程式碼解析

1. **新增 `display_menu()` 函數**：
   - 顯示程式的主選單
   - 列出所有可用的功能選項

2. **擴展 `main()` 函數**：
   - 使用 `while` 迴圈創建一個持續運行的選單系統
   - 使用 `input()` 函數獲取使用者輸入
   - 使用條件判斷 (`if-elif-else`) 處理不同的選單選項
   - 當使用者選擇 '0' 時退出迴圈，結束程式

3. **使用者互動**：
   - 程式會等待使用者輸入一個數字
   - 根據輸入的數字執行相應的功能
   - 如果輸入無效，會提示使用者重新輸入

## 執行結果

程式執行後，會顯示如下選單：

```
成功連接到資料庫！

===== 台鐵資料查詢系統 =====
1. 查詢所有車站資訊
2. 查詢特定地區的車站
3. 查詢車站進出站人數
4. 統計分析
0. 離開系統
==========================
請選擇功能 (0-4):
```

使用者可以輸入數字選擇功能，例如輸入 `1`：

```
請選擇功能 (0-4): 1
功能 1: 查詢所有車站資訊 (尚未實現)

===== 台鐵資料查詢系統 =====
1. 查詢所有車站資訊
2. 查詢特定地區的車站
3. 查詢車站進出站人數
4. 統計分析
0. 離開系統
==========================
請選擇功能 (0-4):
```

輸入 `0` 退出程式：

```
請選擇功能 (0-4): 0
感謝使用，再見！
資料庫連接已關閉
```

## 練習

1. 修改選單，加入更多功能選項。
2. 實現一個簡單的幫助系統，當使用者輸入 `help` 或 `?` 時顯示說明。
3. 加入輸入驗證，確保使用者只能輸入有效的選項。
4. 實現一個子選單系統，例如在「統計分析」選項下顯示更多細分的功能。

## 延伸閱讀

- [Python 輸入輸出](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python 流程控制](https://docs.python.org/3/tutorial/controlflow.html)
- [命令列介面設計最佳實踐](https://clig.dev/)