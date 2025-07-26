# 步驟 3：查詢車站資訊

## 學習重點
- 執行 SQL 查詢
- 使用參數化查詢防止 SQL 注入
- 處理查詢結果
- 格式化輸出資料

## 程式碼說明

在這個步驟中，我們將實現兩個功能：查詢所有車站資訊和查詢特定地區的車站。

```python
def list_all_stations(conn):
    """列出所有車站資訊"""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT "stationCode", "stationName", "stationAddrTw" FROM "台鐵車站資訊" ORDER BY "stationCode"')
        stations = cursor.fetchall()

        print("\n=== 所有車站列表 ===")
        print(f"{'車站代碼':<10}{'車站名稱':<15}{'地址':<30}")
        print("-" * 55)

        for station in stations:
            print(f"{station[0]:<10}{station[1]:<15}{station[2]:<30}")

        print(f"\n共有 {len(stations)} 個車站")
        cursor.close()
    except Exception as e:
        print(f"查詢錯誤: {e}")

def list_stations_by_area(conn, area):
    """列出特定地區的車站"""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT "stationCode", "stationName", "stationAddrTw" FROM "台鐵車站資訊" WHERE "stationAddrTw" LIKE %s ORDER BY "stationCode"', (f'%{area}%',))
        stations = cursor.fetchall()

        print(f"\n=== {area}地區車站列表 ===")
        print(f"{'車站代碼':<10}{'車站名稱':<15}{'地址':<30}")
        print("-" * 55)

        for station in stations:
            print(f"{station[0]:<10}{station[1]:<15}{station[2]:<30}")

        print(f"\n共有 {len(stations)} 個車站")
        cursor.close()
    except Exception as e:
        print(f"查詢錯誤: {e}")
```

同時，我們需要更新 `main()` 函數中的相應部分：

```python
def main():
    """主程式"""
    conn = connect_to_database()
    if not conn:
        print("無法連接到資料庫，程式結束")
        sys.exit(1)

    while True:
        display_menu()
        choice = input("請選擇功能 (0-4): ")

        if choice == '0':
            print("感謝使用，再見！")
            break
        elif choice == '1':
            list_all_stations(conn)
        elif choice == '2':
            area = input("請輸入地區名稱 (例如: 基隆、台北): ")
            list_stations_by_area(conn, area)
        elif choice == '3':
            print("功能 3: 查詢車站進出站人數 (尚未實現)")
        elif choice == '4':
            print("功能 4: 統計分析 (尚未實現)")
        else:
            print("無效的選擇，請重新輸入")

    conn.close()
```

## 程式碼解析

1. **`list_all_stations()` 函數**：
   - 創建一個資料庫游標 (cursor)
   - 執行 SQL 查詢，獲取所有車站的代碼、名稱和地址
   - 使用 `fetchall()` 獲取所有查詢結果
   - 格式化輸出結果，使用 f-string 和字串對齊
   - 顯示車站總數
   - 使用 `try-except` 處理可能的錯誤

2. **`list_stations_by_area()` 函數**：
   - 與 `list_all_stations()` 類似，但加入了 WHERE 條件
   - 使用參數化查詢 (`%s`) 防止 SQL 注入攻擊
   - 使用 LIKE 運算符進行模糊匹配，搜尋地址中包含特定地區名稱的車站

3. **參數化查詢**：
   - 使用 `%s` 作為參數佔位符
   - 將實際參數作為元組傳遞給 `execute()` 方法
   - 這是防止 SQL 注入攻擊的最佳實踐

4. **格式化輸出**：
   - 使用 f-string 和 `:<數字>` 語法控制輸出寬度
   - 創建表頭和分隔線，使輸出更易讀

## 執行結果

查詢所有車站的輸出示例：

```
=== 所有車站列表 ===
車站代碼   車站名稱        地址
-------------------------------------------------------
900       基隆          基隆市仁愛區港西街5號
910       三坑          基隆市仁愛區德厚里龍安街 206 號
920       八堵          基隆市暖暖區八南里八堵路 142 號
...

共有 241 個車站
```

查詢特定地區車站的輸出示例：

```
請輸入地區名稱 (例如: 基隆、台北): 基隆

=== 基隆地區車站列表 ===
車站代碼   車站名稱        地址
-------------------------------------------------------
900       基隆          基隆市仁愛區港西街5號
910       三坑          基隆市仁愛區德厚里龍安街 206 號
920       八堵          基隆市暖暖區八南里八堵路 142 號
930       七堵          基隆市七堵區長興里東新街 2 號
940       百福          基隆市七堵區堵南里明德三路 1 之 1 號
7361      海科館        基隆市中正區長潭里
7390      暖暖          基隆市暖暖區暖暖里暖暖街 51 號

共有 7 個車站
```

## 練習

1. 擴展 `list_all_stations()` 函數，顯示更多車站資訊，如電話號碼和是否提供自行車服務。
2. 實現一個新功能，允許使用者根據車站名稱搜尋特定車站。
3. 修改程式碼，讓使用者可以選擇排序方式（按車站代碼、名稱或地區排序）。
4. 實現分頁功能，每次只顯示 10 個車站，並允許使用者瀏覽下一頁或上一頁。

## 延伸閱讀

- [psycopg2 游標使用](https://www.psycopg.org/docs/usage.html#query-parameters)
- [SQL 注入攻擊與防範](https://owasp.org/www-community/attacks/SQL_Injection)
- [Python 字串格式化](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
- [PostgreSQL LIKE 運算符](https://www.postgresql.org/docs/current/functions-matching.html)