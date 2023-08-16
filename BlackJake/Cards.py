suite=("Heart", "Diamond","Ace","Spades")
rank=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,
        "Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":1}

class Cards():
    allCards=[]
    
    def __init__(self,suite,rank):
        self.suite=suite;
        self.rank=rank;
        self.value=values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suite}"
        