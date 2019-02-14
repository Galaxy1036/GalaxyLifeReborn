import random


def handle_obtain_universe(command_data, answer_command_data):
    answer_command_data['friendCode'] = ''
    answer_command_data['events'] = []
    answer_command_data['promo'] = None

    answer_command_data['Universe'] = []

    # Profile part

    user_profile_data = {}
    user_profile_data['Profile'] = []

    user_profile_data['exp'] = '0.00'  # Player XP
    # As long as there's no saving we can give every player nearly unlimited resources, which basically creates a sandbox mode
    user_profile_data['DCCoins'] = 1000000  # Player Coins
    user_profile_data['DCMinerals'] = 1000000  # Player Minerals
    user_profile_data['DCCash'] = 1000000  # Player Chips
    user_profile_data['playerName'] = 'Starling'  # Player Name
    user_profile_data['DCWorldName'] = 'YourPlanet'  # Player World Name
    user_profile_data['flags'] = 'flags_unknown'
    user_profile_data['DCPlayerRank'] = 1
    user_profile_data['DCDroids'] = 5  # Player worker count
    user_profile_data['tutorialCompleted'] = 1
    user_profile_data['damageProtectionTimeLeft'] = 86400000  # Time as milliseconds
    user_profile_data['damageProtectionTimeTotal'] = 86400000  # Time as milliseconds
    user_profile_data['lastVisitTime'] = 0
    user_profile_data['lastLevelNotified'] = 0
    user_profile_data['score'] = 0

    profile_data = {}

    profile_data['Missions'] = []

    missions_types = ['ReadyToStart', 'Available', 'Unlocked', 'Rewarded', 'Completed', 'Params']
    mission = {}

    for mission_type in missions_types:
        mission[mission_type] = {}

    mission['chunk'] = ''
    profile_data['Missions'].append(mission)

    profile_data['Targets'] = None
    profile_data['baseCoinsAndMineralsCapacity'] = 1000000

    profile_data['Planets'] = []

    planet = {}

    planet['sku'] = '0:0:0'
    planet['planetId'] = 0
    planet['capital'] = 1
    planet['HDLevel'] = 1
    planet['starName'] = 'YourStar'
    planet['starId'] = 0
    planet['starType'] = 0
    planet['planetType'] = random.randint(0, 7)  # Give the player a random planet type each type he logs in
    planet['coinsLimit'] = 0
    planet['mineralsLimit'] = 0

    profile_data['Planets'].append(planet)

    user_profile_data['Profile'].append(profile_data)

    user_profile_data['expendables'] = None

    answer_command_data['Universe'].append(user_profile_data)
