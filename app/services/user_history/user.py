import math

import pandas as pd
from riotwatcher import LolWatcher

from app.services.user_history.user_history import ApiHistory


class ApiUser(object):
    def __init__(self):
        global api_key, watcher, my_region
        api_key = "RGAPI-2d9f46bc-9615-4aa2-918b-a53b55078857"
        watcher = LolWatcher(api_key)
        my_region = "kr"

    def user_info(self, nickname):
        user = watcher.summoner.by_name(my_region, nickname)
        nickname = user['name']
        uuid = user['puuid']
        match_id = watcher.match.matchlist_by_puuid(my_region, uuid, type='ranked')
        recent = []
        for i in range(len(match_id)):
            matches = watcher.match.by_id(my_region, match_id[i])
            metadata = matches['metadata']['participants']
            user_num = [i for i in range(0, 10) if metadata[i] == uuid]
            user_info = matches['info']["participants"][user_num[0]]
            champion_name = user_info['championName']
            recent.append(champion_name)
        most = max(set(recent), key=recent.count)
        level = user['summonerLevel']
        leage = watcher.league.by_summoner(my_region, user['id'])
        tier = f"{leage[0]['tier']} {leage[0]['rank']}"
        win_rate = f"{int(leage[0]['wins'] / (leage[0]['losses'] + leage[0]['wins']) * 100)}%"
        db_df = {'uuid' : uuid, 'nickname' : nickname, 'tier' : tier, 'win_rate' : win_rate, 'most' : most, 'level' : level}
        print(db_df)
        return db_df

