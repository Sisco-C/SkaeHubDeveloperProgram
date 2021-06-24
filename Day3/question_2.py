import numpy 
class Compute:
    end=0
    begin =0
    def __init__(self):
      self.month = int(input("input the month:\n"))
      self.year = int(input("input the year:\n"))

    def display(self):
      if self.month == 12:
        self.end = str(self.year)+'-'+str(self.month)+'-31'
        self.begin = str(self.year)+'-'+str(self.month)+'-01'
        self.date = 1
      else:
  
        # single digit months
        if self.month < 10:
            self.endM = '-0'+str(self.month+1)
            self.beginM = '-0'+str(self.month)
  
        # double digit months
        else:
            self.endM = '-'+str(self.month+1)
            self.beginM = '-'+str(self.month)
  
        self.end = str(self.year)+self.endM+'-01'
        self.begin = str(self.year)+self.beginM+'-01'
    def disp(self):
         return (numpy.datetime64(numpy.datetime64(self.end) - numpy.datetime64(self.begin)+self.date).astype(numpy.longlong))
cup = Compute()
cup.disp()