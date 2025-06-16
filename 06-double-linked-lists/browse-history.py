class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.current = homepage

    def visit(self, url: str) -> None:
        self.history.append(self.current)
        self.current = url
        self.future = []

    def back(self, steps: int) -> str:
        num_steps = steps if steps < len(self.history) else len(self.history)
        for step in range(num_steps):
            self.future.append(self.current)
            self.current = self.history[-1]
            self.history.pop()
        return self.current

    def forward(self, steps: int) -> str:
        num_steps = steps if steps < len(self.future) else len(self.future)
        for step in range(num_steps):
            self.history.append(self.current)
            self.current = self.future[-1]
            self.future.pop()
        return self.current

if __name__ == "__main__":
    obj = BrowserHistory('leetcode.com')
    obj.visit('google.com')
    obj.visit('facebook.com')
    obj.visit('youtube.com')

    obj.back(1)
    obj.back(1)
    obj.forward(1)

    obj.visit('linkedin.com')

    obj.forward(2)
    obj.back(2)
    obj.back(7)