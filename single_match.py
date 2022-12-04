import pandas as pd
from scrap_hk33race_result import horseracec33_soup
from dataclasses import fields,dataclass
import datetime as dt
from parameters import *


@dataclass
class hk33_horacerace_result:
    date:str
    race_num:int
    court:str
    track:str
    season:str

    def __post_init__(self):
        self.url = f"https://horse.hk33.com/race-results/{self.date}/{self.race_num}"
        self.soup = horseracec33_soup(self.url)
        self.df = pd.DataFrame(columns=[])
        # print(self.soup)

    def locate_result_table_to_dict(self):
        table=self.soup.find("div",{"id":"race_result_horses","class":"mb_s mlr_a"})
        horses=table.find_all("div",{"class":"race_result_horse mb_xs ptb_xs"})
        self.horse_dict= {i:j for i,j in enumerate(horses)}
        # return horse_dict

    def get_each_horse_info_by_race(self,horse_html):
        # print(horse_html)
        temp_dict={}
        for k,v in hk33_horse_class_info_loc.items():
            for nk,nv in v.items():
                temp_dict[k]=horse_html.find(nk,nv).text.strip()
        return temp_dict

if __name__ == '__main__':
    all_race_df=pd.read_csv('output/all_racedate_info.csv',header=0,)
    row=all_race_df.iloc[0]
    print(row)
    race=hk33_horacerace_result(date=row['date'], race_num=row['num_of_race'],
                           court=row['court'], track=row['track'], season=row['season'])
    race.locate_result_table_to_dict()
    horse_dict = race.get_each_horse_info_by_race(race.horse_dict[0])
    print(horse_dict)
