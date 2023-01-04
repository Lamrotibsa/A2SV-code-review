class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        new=x
        val=0
        i=0
        while new>=1:

            num=new%10
            val=(val*10)+num
            new=new//10
            i+=1
            print(val)
        
        if val==x:
            return True
        else:
            return False
        
        
