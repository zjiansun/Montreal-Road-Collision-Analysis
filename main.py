import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.dropna(subset = ['RUE_ACCDN'], inplace = True) # drop rows with missing street names

df.drop(['NO_SEQ_COLL', 'JR_SEMN_ACCDN', 'CD_MUNCP', 'NO_CIVIQ_ACCDN', 'SFX_NO_CIVIQ_ACCDN', 'BORNE_KM_ACCDN', 'TP_REPRR_ACCDN', 'NB_METRE_DIST_ACCD', 'CD_SIT_PRTCE_ACCDN', 'CD_ETAT_SURFC', 'CD_ECLRM', 'CD_ENVRN_ACCDN', 'NO_ROUTE', 'CD_CATEG_ROUTE', 'CD_ETAT_CHASS', 'CD_ASPCT_ROUTE', 'CD_LOCLN_ACCDN', 'CD_POSI_ACCDN', 'CD_CONFG_ROUTE', 'CD_ZON_TRAVX_ROUTR', 'CD_PNT_CDRNL_ROUTE', 'CD_PNT_CDRNL_REPRR', 'CD_COND_METEO', 'CD_COND_METEO', 'MRC'], axis = 1, inplace = True) # drop column with collision number

# The top 10 streets with most collisions
# print(df['RUE_ACCDN'].value_counts().head(10))

# The top 10 streets with most deadly collisions
# print(df[df['NB_MORTS'] > 0]['RUE_ACCDN'].value_counts().head(10))

#print the hour of the day with most collisions (the string HEURE_ACCDN indicates the hour of the day)
df['HEURE_ACCDN'].replace({
    '00:00:00-00:59:00' : '12AM-1AM', 
    '01:00:00-01:59:00' : '1AM-2AM',  
    '02:00:00-02:59:00' : '2AM-3AM', 
    '03:00:00-03:59:00' : '3AM-4AM',
    '04:00:00-04:59:00' : '4AM-5AM',
    '05:00:00-05:59:00' : '5AM-6AM',
    '06:00:00-06:59:00' : '6AM-7AM',
    '07:00:00-07:59:00' : '7AM-8AM',
    '08:00:00-08:59:00' : '8AM-9AM',
    '09:00:00-09:59:00' : '9AM-10AM',
    '10:00:00-10:59:00' : '10AM-11AM',
    '11:00:00-11:59:00' : '11AM-12PM',
    '12:00:00-12:59:00' : '12PM-1PM',
    '13:00:00-13:59:00' : '1PM-2PM',
    '14:00:00-14:59:00' : '2PM-3PM',
    '15:00:00-15:59:00' : '3PM-4PM',
    '16:00:00-16:59:00' : '4PM-5PM',
    '17:00:00-17:59:00' : '5PM-6PM',
    '18:00:00-18:59:00' : '6PM-7PM',
    '19:00:00-19:59:00' : '7PM-8PM',
    '20:00:00-20:59:00' : '8PM-9PM',
    '21:00:00-21:59:00' : '9PM-10PM',
    '22:00:00-22:59:00' : '10PM-11PM',
    '23:00:00-23:59:00' : '11PM-12AM'
    }, inplace = True)
df = df[df.HEURE_ACCDN != "Non précisé"]
print(df['HEURE_ACCDN'].value_counts())

# plot the hour of the day with most collisions with the matplotlib library
df['HEURE_ACCDN'].value_counts().plot(kind='bar', title='Road collisions by hour of the day- Montreal', xlabel='Hour of day', ylabel='Total accidents (2012-2022)' ,figsize=(10, 5))
plt.show()