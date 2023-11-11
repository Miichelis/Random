class Solution:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
    def addTwoNumbers(self):
        l1=self.l1
        l2=self.l2
        sL=[]
        c=0
        if len(l1) > len(l2):
            for i in range(len(self.l1)-len(l2)):
                l2.append(0)
        else:
            for i in range(len(l2)-len(l1)):
                l1.append(0)
        for i in range(len(l1)):
            if l1[i] + l2[i]+c < 10:
                sL.append(l1[i]+l2[i]+c)
                c=0
            elif l1[i]+l2[i]+c >= 10:
                sL.append(l1[i]+l2[i]-10+c)
                c=1
            if i == len(l1)-1 and c == 1:
                sL.append(c)
        return sL


S=Solution([9,9,9,9,9,9,9],[9,9,9,9])

print S.addTwoNumbers()
