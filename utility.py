def gameWin(computer,name):
    if computer == name:
        return None

#Check for all possibilities when computer choose S
    elif computer == 's':
        if name == 'w':
          return False
        elif name == 'g':
          return True

#check for all possibilities when computer choose W
    elif computer == 'w':
      if name == 'g':
        return False
      elif name == 's':
        return True
#check for all possibilities when computer choose G
    elif computer == 'g':
     if name == 's':
        return False
     elif name == 'w':
        return True
