
class Game():
   
     def __init__(self):
          self.gamecount=0
          self.gamescore=0
          self.scores=[]
          self.framescores=[]
          
          
     def addframe(self,num):
          if self.gamecount<10:
               self.scores.extend(num)
               self.gamecount+=1
          else:
               print "only 10 frames per game"
               
     def displayCount(self):
         print "Round %d" % self.gamecount
                
     def displayScore(self):
         a=', '.join(map(str,self.framescores))
         print "Frame Scores: %s" %a 
         print "Game Score: %d" % self.gamescore

     def is_spare(self, one,two):
         return one + two == 10

     def is_strike(self, one):
         return one == 10
     def calculatescore(self):
          i=0
          r=0
          while r<10:
               if self.is_strike(self.scores[i]):
                    framescore= 10 + self.scores[i+1]+ self.scores[i+2]
                    r+=1
                    i+=1
               elif self.is_spare(self.scores[i],self.scores[i+1]):
                    framescore=10+ self.scores[i+2]
                    r+=1
                    i+=2
               else:
                 framescore= self.scores[i]+ self.scores[i+1]
                 r+=1
                 i+=2
               self.gamescore+=framescore
               self.framescores.append(framescore)


class GameTest():

    def __init__(self):
         self.game = Game() #first demo
         self.second= Game() #for example demo 2
    def demo(self):
      self.game.addframe([1,2])
      self.game.addframe([10])
      self.game.addframe([5,4])
      self.game.addframe([7,3])
      self.game.addframe([10])
      self.game.addframe([10])
      self.game.addframe([1,4])
      self.game.addframe([6,2])
      self.game.addframe([7,3])
      self.game.addframe([10,3,7])
      self.game.calculatescore()
      self.game.displayScore()
      

j= GameTest()
j.demo()
     

     
                    


