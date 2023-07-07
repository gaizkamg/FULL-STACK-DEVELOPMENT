teams = {
  "astros": ["Altuve", "Correa", "Bregman"], #we store a List inside a dictionary 
  "player1": 'Gaizka',
}

print(teams['astros'])
print(teams['astros'][2]) #we can choose wich element
print(teams['player1'])
team_select= teams['astros'][:2]
team_select2= teams['player1']
print(team_select)
print(team_select2)

teams['nuevo']='Keanu' #adding a new key
print(teams)

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team = teams.get('meths', 'No featured team') #we can use this for searching for some key and not get an error if the key doesn't exists.

print(featured_team)

