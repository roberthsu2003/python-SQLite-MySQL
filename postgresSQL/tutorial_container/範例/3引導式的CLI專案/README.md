Python Command Line 專案，結合 SQL 查詢功能，並且採用**函數框架先行**的教學方式。

## 專案架構建議

````python
import psycopg2
from psycopg2.extras import RealDictCursor
import argparse
import sys
from typing import List, Dict, Any

class SubQueryCLI:
    def __init__(self, db_config: Dict[str, str]):
        """
        初始化資料庫連接
        
        Args:
            db_config: 資料庫連接配置
        """
        self.db_config = db_config
        self.conn = None
        
    def connect_db(self) -> bool:
        """
        建立資料庫連接
        
        Returns:
            bool: 連接成功返回 True，失敗返回 False
            
        TODO: 學生需要實作資料庫連接邏輯
        - 使用 psycopg2 建立連接
        - 處理連接錯誤
        - 設定 cursor_factory 為 RealDictCursor
        """
        # 學生實作區域
        pass
        
    def get_max_entry_count(self) -> List[Dict[str, Any]]:
        """
        範例1: 找出進站人數最多的一筆記錄
        
        Returns:
            List[Dict]: 查詢結果
            
        學習重點:
        - 單值子查詢的使用
        - MAX() 函數的應用
        - LEFT JOIN 的運用
        
        TODO: 學生需要完成以下步驟
        1. 寫出子查詢找出最大進站人數
        2. 將子查詢嵌入主查詢的 WHERE 條件中
        3. 使用 LEFT JOIN 取得站點資訊
        """
        query = """
        -- 請完成這個查詢
        SELECT *
        FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
        WHERE 進站人數 = (
            -- TODO: 完成子查詢
            SELECT _____ 
            FROM _____
        );
        """
        
        # 學生實作區域
        pass
        
    def get_max_entry_by_station(self) -> List[Dict[str, Any]]:
        """
        範例2: 找出各站點進站人數最多的一筆記錄
        
        Returns:
            List[Dict]: 查詢結果
            
        學習重點:
        - 多值子查詢的使用
        - GROUP BY 的應用
        - 複合條件 (欄位1, 欄位2) IN 的用法
        
        TODO: 學生需要完成以下步驟
        1. 理解為什麼需要使用 (站點編號, 進站人數) 的組合
        2. 完成子查詢的 GROUP BY 部分
        3. 在主查詢中正確使用 IN 運算符
        """
        query = """
        -- 請完成這個查詢
        SELECT *
        FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
        WHERE (_____, _____) IN (
            SELECT _____, MAX(_____)
            FROM _____
            GROUP BY _____
        );
        """
        
        # 學生實作區域
        pass
    
    def get_top_sales_by_month(self) -> List[Dict[str, Any]]:
        """
        範例3: 找出每月銷售額最高的商品 (新增範例)
        
        Returns:
            List[Dict]: 查詢結果
            
        學習重點:
        - 商業場景中的數據分析
        - 複合條件查詢的實際應用
        - 時間維度的分組查詢
        
        TODO: 學生需要完成以下步驟
        1. 思考商業需求：為什麼要找每月銷售冠軍？
        2. 設計表格結構（sales, products）
        3. 完成子查詢邏輯
        4. 加入商品資訊的 JOIN
        
        提示：
        - 需要按月份分組
        - 找出每組的最大銷售額
        - 同時返回月份和銷售額用於匹配
        """
        query = """
        -- 請根據學習重點完成這個查詢
        SELECT s.月份, p.商品名稱, s.銷售額
        FROM _____ s LEFT JOIN _____ p ON s._____ = p._____
        WHERE (s._____, s._____) IN (
            SELECT _____, _____(_____) 
            FROM _____
            GROUP BY _____
        );
        """
        
        # 學生實作區域
        pass
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """
        執行 SQL 查詢
        
        Args:
            query: SQL 查詢語句
            
        Returns:
            List[Dict]: 查詢結果
            
        TODO: 學生需要實作查詢執行邏輯
        - 建立 cursor
        - 執行查詢
        - 處理錯誤
        - 返回結果
        """
        # 學生實作區域
        pass
    
    def close_connection(self):
        """
        關閉資料庫連接
        
        TODO: 學生需要實作連接關閉邏輯
        """
        # 學生實作區域
        pass

def main():
    """
    主程式入口
    
    TODO: 學生需要完成以下功能
    1. 設定命令列參數解析
    2. 讀取資料庫配置
    3. 建立 CLI 實例
    4. 根據參數執行相應的查詢
    5. 格式化輸出結果
    """
    
    # 資料庫配置
    db_config = {
        'host': 'localhost',
        'database': 'your_database',
        'user': 'your_username',
        'password': 'your_password',
        'port': 5432
    }
    
    # 建立 CLI 實例
    cli = SubQueryCLI(db_config)
    
    # 學生實作區域
    pass

if __name__ == "__main__":
    main()
````

## 學習檢核表

````markdown
## SubQuery CLI 專案學習檢核

### 階段1：基礎設定
- [ ] 能夠理解專案結構
- [ ] 能夠建立資料庫連接
- [ ] 能夠處理基本的錯誤處理

### 階段2：單值子查詢
- [ ] 能夠解釋 `get_max_entry_count()` 的商業需求
- [ ] 能夠獨立完成子查詢部分
- [ ] 能夠正確使用 LEFT JOIN
- [ ] 能夠測試查詢結果

### 階段3：多值子查詢
- [ ] 能夠理解 `(欄位1, 欄位2) IN` 的邏輯
- [ ] 能夠完成 `get_max_entry_by_station()` 函數
- [ ] 能夠解釋為什麼需要 GROUP BY
- [ ] 能夠驗證每個站點只有一筆最大值記錄

### 階段4：實際應用
- [ ] 能夠設計 `get_top_sales_by_month()` 的表格結構
- [ ] 能夠完成商業場景的子查詢
- [ ] 能夠處理時間維度的分組
- [ ] 能夠測試並驗證結果

### 階段5：CLI 功能
- [ ] 能夠設計命令列參數
- [ ] 能夠格式化輸出結果
- [ ] 能夠處理使用者輸入錯誤
- [ ] 能夠撰寫使用說明

### 自我檢核問題
1. 能否在不看答案的情況下完成 70% 的函數？
2. 能否解釋每個子查詢的執行順序？
3. 能否獨立修改查詢條件？
4. 能否處理基本的程式錯誤？
````

## 使用範例

````bash
# 執行不同的查詢
python subquery_cli.py --query max_entry
python subquery_cli.py --query station_max
python subquery_cli.py --query monthly_sales

# 顯示幫助
python subquery_cli.py --help
````

## 教學流程

1. **先讓學生理解整體架構**
2. **逐一完成每個函數的 TODO 部分**
3. **測試每個函數的功能**
4. **最後完成 CLI 介面**
5. **加入錯誤處理和優化**

