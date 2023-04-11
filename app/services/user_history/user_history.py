import pandas as pd
from requests import HTTPError
from riotwatcher import LolWatcher
from collections import defaultdict


class ApiHistory(object):
    def __init__(self):
        global api_key, watcher, my_region
        api_key = "RGAPI-2d9f46bc-9615-4aa2-918b-a53b55078857"
        watcher = LolWatcher(api_key)
        my_region = "kr"

    def summoner(self, nickname):
        try:
            user = watcher.summoner.by_name(my_region, nickname)
            nickname = user['name']
            uuid = user['puuid']
            to_db = pd.DataFrame({
                'nickname': [nickname],
                'uuid': [uuid]
            })

            json = to_db.to_json(orient='records', force_ascii=False)
            print(json)

            return {'nickname': nickname, 'uuid': uuid}

        except HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return {'nickname': nickname, 'uuid': None}


    def match_id(self ,puuid):
        return watcher.match.matchlist_by_puuid(my_region, puuid, type='ranked')

    def play_list(self, nickname,id):
        user = watcher.summoner.by_name(my_region, nickname)
        puuid = user['puuid']
        print(puuid)
        match_id = watcher.match.matchlist_by_puuid(my_region, puuid, type='ranked')
        summoner_name_ls, puuid_ls, match_id_ls, champion_name_ls, result_ls, kills_ls, deaths_ls, assists_ls, kda_ls, position_ls \
            = list(), list(), list(), list(), list(), list(), list(), list(), list(), list()

        for i in range(len(match_id)):
                matches = watcher.match.by_id(my_region, match_id[i])
                metadata = matches['metadata']['participants']
                user_num = [i for i in range(0, 10) if metadata[i] == puuid]
                user_info = matches['info']["participants"][user_num[0]]
                champion_name = user_info['championName']
                result = '패배' if str(user_info['win']) == 'False' else '승리'
                kills = user_info['kills']
                deaths = user_info['deaths']
                assists = user_info['assists']
                kda = 'perfect' if deaths == 0 else round((kills + assists) / deaths, 2)
                position = 'Support' if user_info['teamPosition'] == 'UTILITY' else user_info['teamPosition']
                summoner_name = user_info['summonerName']
                puuid_ls.append(puuid)
                match_id_ls.append(match_id[i])
                champion_name_ls.append(champion_name)
                result_ls.append(result)
                kills_ls.append(kills)
                deaths_ls.append(deaths)
                assists_ls.append(assists)
                kda_ls.append(kda)
                position_ls.append(position)
                summoner_name_ls.append(summoner_name)



                print(f'매치 기록 : {match_id[i]}\n'
                      f'챔피언 이름 :{champion_name} \n'
                      f'승리 패배 : {result}\n'
                      f'킬 : {kills}\n'
                      f'데스 : {deaths}\n'
                      f'어시스트 : {assists}\n'
                      f'kda : {kda},\n'
                      f'라인 : {position}\n'
                      f'닉네임 : {summoner_name}\n')

        db_df = pd.DataFrame({'id': id, 'nickname': summoner_name_ls, 'uuid': puuid_ls, 'matchid' : match_id_ls, 'champion': champion_name_ls, 'result': result_ls, 'kills': kills_ls,
                    'deaths': deaths_ls, 'assists': assists_ls, 'kda' : kda_ls, 'position': position_ls })
        print(db_df)
        print(db_df.columns)
        json = db_df.to_json(orient='records', force_ascii=False)
        print(json)
        return db_df


    def play_list_ls(self, nickname):
        user = watcher.summoner.by_name(my_region, nickname)
        puuid = user['puuid']
        print(puuid)
        match_id = watcher.match.matchlist_by_puuid(my_region, puuid, type='ranked')
        summoner_name_ls, puuid_ls, match_id_ls, champion_name_ls, result_ls, kills_ls, deaths_ls, assists_ls, kda_ls, position_ls \
            = list(), list(), list(), list(), list(), list(), list(), list(), list(), list()

        for i in range(len(match_id)):
                matches = watcher.match.by_id(my_region, match_id[i])
                metadata = matches['metadata']['participants']
                user_num = [i for i in range(0, 10) if metadata[i] == puuid]
                user_info = matches['info']["participants"][user_num[0]]
                champion_name = user_info['championName']
                result = '패배' if str(user_info['win']) == 'False' else '승리'
                kills = user_info['kills']
                deaths = user_info['deaths']
                assists = user_info['assists']
                kda = 'perfect' if deaths == 0 else round((kills + assists) / deaths, 2)
                position = 'Support' if user_info['teamPosition'] == 'UTILITY' else user_info['teamPosition']
                summoner_name = user_info['summonerName']
                puuid_ls.append(puuid)
                match_id_ls.append(match_id[i])
                champion_name_ls.append(champion_name)
                result_ls.append(result)
                kills_ls.append(kills)
                deaths_ls.append(deaths)
                assists_ls.append(assists)
                kda_ls.append(kda)
                position_ls.append(position)
                summoner_name_ls.append(summoner_name)



                print(f'매치 기록 : {match_id[i]}\n'
                      f'챔피언 이름 :{champion_name} \n'
                      f'승리 패배 : {result}\n'
                      f'킬 : {kills}\n'
                      f'데스 : {deaths}\n'
                      f'어시스트 : {assists}\n'
                      f'kda : {kda},\n'
                      f'라인 : {position}\n'
                      f'닉네임 : {summoner_name}\n')



        return [summoner_name_ls, puuid_ls, match_id_ls, champion_name_ls, result_ls, kills_ls, deaths_ls, assists_ls, kda_ls, position_ls]

    def match_list(self):
        pass


    def all_death_time(self, matchid):
        time_line = watcher.match.timeline_by_match(my_region, matchid)
        death_list = list()
        for i in range(len(time_line['info']['frames'])):
            for j in range(len(time_line['info']['frames'][i]['events'])):
                if time_line['info']['frames'][i]['events'][j]['type']  == 'CHAMPION_KILL':
                   timestamp = time_line['info']['frames'][i]['events'][j]['timestamp']
                   death_list.append(timestamp)
        print(death_list)

    def user_death_time(self, matchid, puuid):
        time_line = watcher.match.timeline_by_match(my_region, matchid)
        death_list = list()
        puuid_list = time_line['metadata']['participants']
        in_game_id = [i for i in range(len(puuid_list)) if puuid_list[i] == puuid]

        for i in range(len(time_line['info']['frames'])):
            for j in range(len(time_line['info']['frames'][i]['events'])):
                if time_line['info']['frames'][i]['events'][j]['type']  == 'CHAMPION_KILL':
                    if time_line['info']['frames'][i]['events'][j]['victimId'] == in_game_id[0] :
                       timestamp = time_line['info']['frames'][i]['events'][j]['timestamp']
                       death_list.append(timestamp)
        print(death_list)



if __name__ == '__main__':
    # name = ApiHistory().summoner('hideonbush')
    # puuid = name['puuid']
    # match_id = ApiHistory().match_id(name['puuid'])
    ApiHistory().play_list('hideonbush')
    # Name().all_death_time(match_id[0])
    # Name().user_death_time(match_id[0], puuid)