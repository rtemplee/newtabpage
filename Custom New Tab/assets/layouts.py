import dash
from dash import html, dcc
import api.nba

def getNBAGamesDivList():
    NBAGames_div_list = []
    for game in api.nba.getNBAGames():
        
        # ifWin = {'home', 'away'}
        # if None not in game['score'].values():
        #     if game['score']['home'] > game['score']['away']:
        #         ifWin['home'] == True
        #     elif game['score']['home'] < game['score']['away']:
        #         ifWin['away'] == True
        # for team in ['home', 'away']:
        #     if ifWin['team'] == True:
        #         score_style = {'float':'right'}
        def setTeamStyle(style, score, side):
            if score['home'] == None:
                return style
            if score['home'] > score['away']:
                if side == 'home':
                    return style
                else:
                    return style | {'color':'rgb(148,148,148)'}
            else:
                if side == 'home':
                    return style | {'color':'rgb(148,148,148)'}
                else:
                    return style
                
        
        NBAGames_div_list.append(
            html.Div([
                html.Div(game['time'], className='game-header'),
                html.Div([
                    html.Div([
                        html.Span((game['teams'][x]).upper(), style=setTeamStyle(
                            {}, game['score'], x)),
                        html.Span(game['score'][x], style=setTeamStyle(
                            {'float':'right'}, game['score'], x))
                    ], className='team-info') for x in ['home', 'away']
                ], className='teams-container'),
                html.Div(game['status'], className='game-status'),
            ], className='game-container')
        )
        NBAGames_div_list.append(html.Div('-'))
    return NBAGames_div_list

hello_world = html.Div([
    html.Div([html.Div('Title', style={'color':'white'}), html.Div(getNBAGamesDivList())]), html.Div('middle'), html.Div('right')],
                       style={'display':'grid',
                           'grid-template-columns':'300px auto 300px'})


