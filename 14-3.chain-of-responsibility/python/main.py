"""
@责任链模式

@一段没有灵魂的说明代码
"""

import abc

class Handler(abc.ABC):
    def __init__(self, successor):
        self.successor = successor

    @abc.abstractmethod
    def handleRequest(self, input_list):
        """ handle request """

class FilterA(Handler):
    def handleRequest(self, input_list):
        if len(input_list):
            input_list = [i for i in input_list if i != 'A']
        if self.successor:
            return self.successor.handleRequest(input_list)
        else:
            return input_list

class FilterB(Handler):
    def handleRequest(self, input_list):
        if len(input_list):
            input_list = [i for i in input_list if i != 'B']
        if self.successor:
            return self.successor.handleRequest(input_list)
        else:
            return input_list

class FilterC(Handler):
    def handleRequest(self,input_list):
        if len(input_list):
            input_list = [i for i in input_list if i != 'C']
        if self.successor:
            return self.successor.handleRequest(input_list)
        else:
            return input_list

class FilterChain(Handler):
    """ 将以上各个节点串起来，方便添加管理 """

    def_filter = [FilterA, FilterB, FilterC]

    def __init__(self):
        self.filter = None
        for filterCls in reversed(self.def_filter):
            self.filter = filterCls(self.filter)

    def handleRequest(self, input_list):
        return self.filter.handleRequest(input_list)

if __name__ == "__main__":
    filterx = FilterChain()
    print(filterx.handleRequest('xAxBxC'))