#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list
        self.__pi = 3.141  # private variable

    def area(self, radius):
        return self.__pi * (radius ** 2)

    def perimeter(self, radius):
        return 2 * self.__pi * radius

    def calculate(self):
        for radius in self.radius_list:
            circle_area = self.area(radius)
            circle_perimeter = self.perimeter(radius)
            print(f"Radius: {radius}, Area: {circle_area}, Perimeter: {circle_perimeter}")

# Test the Circle class
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
circle.calculate()


# In[2]:


class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.volume_level = 50

    def toggle_power(self):
        self.is_on = not self.is_on

    def set_channel(self, new_channel):
        if self.is_on and 1 <= new_channel <= 120:
            self.channel = new_channel

    def set_volume(self, new_volume_level):
        if self.is_on and 0 <= new_volume_level <= 100:
            self.volume_level = new_volume_level

    def channel_up(self):
        if self.is_on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.is_on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.is_on and self.volume_level < 100:
            self.volume_level += 1

    def volume_down(self):
        if self.is_on and self.volume_level > 0:
            self.volume_level -= 1

# Test the TV class
tv = TV()
print(tv.is_on)  # Output: False
tv.toggle_power()
print(tv.is_on)  # Output: True
print(tv.channel)  # Output: 1
tv.channel_up()
print(tv.channel)  # Output: 2
tv.set_channel(5)
print(tv.channel)  # Output: 5
tv.volume_up()
print(tv.volume_level)  # Output: 51


# In[ ]:




