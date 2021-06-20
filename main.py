from pprint import pprint


# Task #1

class Stack:

    def __init__(self):
        self.storage = []

    def isEmpty(self):
        if not self.storage:
            return True
        return False

    def push(self, element):
        self.storage.append(element)

    def pop(self):
        if self.storage:
            return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def size(self):
        return len(self.storage)


# Task #2

class Balancer:

    def __init__(self, test_string):
        self.bracket = {'(': ')',
                        '[': ']',
                        '{': '}'}
        self.stack = Stack()
        self.test_string = test_string

    def balance(self):
        for elem in self.test_string:
            if elem in self.bracket.keys():
                self.stack.push(elem)

            if elem in self.bracket.values():
                if self.bracket.get(self.stack.pop()) != elem:
                    self.stack.push(None)
                    break
        msg = 'Сбалансировано' if self.stack.isEmpty() else 'Не сбалансировано'
        return msg


if __name__ == '__main__':

    test_strings = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]',

    ]

    result = []
    for ts in test_strings:
        result.append([ts, Balancer(ts).balance()])

    pprint(result)