#https://leetcode.com/problems/design-browser-history/description/
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.backStack = []
        self.forwardStack = []
        self.cur = homepage

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.backStack.append(self.cur)
        self.cur =url
        self.forwardStack = []
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and len(self.backStack) > 0:
            self.forwardStack.append(self.cur)
            self.cur = self.backStack.pop()
            steps-=1
        return self.cur
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and len(self.forwardStack) > 0 :
            self.backStack.append(self.cur)
            self.cur = self.forwardStack.pop()
            steps-=1
        return self.cur

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)