class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        valid = ["0","1","2","3","4","5","6","7","8","9","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
 
        while l<r:

            while l < r and s[r] not in valid:
                r -= 1

            while l < r and s[l] not in valid:
                l += 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1


        return True