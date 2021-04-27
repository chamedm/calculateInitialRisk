from datetime import datetime

def main(reunion):
  subtotalRisk = 0
  totalRisk = 0
  numberOfUsers = len(reunion.users)
  usersRisk = getUsersFactor(numberOfUsers)
  durationRisk = getDurationFactor(reunion.duration)
  masksRisk = getMasksFactor(reunion.masks)
  openSpaceRisk = getOpenSpaceFactor(reunion.openSpace)

  subtotalRisk = usersRisk * durationRisk * masksRisk * openSpaceRisk

  if(subtotalRisk >= 1 and subtotalRisk <= 12):
    totalRisk = 1
  elif(subtotalRisk >13 and subtotalRisk<=24):
    totalRisk = 2
  elif(subtotalRisk > 24 and subtotalRisk <= 36):
    totalRisk = 3
  else:
    totalRisk = 4
  
  print(totalRisk)
  reunion.risk = totalRisk
  return reunion
  

class Reunion:
  def __init__(self, users, duration, masks, openSpace, registeredDate):
    self.registeredDate = datetime.strptime(registeredDate,"%d/%m/%y")
    self.users = users
    self.duration = duration
    self.masks = masks
    self.openSpace = openSpace
    self.risk = 0
  
  
def getUsersFactor(users):
  factor = 0
  if(users > 0 and users < 5):
    factor = 1
  elif(users >= 5 and users < 10):
    factor = 2
  elif(users >= 10 and users < 15):
    factor = 3
  elif(users >= 15 ):
    factor = 4
  return factor

def getDurationFactor(duration):
  factor = 0
  if(duration > 0 and duration < 30):
    factor = 1
  elif(duration >=30 and duration < 60):
    factor = 2
  elif(duration >= 60 and duration < 90):
    factor = 3
  elif(duration > 90):
    factor = 4
  return factor

def getMasksFactor(masks):
  factor = 0
  if(masks):
    factor = 1
  else:
    factor = 3
  return factor

def getOpenSpaceFactor(openSpace):
  factor = 0
  if(openSpace):
    factor = 1
  else: 
    factor = 3
  return factor




if(__name__ == "__main__"):
  r1 = Reunion( ["mariana@mail.com", "caro@mail.com", "dario@mail.com" ],20,True,True, "11/03/02") 
  # r2 = Reunion(15, 30, False, True)
  # r3 = Reunion(15, 60, True, False)
  # r4 = Reunion(20,90,False, False)
  main(r1)