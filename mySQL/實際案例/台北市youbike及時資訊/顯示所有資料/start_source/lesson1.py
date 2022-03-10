import dataSource

if __name__ == "__main__":
    youbikeInfo = dataSource.loadDataFraomYouBikeTP()
    dataSource.update_data(youbikeInfo)