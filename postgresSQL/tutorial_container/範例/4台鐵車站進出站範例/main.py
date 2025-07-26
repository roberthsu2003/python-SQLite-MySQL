#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
台鐵資料查詢系統 - 主程式
這是一個簡單的命令列介面程式，用於查詢台鐵車站資訊和進出站人數
"""

import psycopg2
import sys
from datetime import datetime

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
            show_statistics(conn)
        else:
            print("無效的選擇，請重新輸入")

    conn.close()

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

def list_passenger_data(conn, station_name):
    """列出特定車站的進出站人數"""
    # 這個功能需要根據實際的資料表結構來實現
    # 這裡假設「每日各站進出站人數」表有站名、日期、進站人數、出站人數等欄位
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

def show_statistics(conn):
    """顯示統計分析資料"""
    try:
        cursor = conn.cursor()

        # 1. 各縣市車站數量統計
        print("\n=== 各縣市車站數量統計 ===")
        cursor.execute("""
            SELECT
                SUBSTRING("stationAddrTw" FROM '^[^市縣]*[市縣]') as city,
                COUNT(*) as count
            FROM "台鐵車站資訊"
            GROUP BY SUBSTRING("stationAddrTw" FROM '^[^市縣]*[市縣]')
            ORDER BY count DESC
        """)

        city_stats = cursor.fetchall()
        for city, count in city_stats:
            print(f"{city if city else '未知':<10}: {count} 個車站")

        # 2. 有無自行車服務的車站統計
        print("\n=== 自行車服務統計 ===")
        cursor.execute("""
            SELECT
                "haveBike",
                COUNT(*) as count
            FROM "台鐵車站資訊"
            GROUP BY "haveBike"
        """)

        bike_stats = cursor.fetchall()
        for have_bike, count in bike_stats:
            status = "提供" if have_bike == 'Y' else "不提供"
            print(f"{status}自行車服務的車站: {count} 個")

        cursor.close()
    except Exception as e:
        print(f"統計分析錯誤: {e}")

if __name__ == "__main__":
    main()