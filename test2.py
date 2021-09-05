from test import myClass

ins = myClass()
ins.add_instance_method(3,5)
myClass.add_instance_method(3,5)       #Error
myClass.add_instance_method(ins,3,5)
myClass.add_instance_method(None,3,5)

myClass.add_class_method(3,5)
myClass.add_class_method(myClass,3,5) #Error
ins.add_class_method(3,5)

myClass.add_static_method(3,5)
ins.add_static_method(3,5)

from test import childClass

a = childClass.add_static_method(3,5)



