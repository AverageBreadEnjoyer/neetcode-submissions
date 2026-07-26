class ListNode:
    def __init__(self, value: str, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.tail = node
        
        
    def visit(self, url: str) -> None:
        new_node = ListNode(url, None, self.tail)
        self.tail.next = new_node
        self.tail = new_node
        
    
        
    def back(self, steps: int) -> str:
        i = 0
        while self.tail.prev != None:
            self.tail = self.tail.prev 
            i += 1
            if i == steps:
                break
            
        return self.tail.value


    def forward(self, steps: int) -> str:
        i = 0 
        while self.tail.next != None:
            self.tail = self.tail.next
            i += 1
            if i == steps:
                break
        return self.tail.value

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)