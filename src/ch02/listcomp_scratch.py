symbols = '$#**$&@'
codes = [ord(c) for c in symbols]
print(codes);

colors = ['black', 'white', 'blue']
sizes = ['S', 'M', 'L']

shirts = [(color, size) for color in colors
                        for size in sizes]
print(shirts, sep='\n')
