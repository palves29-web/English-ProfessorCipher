import os

class GenerateCodes():
  def __init__(self):
    self.GeneratedList = []
    self.List = []
  def Generate(self, filepath: str):
    with open(filepath, 'r') as file:
      self.List = file.read().split(",")
    print(self.List)
