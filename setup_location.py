from location import Location
from boss import Boss



def setup_locations() -> Location:
    """Crée les différents lieux et leurs connexions et retourne le point de départ."""
    cave = Location("Caverne Humide", "Une odeur de moisissure emplit l'air.")
    lake = Location("Lac Mystique", "L'eau scintille sous la lumière de la lune.")
    village = Location("Village de la Terre", "Des gens vieillissants et en peine de vivre.")
    desert = Location("Désert Froid", "Des arbres géants et des rochers couvrent le sol.")
    ruins = Location("Ruines Anciennes", "Des ruines massives et étroites.")
    mountain = Location("Montagne Épaisse", "Des massifs de pierre et de roches.")
    swamp = Location("Marais Étroit", "Des plantes et des animaux vivent à la surface.")
    boss_location = Location("Caverne du Boss", "Une caverne sombre où réside une créature maléfique.", has_boss = True)
    forest = Location("Forêt Sombre", "Des arbres denses vous entourent.")
    
    # Paramétrage pour le boss
    boss = Boss("MATHIAS SOW", "Une créature massive avec des yeux brûlants.", 200, 25, 10)

    # Connexions entre les lieux
    forest.north = cave
    forest.east = lake
    forest.south = village
    forest.west = swamp

    cave.south = forest
    lake.west = forest
    village.north = forest
    village.east = desert
    swamp.east = forest

    desert.west = village
    desert.north = ruins

    ruins.south = desert
    ruins.west = mountain
    ruins.north = boss_location  # Connexion au boss

    mountain.east = ruins
    mountain.south = swamp

    swamp.north = mountain

    # Paramétrage pour le boss
    boss_location.boss = boss

    # Retourner le lieu de départ (Forêt Sombre)
    return forest

