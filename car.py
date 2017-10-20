class Car(object):
  
  def __init__(self, name="General", model="GM", Type = None, 
  												 num_of_doors = 4,
  												 num_of_wheels = 4,
  												 speed = 0):
    self.model = model
    self.name = name
    self.Type = Type
    self.num_of_doors = num_of_doors
    self.num_of_wheels = num_of_wheels
    if self.name == "Porshe" or self.name == "Koenigsegg":
    	self.num_of_doors = 2
    if self.Type == "trailer":
    	self.num_of_wheels = 8
  def is_saloon(self):
  	if self.Type != "trailer":
  		return True
  	return False
