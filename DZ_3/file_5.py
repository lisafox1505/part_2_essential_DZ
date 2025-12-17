from example_7 import Shape

class Cone(Shape):
    def draw(self):
        self.draw1.polygon([(250, 100), (150, 350), (350, 350)], fill='orange', outline='black')
        self.draw1.ellipse((150, 308, 350, 408), fill='orange', outline='black')

    def erase(self):
        self.draw1.polygon([(250, 100), (150, 350), (350, 350)], fill=self.back_color, outline=self.back_color)
        self.draw1.ellipse((150, 308, 350, 408), fill=self.back_color, outline=self.back_color)

    def save(self):
        print("Image with cone was created")
        return self.im.save('draw-cone.png', quality=95)

class Paraboloid(Shape):
    def draw(self):
        self.draw1.chord((150, 150, 350, 450), start=0, end=180, fill='violet',outline='black')
        self.draw1.ellipse((150, 280, 350, 320), fill='violet', outline='black')

    def erase(self):
        self.draw1.chord((150, 150, 350, 450), start=0, end=180, fill=self.back_color, outline=self.back_color)
        self.draw1.ellipse((150, 280, 350, 320), fill=self.back_color, outline=self.back_color)

    def save(self):
        print("Image with cone was created")
        return self.im.save('draw-paraboloid.png', quality=95)


cone = Cone()
cone.draw()
cone.save()
cone.erase()
cone.save()
paraboloid = Paraboloid()
paraboloid.draw()
paraboloid.save()
paraboloid.erase()
paraboloid.save()