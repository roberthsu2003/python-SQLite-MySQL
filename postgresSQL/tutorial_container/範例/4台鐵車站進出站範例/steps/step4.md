# 步驟 4：查詢進出站人數資料

## 學習重點
- 處理多表查詢
- 日期資料處理
- 資料關聯與過濾
- 處理可能不存在的資料

## 程式碼說明

在這個步驟中，我們將實現查詢特定車站的進出站人數功能。這需要從「台鐵車站資訊」表獲取車站代碼，然後使用這個代碼查詢「每日各站進出站人數」表。

```python
from datetime import datetime

def list_passenger_data(conn, station_name):
    """列出特定車站的進出站人數"""
    try:
        cursor = conn.cursor()

        # 先查詢車站代碼
        cursor.execute('SELECT "stationCode", "stationName" FROM "台鐵車站資訊" WHERE "stationName" = %s', (station_name,))
        station = cursor.fetchone()

        if not station:
            print(f"找不到名為 {station_name} 的車站")
            return

        station_code = station[0]

        # 查詢進出站人數資料
        # 注意：這裡的 SQL 查詢需要根據實際的資料表結構進行調整
        cursor.execute('SELECT * FROM "每日各站進出站人數" WHERE "車站代碼" = %s ORDER BY "日期" DESC LIMIT 10', (station_code,))
        data = cursor.fetchall()

        if not data:
            print(f"{station_name} 車站沒有進出站人數資料")
            return

        print(f"\n=== {station_name} 車站進出站人數 (最近10筆) ===")
        # 根據實際資料表結構調整輸出格式
        print(f"{'日期':<15}{'進站人數':<10}{'出站人數':<10}")
        print("-" * 35)

        for row in data:
            # 假設資料表結構為：車站代碼、日期、進站人數、出站人數
            # 根據實際情況調整索引
            print(f"{row[1]:<15}{row[2]:<10}{row[3]:<10}")

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
            station = input("請輸入車站名稱: ")
            list_passenger_data(conn, station)
        elif choice == '4':
            print("功能 4: 統計分析 (尚未實現)")
        else:
            print("無效的選擇，請重新輸入")

    conn.close()
```

## 程式碼解析

1. **多步驟查詢**：
   - 首先查詢「台鐵車站資訊」表，獲取車站代碼
   - 使用 `fetchone()` 獲取單一結果
   - 檢查是否找到車站，如果沒有則提前返回
   - 使用找到的車站代碼查詢「每日各站進出站人數」表

2. **資料驗證與錯誤處理**：
   - 檢查車站是否存在
   - 檢查是否有進出站人數資料
   - 使用適當的錯誤訊息提示使用者

3. **結果限制與排序**：
   - 使用 `ORDER BY "日期" DESC` 按日期降序排序，顯示最新資料
   - 使用 `LIMIT 10` 限制結果數量，避免資料過多

4. **日期處理**：
   - 引入 `datetime` 模組處理日期資料
   - 根據實際資料表結構格式化日期輸出

## 執行結果

查詢車站進出站人數的輸出示例：

```
請輸入車站名稱: 台北

=== 台北 車站進出站人數 (最近10筆) ===
日期            進站人數    出站人數
-----------------------------------
2023-06-30     45678      43210
2023-06-29     44321      42345
2023-06-28     43567      41234
2023-06-27     42789      40987
2023-06-26     41234      39876
2023-06-25     38765      37654
2023-06-24     52345      51234
2023-06-23     43210      42109
2023-06-22     42345      41234
2023-06-21     41234      40123
```

如果找不到車站：

```
請輸入車站名稱: 不存在的車站
找不到名為 不存在的車站 的車站
```

如果車站沒有進出站人數資料：

```
請輸入車站名稱: 海科館
海科館 車站沒有進出站人數資料
```

## 練習

1. 擴展功能，允許使用者指定日期範圍查詢進出站人數。
2. 計算並顯示進出站人數的總和和平均值。
3. 實現一個功能，比較兩個車站的進出站人數。
4. 加入資料視覺化，例如使用 ASCII 圖表顯示進出站人數趨勢。

## 延伸閱讀

- [Python datetime 模組](https://docs.python.org/3/library/datetime.html)
- [PostgreSQL 日期函數](https://www.postgresql.org/docs/current/functions-datetime.html)
- [SQL JOIN 操作](https://www.postgresql.org/docs/current/tutorial-join.html)
- [Python 資料視覺化入門](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)