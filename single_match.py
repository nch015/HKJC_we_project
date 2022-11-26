import pandas as pd
from scrap_hk33race_result import horseracec33_soup
from dataclasses import fields,dataclass
import datetime as dt
infoof_horse=[]


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

    def locate_result_table(self):
        table=self.soup.find("div",{"id":"race_result_horses","class":"mb_s mlr_a"})
        horses=table.find_all("div",{"class":"race_result_horse mb_xs ptb_xs"})
        horse_dict= {i:j for i,j in enumerate(horses)}
        return horse_dict

    def get_each_horse_info_by_race(self):

if __name__ == '__main__':
    all_race_df=pd.read_csv('output/all_racedate_info.csv',header=0,)
    row=all_race_df.iloc[0]
    race=hk33_horacerace_result(date=row['date'], race_num=row['num_of_race'],
                           court=row['court'], track=row['track'], season=row['season'])
    race.locate_result_table()
