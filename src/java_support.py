from src.lib_for_java import *
from src.lib_usual import *

def java_class(jar_path, class_name):
    jarpath = os.path.join(os.path.abspath(".."), jar_path)
    jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jarpath)
    JavaClass = jpype.JClass(class_name)
    return JavaClass()
    