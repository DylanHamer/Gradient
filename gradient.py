"""
GradientGenerator
Generate a gradient between two color points
By Dylan Hamer
"""

def rgbToHex(r, g, b):
    """Convert RGB to six digit hex"""
    if r <= 255 and g <= 255 and b <= 255:
        colorHex = "#%02x%02x%02x" % (r, g, b)
    else:
        raise ValueError("Values can not be more than 255")
    return colorHex
    
def genGradient():
    for r in range(255):
        for g in range(255):
            for b in range(255):
                colorRGB = (r, g, b)
                colorHex = rgbToHex(r, g, b)
                print(colorHex)
        
genGradient()
