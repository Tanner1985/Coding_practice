#Functions to convert a given value to metric and return the converted number
def InchesToCm(inches_converter):
        convertedInchs = inches_converter * 2.54
        return convertedInchs
def PoundsToKg(pounds_converter):
        convertedPounds = pounds_converter * .45
        return convertedPounds
def GalToLit(gallons_converter):
        convertedGals = gallons_converter * 3.9
        return convertedGals
def FahToCel(fahren_converter):
        convertedFah = (fahren_converter - 32) * 5/9
        return convertedFah
def milesToKm(miles_converter):
        convertedMiles = miles_converter * 1.6
        return convertedMiles