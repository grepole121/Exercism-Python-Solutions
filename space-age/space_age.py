class SpaceAge:
    RATIOS = [(planet, ratio * 31557600) for planet, ratio in (
        ('earth', 1.0),
        ('mercury', 0.2408467),
        ('venus', 0.61519726),
        ('mars', 1.8808158),
        ('jupiter', 11.862615),
        ('saturn', 29.447498),
        ('uranus', 84.016846),
        ('neptune', 164.79132)
    )]

    def __init__(self, seconds):
        self.s = seconds
        for planet, ratio in self.RATIOS:
            space_years = lambda ratio=ratio: round(seconds / ratio, 2)
            setattr(self, "on_" + planet, space_years)