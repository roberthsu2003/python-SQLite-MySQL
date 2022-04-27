# 台灣即時pm2.5資訊
## 只收集最新一筆資料

### 第一部份下載資訊.py

```python
import dataSource

if __name__ == "__main__":
    downloadData = dataSource.downloadData()
    for item in downloadData:
        print(item)

```


### dataSource.py
- [註冊行政院環保署資料開放平臺會員](https://data.epa.gov.tw/paradigm)

```python
import requests
def downloadData():
    urlpath = '	https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'
    def stringToFloat(s):
        try:
            return float(s)
        except:
            return 999.0
    response = requests.get(urlpath)
    if response.status_code == 200:
        print('下載成功')
        data = response.json()
        datas = data["records"]
        importData = [
            (item['Site'], item['county'], stringToFloat(item['PM25']), item['DataCreationDate'], item['ItemUnit']) for
            item in datas]
        return importData
        
```


