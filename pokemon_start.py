import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))


# Randomly select a Pokémon for the CPU (from Gen 1)
cpu_pokemon_id = random.randint(1, 151)
url = f'https://pokeapi.co/api/v2/pokemon/{cpu_pokemon_id}/'
response = requests.get(url)
cpu_pokemon_data = json.loads(response.text)

# To get ability for CPU
cpu_abilities = cpu_pokemon_data['abilities'][0]
cpu_ability = cpu_abilities['ability']

# To format height and weight properly for CPU
cpu_height = int(cpu_pokemon_data['height']) / 10  # in meters
cpu_weight = int(cpu_pokemon_data['weight']) / 10  # in kg

# Print the CPU's Pokémon data
print(f"\nCPU chose {cpu_pokemon_data['name'].capitalize()}:")
print(f'Name: {cpu_pokemon_data["name"].capitalize()}')
print(f'Weight: {cpu_weight} kg')
print(f'Height: {cpu_height} m')
print(f'Ability: {cpu_ability["name"].capitalize()}')
