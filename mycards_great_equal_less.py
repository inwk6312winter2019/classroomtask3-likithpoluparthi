class Card():
  suitname=["Clubs",'Diamonds','Hearts','spades']
  rankname=[None,'Ace','2','3','4','5','6','7','8','9','Jack','Queen','King']
  def __init__(self,rank=0,suit=2):
    self.rank=rank
    self.suit=suit
  def __str__(self):
    return ("the card is {} and the suit is {}".format(Card.rankname[self.rank],Card.suitname[self.suit])) 
  def __lt__(self,other):
    if self.suit>other.suite:
      return True
    else:
      return False
  def __rt__(self,other):
    if self.suite<other.suite:
      return True
    else:
      return False
  def __eq__(self,other):
    if self.suite == other.suite:
      return True
ace_of_spades=Card(1,3)
print(ace_of_spades)
