from task1 import yml_parser as parser_1
from task2 import yml_parser as parser_2
from task3 import yml_parser as parser_3
from timeit import timeit

class Tests:
    f = "schedule.yml"
    def test_1():
        parser_1(Tests.f)
    def test_2():
        parser_2(Tests.f)
    def test_3():
        parser_3(Tests.f)

print(timeit(Tests.test_1, number=100))
print(timeit(Tests.test_2, number=100))
print(timeit(Tests.test_3, number=100))

