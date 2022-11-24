import requests
import json
from datetime import datetime, timedelta
from pytz import timezone, utc

headers = {
	"X-RapidAPI-Key": "4ec7c9af6cmsh5ed7b801eba75c6p11176cjsn1a906fdacaf9",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

# Returns previous, current, and upcoming nba games for 
def getNBAGames():
    url = "https://api-nba-v1.p.rapidapi.com/games"
    
    today = datetime.today()
    dates_list = [today-timedelta(days=1), 
                  today, 
                  today+timedelta(days=1)]
    print(dates_list)
    
    # Glitch in api requires day forward
    f_dates = [{'date':(date + timedelta(days=1)).strftime('%Y-%m-%d')} 
               for date in dates_list]
    
    NBAgames = []
    for date in f_dates:
        # Get list of games with score and time
        response = (json.loads(requests.request("GET", url, headers=headers, params=date).text))['response']
        
        for game in response:
            unf_datetime = game['date']['start']
            unf_time = unf_datetime.replace('T',' ').split('.')[0]
            
            NBAgames.append(
                {'time':zeroToUTC(unf_time),
                 'teams':{'home':game['teams']['home']['name'],
                          'away':game['teams']['visitors']['name']},
                 'score':{'home':game['scores']['home']['points'],
                          'away':game['scores']['visitors']['points']},
                 'status':game['status']['long'],
                 'clock':game['status']['clock'],
                 'halftime':game['status']['halftime']
                 })
    return NBAgames  



def getNBAGamesFuck():
    return [{'time': '2022-11-22 19:30:00', 'teams': {'home': 'Philadelphia 76ers', 'away': 'Brooklyn Nets'}, 'score': {'home': 115, 'away': 106}, 'status': 'Finished', 'clock': None, 'halftime': False},
            {'time': '2022-11-22 20:00:00', 'teams': {'home': 'Memphis Grizzlies', 'away': 'Sacramento Kings'}, 'score': {'home': 109, 'away': 113}, 'status': 'Finished', 'clock': None, 'halftime': False},
            {'time': '2022-11-22 21:00:00', 'teams': {'home': 'Denver Nuggets', 'away': 'Detroit Pistons'}, 'score': {'home': 108, 'away': 110}, 'status': 'Finished', 'clock': None, 'halftime': False},
            {'time': '2022-11-22 22:00:00', 'teams': {'home': 'Phoenix Suns', 'away': 'Los Angeles Lakers'}, 'score': {'home': 115, 'away': 105}, 'status': 'Finished', 'clock': None, 'halftime': False},
            {'time': '2022-11-23 19:00:00', 'teams': {'home': 'Charlotte Hornets', 'away': 'Philadelphia 76ers'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 19:00:00', 'teams': {'home': 'Cleveland Cavaliers', 'away': 'Portland Trail Blazers'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 19:00:00', 'teams': {'home': 'Indiana Pacers', 'away': 'Minnesota Timberwolves'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 19:30:00', 'teams': {'home': 'Atlanta Hawks', 'away': 'Sacramento Kings'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 19:30:00', 'teams': {'home': 'Boston Celtics', 'away': 'Dallas Mavericks'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 19:30:00', 'teams': {'home': 'Miami Heat', 'away': 'Washington Wizards'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 19:30:00', 'teams': {'home': 'Toronto Raptors', 'away': 'Brooklyn Nets'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 20:00:00', 'teams': {'home': 'Milwaukee Bucks', 'away': 'Chicago Bulls'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 20:00:00', 'teams': {'home': 'Oklahoma City Thunder', 'away': 'Denver Nuggets'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 20:00:00', 'teams': {'home': 'San Antonio Spurs', 'away': 'New Orleans Pelicans'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 21:00:00', 'teams': {'home': 'Utah Jazz', 'away': 'Detroit Pistons'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-23 22:00:00', 'teams': {'home': 'Golden State Warriors', 'away': 'LA Clippers'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None},
            {'time': '2022-11-25 17:00:00', 'teams': {'home': 'Charlotte Hornets', 'away': 'Minnesota Timberwolves'}, 'score': {'home': None, 'away': None}, 'status': 'Scheduled', 'clock': None, 'halftime': None}]

# Convert from UTC +0 to EST, convert 24hr to 12hr format
def zeroToUTC(zero):
    # Convert to datetime
    datetime_obj = datetime.strptime(zero, '%Y-%m-%d %H:%M:%S')
    tz_zero = utc.localize(datetime_obj)
    tz_utc = tz_zero.astimezone(timezone('US/Eastern'))
    f_tz_utc = tz_utc.strftime('%Y-%m-%d %I:%M %p')
    return f_tz_utc
            


