class Solution:
    def sortArray(self, mylist: List[int]) -> List[int]:
        n = len(mylist)
        for i in range(n-1):
            for j in range(n-i-1):
                if mylist[j] > mylist[j+1]:
                    mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

        return(mylist)