class ListNode:
    def __init__(self, val, prev, next):
        self.prev = prev
        self.next = next
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        node = ListNode(val=homepage, prev=None, next=None)
        self.curr = node
        

    def visit(self, url: str) -> None:
        new_node = ListNode(val=url, prev=self.curr, next= None) # new node previous points to curr, next points none
        self.curr.next = new_node
        self.curr = new_node

        

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev != None and i < steps:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val


        

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next != None and i < steps:
            self.curr = self.curr.next
            i += 1
        return self.curr.val


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)