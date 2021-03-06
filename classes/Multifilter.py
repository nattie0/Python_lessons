'''
Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе 
два аргумента a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x 
из последовательности a, что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x, 
а элемент x является допущенным.

В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и 
стандартный класс filter, но будет использовать не одну функцию, а несколько.

Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент, и сколько 
не допускают. Обозначим эти количества за pos и neg.

Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает 
True, если элемент допущен, и False иначе.

Класс должен обладать следующей структурой:

class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
'''

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
