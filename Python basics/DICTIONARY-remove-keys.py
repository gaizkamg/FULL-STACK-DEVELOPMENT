teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['angels'] #if the key doesn't exist it will give us an error
removed_team = teams.pop('red sox', 'Team not found')

print(teams)
print(removed_team)