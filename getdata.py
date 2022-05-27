impor pandas as pd

def getdata():

    try:
    import kaggle

    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('imdevskp/corona-virus-report', path='./data', unzip=True)
except:
    print('download kaggle auth to ~/.kaggle.json')

    # getting data
    covid_df = pd.read_csv('./data/covid_19_clean_complete.csv')
    pop_df = pd.read_csv('./data/macro_corona_data.csv')
    df = wrangle_data(covid_df, pop_df)

    return df

