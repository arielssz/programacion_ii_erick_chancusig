class RadarDragon:
    def __init__(self, region1, region2):
        self.region1 = region1
        self.region2 = region2

    def buscar_esferas(self):
        encontradas = self.region1 + self.region2
        faltan = 7 - encontradas

        print("Esferas encontradas:", encontradas)
        print("Esferas que faltan:", faltan)

radar_bulma = RadarDragon(3, 2)
radar_bulma.buscar_esferas()