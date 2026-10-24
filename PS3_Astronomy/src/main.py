
sr = 696000
er = 6371
yr=365.25 #1 year = 365.25days
au=149600000
#period
s1=4
s2=80
s3=40


#luminosity
ls1=1.00
ls2=0.40
ls3=0.08

#brightness dip
s1dip = 0.9970
s2dip = 0.9990
s3dip = [0.9990, 0.9992, 0.9991, 0.9993, 0.9990]
#radius
s1r = 1.00
s2r = 0.80
s3r = 0.50
#mass
s1mass=1.00 #times mass of sun
s2mass=0.80
s3mass=0.50



def depth(dips, normal=1.0000):
    s = 0

    if isinstance(dips, list):
        for i in dips:
            x = (normal - i) / normal
            s += x

        return s / len(dips)

    else:
        return (normal - dips) / normal


def planetsize(starR, td):
    starradius = starR * sr
    planet = starradius * (td ** 0.5)

    return planet, planet / er


def classifyplanet(radius):
    earth_radii = radius[1]

    if earth_radii <= 1.25:
        return "Earth-sized"
    elif earth_radii <= 2:
        return "Super-Earth"
    elif earth_radii <= 6:
        return "Neptune-sized"
    else:
        return "Jupiter-sized"

def energy_received(luminosity, orbital_distance):
    return luminosity / (orbital_distance ** 2)

def orbitaldis(hostmass,orbperiod):
    period=orbperiod/yr
    orbdis=(hostmass*((period)**2))**(1/3)
    return orbdis

def habitable(l):
    return l**0.5

def hz_ratio(orbital_distance, luminosity): #more the better
    hz_distance = habitable(luminosity)
    return orbital_distance / hz_distance


for name, starR, dip ,mass,period,lum in [
    ("STAC-1", s1r, s1dip,s1mass,s1,ls1),
    ("STAC-2", s2r, s2dip,s2mass,s2,ls2),
    ("STAC-3", s3r, s3dip,s3mass,s3,ls3)
]:
    td = depth(dip)
    radius = planetsize(starR, td)
    distance = float(f"{orbitaldis(mass, period):.3f}")
    ratio = hz_ratio(distance, lum)
    energy = energy_received(lum, distance)
    print(f"\n{name}")
    print(f"Transit depth: {td:.6f}")
    print(f"Planet radius: {radius[0]:.2f} km")
    print(f"Earth radii: {radius[1]:.2f} ER")
    print(f"Classification: {classifyplanet(radius)}")
    print(f"Orb Distance : {orbitaldis(mass,period):.3f} AU")
    print(f"Orb Distance in km : {(orbitaldis(mass,period)*au):.3f} km")
    print(f"Earth's orbital distance is {1 / orbitaldis(mass, period):.3f} times the planet's orbital distance")
    print(f"Habitable zone reference distance {habitable(lum):.3f} AU")
    print(f"{name} H/Z ratio : {ratio:.2f}")
    print(f"Energy received: {energy:.2f} times Earth's")