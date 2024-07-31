# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
        if A is None or A.next is None:
            return A
        start=A.next
        prev=None
        curr=A
        nex=A.next
        while nex!=None:
            if prev!=None:
                prev.next=nex
            curr.next=nex.next
            nex.next=curr
            prev=curr
            curr=curr.next
            if curr==None:
                break
            else:
                nex=curr.next
        return start
                
                
                
            
            
