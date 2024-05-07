

import requests
import json
import pandas as pd


def call_api (pokemon):
    '''
    Takes a pokemon dex ID and makes the call to the api
    '''
    
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/').text
    response_info = json.loads(response)
    
    return response_info



def get_stats(pokemon):

    '''
    Takes a pokemon dex ID and calls the api. Then returns stats in a list
    '''
    
    poke_stats = call_api(pokemon)

    dex_id = pokemon
    name = poke_stats['name']
    type = poke_stats['types'][0]['type']['name'] 
    
    try:
        type2 = poke_stats['types'][1]['type']['name']
    except IndexError:
        type2 = 'N/A'    
        
    hp = poke_stats['stats'][0]['base_stat']
    attack = poke_stats['stats'][1]['base_stat']
    defense = poke_stats['stats'][2]['base_stat']
    sp_atk = poke_stats['stats'][3]['base_stat']
    sp_def = poke_stats['stats'][4]['base_stat']
    speed = poke_stats['stats'][5]['base_stat']
    
    
    return dex_id, name, type, type2, hp, attack, defense, sp_atk, sp_def, speed



def generation_df (start_dex, end_dex): 
    
    '''
    Takes a starting and ending dex ID to define a particular range of pokemon, for example the first generation would be 1-151.
    Then returns a dataframe containing stats for all pokemon in the defined range
    '''
    gen_list = []
    for i in range(start_dex, end_dex):
        gen_list.append(get_stats(i))
    col = ['dex_id', 'name', 'type', 'type_2', 'hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed']
    gen_df = pd.DataFrame(data=gen_list, columns = col)
    
    return gen_df


def team_df(p1,p2=0,p3=0,p4=0,p5=0,p6=0):
    
    '''
    Takes up to six pokemon dex IDs and returns dataframe of stats. A player can hold up to 6 pokemon on their team
    
    '''
    
    team_list = []
    id_list = [p1,p2,p3,p4,p5,p6]
    for i in id_list:
        if i > 0:
            team_list.append(get_stats(i))
    
    col = ['dex_id', 'name', 'type', 'type_2', 'hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed']
    team_df = pd.DataFrame(data=team_list, columns = col)
    return team_df