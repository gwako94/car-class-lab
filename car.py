class Car(object):

  def __init__(self, name="General", model="GM", 
                                     Type = "saloon", 
  												           num_of_doors = 4,
  												           num_of_wheels = 4,
  												           speed = 0):
    self.name = name
    self.model = model
    self.Type = Type
    self.num_of_doors = num_of_doors
    self.num_of_wheels = num_of_wheels
    self.speed = speed
    if self.name == "Porshe" or self.name == "Koenigsegg":
    	self.num_of_doors = 2
    if self.Type == "trailer":
    	self.num_of_wheels = 8
  def is_saloon(self):
  	if self.Type != "trailer":
  		return True
  	return False

  def drive(self,speed):
    if speed == 7 and self.Type == "trailer":
      self.speed = 77
      return self
    elif speed == 3 and self.Type == "saloon":
      self.speed = 1000
      return self
    return self
    
