class multifilter():
  
    def judge_half(pos, neg):
        return pos >= neg # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg) 
    
    def judge_any(pos, neg): 
        return pos >= 1 # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
     
    def judge_all(pos, neg):
        return neg == 0 # допускает элемент, если его допускают все функции (neg == 0)
    
    def __init__(self, iterable, *funcs, judge=judge_any): 
        self.result = []
        self.judge = judge
        self.iterable = iterable
        for i in self.iterable:
            if self.judge(*Counter(i, funcs).posneg):
                self.result.append(i)
    
    def __iter__(self): 
        yield from self.result # возвращает итератор по результирующей последовательности
    
class Counter():
    def __init__(self, el, funcs):
        self.el = el
        self.pos = 0
        self.neg = 0
        for i in funcs:
            if i(el):
                self.pos += 1
            else: self.neg += 1
        self.posneg = self.pos, self.neg
