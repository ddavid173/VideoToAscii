class frame(object):
    def __init__(self, rgb):
        self.rgb = rgb
        self.printible = ''
        self.grey = []
        self.ascii = []
        asciiConversion = [' ', '.','o', 'O','0','&','@']
        for x in range(len(rgb)):
            self.grey.append([])
            self.ascii.append([])
            for y in rgb[x]:
                greys = int(0.21 * y[0] + 0.72 * y[1] + 0.07 * y[2])
                ascii = asciiConversion[int(greys / 42)]
                self.grey[x].append(greys)
                self.ascii[x].append(ascii)
    
    def rendered(self):
        return (len(self.printible) > 0)
    
    def render(self):
        string = ''
        for x in range(len(self.ascii)):
            for y in self.ascii[x]:
                string += y
            string += '\n'
        self.printible += string

    def __str__(self):
        if self.rendered():
            return self.printible
        else:
            return 'Not Rendered'