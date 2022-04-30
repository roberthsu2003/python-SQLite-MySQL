import dataSource

if __name__ == "__main__":
    try:
        dataSource.download_to_mysql('2330.TW')
    except Exception as e:
        print(e)


