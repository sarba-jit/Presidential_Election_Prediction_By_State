from pandas import *
import numpy as np
import re
from string import *

candidates = ['clinton','cruz','sanders','trump']
dates = [18,19,20,21,22,23,24,25,26,27,28,29]

for item_candidates in candidates:
    for item_dates in dates:
        df = read_csv(open(item_candidates+'/'+item_candidates+'_03_'+str(item_dates)+'.csv', 'rU'), encoding='utf-8', engine='c')
        df1 = df[df['userLocation'].notnull()]
        print list(df1)
        df2 = pandas.DataFrame(columns=['tweetID', 'tweetText', 'tweetRetweetCt', 'tweetFavoriteCt', 'tweetSource', 'tweetCreated', 'userID',
                                'userScreen', 'userName', 'userCreateDt', 'userDesc', 'userFollowerCt', 'userFriendsCt', 'userLocation', 'userTimezone'])

        test_string = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
               'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
               'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
               'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICU', 'DELAWARE',
               'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOI', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
               'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA',
               'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA',
               'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA',
               'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA',
               'WISCONSIN', 'WYOMING','AMERICA','US','USA','UNITED STATES OF AMERICA']

        count =0
        for index, row in df1.iterrows():
            x = str(row['userLocation'].encode('utf-8'))
            x = str.upper(x)
            if type(x) == str:
                for item in test_string:
                        for item2 in x.split():
                            if (item == str(item2)):
                                count = count + 1
                                df2 = df2.append(row)

        print count
        df2.to_csv(item_candidates+'/count/'+item_candidates+'_03_'+str(item_dates)+'_count.csv', sep=',', encoding='utf-8')
        my_file = open(item_candidates +'/count/'+'count.txt', 'a')
        my_file.write(str(item_dates) + '  ' + str(count) + '\n')
        my_file.close()