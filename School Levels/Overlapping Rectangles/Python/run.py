#code
## Generic Rectangle R Definition:
# (x1,y1) . ________
#	  |	    |
#	  |_________|
#		    * (x2,y2)
## Solution
# A rectangle 'R1' is *not* overlapping another rectangle 'R2' if and only if it's meeting 
# any of the following conditions:
#  - Completely to the Right of R2 (R1.x1 > R2.x2)(C1)*
#  - Completely to the Left of R2 (R1.x2 < R2.x1)(C2)*
#  - Completely Above R2 (R1.y2 > R2.y1)(C3)*
#  - Completely Under R2 (R1.y1 < R2.y2)(C4)*
# Therefore, R1 *is* overlapping R2 is a true statement if and only if ~(C1 v C2 v C3 v C4)

# Generic Rectangle definition
class Rectangle:
    def __init__(self, args):
        args = list(filter(None, args.split(" ")))
        self.topLeftX=int(args[0])
        self.topLeftY=int(args[1])
        self.bottomRightX=int(args[2])
        self.bottomRightY=int(args[3])

    #Each of these methods return True if the position with regard to the input rectangle is met, False if otherwise
    def isToRightOf(self, otherRectangle):
        return self.topLeftX > otherRectangle.bottomRightX

    def isToLeftOf(self, otherRectangle):
        return self.bottomRightX < otherRectangle.topLeftX

    def isAbove(self, otherRectangle):
        return self.bottomRightY > otherRectangle.topLeftY

    def isUnder(self, otherRectangle):
        return self.topLeftY < otherRectangle.bottomRightY

    #This method will return 1 or 0 based on the condition for an overlapping rectangle with regard to the input rectangle
    def overlaps(self, r):
        return (1 if not((self.isToRightOf(r)) or (self.isToLeftOf(r)) or (self.isAbove(r)) or (self.isUnder(r))) else 0)

#Main code block    
for x in range(0,int(input())):
    r1=Rectangle(input())
    r2=Rectangle(input())
    print(r1.overlaps(r2))
