class One:
    def __init__(self, *args, **kwargs):
        self.args = args

    def method(self):
        return self.args

    def func_dodatok(self):
        return(self.args + self.args)


class Two:
    def __init__(self, *args, **kwargs):
        self.args = args

    def method(self):
        return self.args

    def func_dodatok(self):
        return(self.args + self.args)

class Three:
    def __init__(self, *args, **kwargs):
        self.args = args
    def method(self):
        return self.args

class Four:
    def __init__(self, *args, **kwargs):
        self.args = args

    def m(self):
        return self.args


obj_one = One(1, 'one', 3434343)
obj_two = Two(2, 'two')
obj_three = Three(3, 'three')
obj_four = Four(4, 'four')

lst_objs = [obj_one, obj_two, obj_three, obj_four]
def my_func(*classes):
    lst_objs_new = []
    lst_for_func_dodatok = []
    for i in lst_objs:
        for cls in classes:
            if isinstance(i, cls):
                dict_method = dict.fromkeys([cls.__name__], i.method())
                lst_objs_new.append(dict_method)
                if isinstance(i, One):
                    dict_method = dict.fromkeys([cls.__name__], i.func_dodatok())
                    lst_for_func_dodatok.append(dict_method)
                elif isinstance(i, Two):
                    dict_method = dict.fromkeys([cls.__name__], i.func_dodatok())
                    lst_for_func_dodatok.append(dict_method)
                    break



    d_1 = {}
    for el in lst_objs_new:
        d_1.update(el)
    print(d_1)
    d_2 = {}
    for el in lst_for_func_dodatok:
        d_2.update(el)
    print(d_2)


f = my_func(One, Two, Three)


