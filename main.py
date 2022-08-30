class Planet:
    def __init__(self, name, gases, no_of_moons, has_ring):
        self.name = name
        self.gases = gases or []
        self.moons = no_of_moons
        self.has_ring = has_ring
    
    def __str__(self):
        return f"Name : {self.name}, Gases : {self.gases}, Number of moons : {self.moons}, Has Ring : {self.has_ring}"

# count of moon with ring or without ring
def count_of_moons_for_planet(planet_list, has_ring=True):
    planet_list = planet_list or []
    moon_count = 0
    for planet in planet_list:
        if planet.has_ring == has_ring:
            moon_count = moon_count + planet.moons
    
    return moon_count
    
# Most common gases
def most_common_gases(planet_list):
    data = dict()
    planet_list = planet_list or []
    for planet in planet_list:
        for gas in planet.gases:
            data[gas] = data.get(gas, 0) + 1
    max_key = max(data, key=data.get)
    
    return max_key

if __name__ == '__main__':
    # Planet data init
    all_planets = []
    all_planets.append(Planet("Mercury", [], 0, False))
    all_planets.append(Planet("Venus", ["Carbon Dioxide", "Nitrogen"], 0, False))
    all_planets.append(Planet("Earth", ["Nirogen", "Oxygen"], 1, False))
    all_planets.append(Planet("Jupitor", ["Hydrogen", "Helium"], 79, True))
    all_planets.append(Planet("Saturn", ["Hydrogen", "Helium"], 83, True))
    all_planets.append(Planet("Uranus", ["Hydrogen", "Helium", "Methane"], 27, True))
    
    
    # printing all planets
    for planet in all_planets:
        print(planet)
        
    
    # get moons for the planet with rings
    print("moons for the planet with ring : ",count_of_moons_for_planet(all_planets))
    # get moons for the planet without rings
    print("moons for the planet without rings : ",count_of_moons_for_planet(all_planets, has_ring=False))
    # get the most common gas from all planets
    print("most common gas from all planets : ", most_common_gases(all_planets))
