import numbers


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def addTwoNumbersSlow(self, l1:ListNode,l2:ListNode)->ListNode:
        number1:int
        number1=0
        power=0
        while l1:
            number1=l1.val*10**power+number1
            power=power+1
            l1=l1.next
        power=0
        number2:int
        number2=0
        while l2:
            number2=l2.val*10**power+number2
            power=power+1
            l2=l2.next

        number3=number1+number2
        dummy=ListNode()
        head=dummy
        while number3>0:
            dummy.val=number3%10
            number3=number3//10
            if number3>0:
                dummy.next=ListNode()
                dummy=dummy.next
        return head

    def addTwoNumbers(self, l1:ListNode,l2:ListNode)->ListNode:
        dummy=ListNode();
        head=dummy;
        carry=0;
        while l1 or l2 or carry:
            number1=l1.val if l1 else 0;
            number2=l2.val if l2 else 0;
            total=number1+number2+carry;

            carry=total//10;
            total=total%10;

            dummy.next=ListNode(total);
            dummy=dummy.next;
            l1=l1.next if l1 else None;
            l2=l2.next if l2 else None;
        return head.next;           

if __name__=="__main__":
    s=Solution();

    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)

    l2=ListNode(5)
    l2.next=ListNode(6)
    l2.next.next=ListNode(4)

    head=s.addTwoNumbers(l1,l2);
    while head:
        print(head.val)
        head=head.next