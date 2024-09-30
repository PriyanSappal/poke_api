import requests
import json
import random
import time

# Get the list of Pokémon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a Pokémon
print('Enter your Pokémon:')
choice = input().lower()

# Get the user's Pokémon data from the API
url = f'https://pokeapi.co/api/v2/pokemon/{choice}/'
response = requests.get(url)
pokemon_data = json.loads(response.text)

# Extract height, weight, and stats
player_height = int(pokemon_data['height']) / 10  # in meters
player_weight = int(pokemon_data['weight']) / 10  # in kg
player_hp = next(stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'hp')
player_attack = next(stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'attack')

# Print the user's Pokémon data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {} (kgs)'.format(player_weight))
print('Height: {} (m)'.format(player_height))
print('HP: {}'.format(player_hp))
print('Attack: {}'.format(player_attack))

# Randomly select a Pokémon for the CPU (from Gen 1)
cpu_pokemon_id = random.randint(1, 151)
url = f'https://pokeapi.co/api/v2/pokemon/{cpu_pokemon_id}/'  # Direct API call for CPU
response = requests.get(url)
cpu_pokemon_data = json.loads(response.text)

# Extract height, weight, and stats for CPU
cpu_height = int(cpu_pokemon_data['height']) / 10  # in meters
cpu_weight = int(cpu_pokemon_data['weight']) / 10  # in kg
cpu_hp = next(stat['base_stat'] for stat in cpu_pokemon_data['stats'] if stat['stat']['name'] == 'hp')
cpu_attack = next(stat['base_stat'] for stat in cpu_pokemon_data['stats'] if stat['stat']['name'] == 'attack')

# Print the CPU's Pokémon data
print(f"\nCPU chose {cpu_pokemon_data['name'].capitalize()}:")
print(f'Name: {cpu_pokemon_data["name"].capitalize()}')
print(f'Weight: {cpu_weight} kg')
print(f'Height: {cpu_height} m')
print(f'HP: {cpu_hp}')
print(f'Attack: {cpu_attack}')

print(f"Your {pokemon_data['name'].capitalize()} VS my {cpu_pokemon_data['name'].capitalize()}! Let's fight!")
time.sleep(4)
while player_hp > 0 and cpu_hp > 0:
    cpu_hp -= player_attack
    print(f"Your {pokemon_data['name'].capitalize()} attacks {cpu_pokemon_data['name'].capitalize()} and "
          f"deals {player_attack} damage! CPU HP is now {cpu_hp}!")

    if cpu_hp <= 0:
        print(f"Your {pokemon_data['name'].capitalize()} wins!")
        break
    time.sleep(4)

    player_hp -= cpu_attack
    print(f"My {cpu_pokemon_data['name'].capitalize()} attacks {pokemon_data['name'].capitalize()} and deals "
          f"{cpu_attack} damage! Player HP is now {player_hp}!")

    if player_hp <= 0:
        print(f"My {cpu_pokemon_data['name'].capitalize()} wins!")
    time.sleep(4)