import os, sys, random, cmath, math
from typing import Union
from src.error_type import *

class HighPrecisionOperation:
    """高精度运算类"""
    def __init__(self, basic_num: Union[int, float] = 0):
        sys.set_int_max_str_digits(2147483647)
        self.basic_num = basic_num
    
    def Addition(self, other_num: Union[int, float] = 0):
        if "." in str(self.basic_num) or "." in str(other_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num * a_power_of_ten)
            provisional_result = provisional_figure_1 + provisional_figure_2
            result = provisional_result / a_power_of_ten
            return HighPrecisionOperation(result)
        else:
            result = self.basic_num + other_num
            return HighPrecisionOperation(result)
        
    def Subtraction(self, other_num: Union[int, float] = 0):
        if "." in str(self.basic_num) or "." in str(other_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num * a_power_of_ten)
            provisional_result = provisional_figure_1 - provisional_figure_2
            result = provisional_result / a_power_of_ten
            return HighPrecisionOperation(result)
        else:
            result = self.basic_num - other_num
            return HighPrecisionOperation(result)
        
    def Multiplication(self, other_num: Union[int, float] = 0):
        if "." in str(self.basic_num) or "." in str(other_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num * a_power_of_ten)
            provisional_result = provisional_figure_1 * provisional_figure_2
            result = provisional_result / (a_power_of_ten ** 2)
            return HighPrecisionOperation(result)
        else:
            result = self.basic_num * other_num
            return HighPrecisionOperation(result)
        
    def Division(self, other_num: Union[int, float] = 0):
        if other_num != 0:
            pass
        else:
            raise ZeroDivisionError(f"不被允许的0 [other_num={other_num}]")
        if "." in str(self.basic_num) or "." in str(other_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num * a_power_of_ten)
            result = provisional_figure_1 / provisional_figure_2
            return HighPrecisionOperation(result)
        else:
            result = self.basic_num / other_num
            return HighPrecisionOperation(result)
        
    def involution(self, index: int = 1):
        if self.basic_num == 0 and index == 0:
            raise HighPrecisionMathError(f"不被允许的数值 [basic_num={self.basic_num}, index={index}]")
        result = self.basic_num ** index
        return HighPrecisionOperation(result)
    
    def HighPrecisionOperationType_conversion_number(self):
        return self.basic_num
    

class HighPrecision:
    """Just a HighPrecision"""
    def __init__(self, basic_num):
        self.basic_num = basic_num

    def is_integer(self):
        return self.basic_num % 1 == 0

    def __int__(self):
        return int(self.basic_num)
    
    def __float__(self):
        return float(self.basic_num)
        
    def __add__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if "." in str(self.basic_num) or "." in str(other_num.basic_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num.basic_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num.basic_num * a_power_of_ten)
            provisional_result = provisional_figure_1 + provisional_figure_2
            result = provisional_result / a_power_of_ten
            return HighPrecision(result)
        else:
            result = self.basic_num + other_num.basic_num
            return HighPrecision(result)
        
    def __sub__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if "." in str(self.basic_num) or "." in str(other_num.basic_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num.basic_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num.basic_num * a_power_of_ten)
            provisional_result = provisional_figure_1 - provisional_figure_2
            result = provisional_result / a_power_of_ten
            return HighPrecision(result)
        else:
            result = self.basic_num - other_num.basic_num
            return HighPrecision(result)
        
    def __mul__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if "." in str(self.basic_num) or "." in str(other_num.basic_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num.basic_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num.basic_num * a_power_of_ten)
            provisional_result = provisional_figure_1 * provisional_figure_2
            result = provisional_result / (a_power_of_ten ** 2)
            return HighPrecision(result)
        else:
            result = self.basic_num * other_num.basic_num
            return HighPrecision(result)
        
    def __truediv__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if "." in str(self.basic_num) or "." in str(other_num.basic_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num.basic_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num.basic_num * a_power_of_ten)
            result = provisional_figure_1 / provisional_figure_2
            return HighPrecision(result)
        else:
            result = self.basic_num / other_num.basic_num
            return HighPrecision(result)

    def __mod__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if "." in str(self.basic_num) or "." in str(other_num.basic_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num.basic_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num.basic_num * a_power_of_ten)
            result = (provisional_figure_1 % provisional_figure_2) / a_power_of_ten
            return HighPrecision(result)
        else:
            result = self.basic_num % other_num.basic_num
            return HighPrecision(result)
    
    def __pow__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return HighPrecision(self.basic_num ** other_num.basic_num)
        
    def __div__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return self.__truediv__(other_num)
    
    def __floordiv__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if "." in str(self.basic_num) or "." in str(other_num.basic_num):
            str_1 = str(self.basic_num).split(".")[-1]
            str_2 = str(other_num.basic_num).split(".")[-1]
            len_1 = len(str_1)
            len_2 = len(str_2)
            if len_1 > len_2:
                a_power_of_ten = int(10 ** len_1)
            else:
                a_power_of_ten = int(10 ** len_2)
            provisional_figure_1 = int(self.basic_num * a_power_of_ten)
            provisional_figure_2 = int(other_num.basic_num * a_power_of_ten)
            not_final_result = provisional_figure_1 / provisional_figure_2
            result = int(str(not_final_result).split(".")[0])
            return HighPrecision(result)
        else:
            not_final_result = self.basic_num / other_num.basic_num
            result = int(str(not_final_result).split(".")[0])
            return HighPrecision(result)
        
    def __pos__(self):
        return HighPrecision(self.basic_num)
    
    def __neg__(self):
        return HighPrecision(-self.basic_num)
    
    def __abs__(self):
        return HighPrecision(abs(self.basic_num))
    
    def __str__(self):
        return str(self.basic_num)
    
    def __repr__(self):
        return F"{repr(self.basic_num)}"
    
    def __len__(self):
        return len(str(self.basic_num))
    
    def __lshift__(self, other_num: int):
        if not isinstance(other_num, int):
            other_num = int(other_num)
        is_int = self.basic_num % 1 == 0

        if is_int:
            return HighPrecision(int(self.basic_num) << other_num)
        else:
            raise TypeError(f"无法对浮点数进行位移操作（{self.basic_num}）")
        
    def __rshift__(self, other_num: int):
        if not isinstance(other_num, int):
            other_num = int(other_num)
        is_int = self.basic_num % 1 == 0

        if is_int:
            return HighPrecision(int(self.basic_num) >> other_num)
        else:
            raise TypeError(f"无法对浮点数进行位移操作（{self.basic_num}）")
        
    def __invert__(self):
        is_int = self.basic_num % 1 == 0

        if is_int:
            return HighPrecision(~int(self.basic_num))
        else:
            raise TypeError(f"无法对浮点数进行按位取反操作（{self.basic_num}）")
        
    def __and__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        is_int = self.basic_num % 1 == 0 and other_num.basic_num % 1 == 0

        if is_int:
            bin_basic = bin(self.basic_num).split("b")[-1]
            bin_other = bin(other_num.basic_num).split("b")[-1]
            list_bin_basic = [char for char in bin_basic]
            list_bin_other = [ccc for ccc in bin_other]
            if len(list_bin_basic) > len(list_bin_other):
                times = int(len(list_bin_basic) - len(list_bin_other))
                for i in range(times):
                    list_bin_other.insert(0, str(0))
            elif len(list_bin_basic) < len(list_bin_other):
                times = int((HighPrecision(len(list_bin_other)) - HighPrecision(len(list_bin_basic))).__repr__())
                for i in range(times):
                    list_bin_basic.insert(0, str(0))
            elif len(list_bin_basic) == len(list_bin_other):
                pass
            list_result = []
            for u, j in zip(list_bin_basic, list_bin_other):
                if u == str(1) and j == str(1):
                    list_result.append(str(1))
                else:
                    list_result.append(str(0))
            bin_result = ""
            for k in list_result:
                bin_result = bin_result + k
            result = int(bin_result, 2)
            return HighPrecision(result)
        else:
            raise TypeError(f"无法对浮点数进行按位与操作（{self.basic_num}）")
        
        
    def __or__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        is_int = self.basic_num % 1 == 0 and other_num.basic_num % 1 == 0

        if is_int:
            bin_basic = bin(self.basic_num).split("b")[-1]
            bin_other = bin(other_num.basic_num).split("b")[-1]
            list_bin_basic = [char for char in bin_basic]
            list_bin_other = [ccc for ccc in bin_other]
            if len(list_bin_basic) > len(list_bin_other):
                times = int(len(list_bin_basic) - len(list_bin_other))
                for i in range(times):
                    list_bin_other.insert(0, str(0))
            elif len(list_bin_basic) < len(list_bin_other):
                times = int((HighPrecision(len(list_bin_other)) - HighPrecision(len(list_bin_basic))).__repr__())
                for i in range(times):
                    list_bin_basic.insert(0, str(0))
            elif len(list_bin_basic) == len(list_bin_other):
                pass
            list_result = []
            for u, j in zip(list_bin_basic, list_bin_other):
                if u == str(1) and j == str(0):
                    list_result.append(str(1))
                elif u == str(0) and j == str(1):
                    list_result.append(str(1))
                elif u == str(1) and j == str(1):
                    list_result.append(str(1))
                else:
                    list_result.append(str(0))
            bin_result = ""
            for k in list_result:
                bin_result = bin_result + k
            result = int(bin_result, 2)
            return HighPrecision(result)
        else:
            raise TypeError(f"无法对浮点数进行按位或操作（{self.basic_num}）")
        
    def __xor__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        is_int = self.basic_num % 1 == 0 and other_num.basic_num % 1 == 0

        if is_int:
            bin_basic = bin(self.basic_num).split("b")[-1]
            bin_other = bin(other_num.basic_num).split("b")[-1]
            list_bin_basic = [char for char in bin_basic]
            list_bin_other = [ccc for ccc in bin_other]
            if len(list_bin_basic) > len(list_bin_other):
                times = int(len(list_bin_basic) - len(list_bin_other))
                for i in range(times):
                    list_bin_other.insert(0, str(0))
            elif len(list_bin_basic) < len(list_bin_other):
                times = int((HighPrecision(len(list_bin_other)) - HighPrecision(len(list_bin_basic))).__repr__())
                for i in range(times):
                    list_bin_basic.insert(0, str(0))
            elif len(list_bin_basic) == len(list_bin_other):
                pass
            list_result = []
            for u, j in zip(list_bin_basic, list_bin_other):
                if u == str(1) and j == str(0):
                    list_result.append(str(1))
                elif u == str(0) and j == str(1):
                    list_result.append(str(1))
                else:
                    list_result.append(str(0))
            bin_result = ""
            for k in list_result:
                bin_result = bin_result + k
            result = int(bin_result, 2)
            return HighPrecision(result)
        else:
            raise TypeError(f"无法对浮点数进行按位异或操作（{self.basic_num}）")
    
    def __iadd__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        res = self.__add__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __isub__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        res = self.__sub__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __imul__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        res = self.__mul__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __itruediv__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        res = self.__truediv__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __ifloordiv__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        res = self.__floordiv__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __imod__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        res = self.__mod__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __ipow__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        res = self.__pow__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __iand__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if not self.is_integer() or not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        res = self.__and__(other_num)
        self.basic_num = res.basic_num
        return self

    def __ior__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if not self.is_integer() or not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        res = self.__or__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __ixor__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if not self.is_integer() or not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        res = self.__xor__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __ilshift__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if not self.is_integer() or not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        res = self.__lshift__(other_num)
        self.basic_num = res.basic_num
        return self

    def __irshift__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if not self.is_integer() or not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        res = self.__rshift__(other_num)
        self.basic_num = res.basic_num
        return self
    
    def __radd__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return self.__add__(other_num)

    def __rsub__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return self.__sub__(other_num)

    def __rmul__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return self.__mul__(other_num)
    
    def __rtruediv__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        if not self.is_integer() or not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        return other_num.__truediv__(self)
    
    def __rmod__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return other_num.__mod__(self)
    
    def __rfloordiv__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return other_num.__floordiv__(self)
    
    def __rpow__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return other_num.__pow__(self)
    
    def __rlshift__(self, other_num: Union["HighPrecision", int]):
        if not self.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        if isinstance(other_num, HighPrecision):
            if not other_num.is_integer():
                raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
            other_num = int(other_num)
        elif isinstance(other_num, float) and not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        return other_num.__lshift__(int(self))
    
    def __rrshift__(self, other_num: Union["HighPrecision", int]):
        if not self.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        if isinstance(other_num, HighPrecision):
            if not other_num.is_integer():
                raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
            other_num = int(other_num)
        elif isinstance(other_num, float) and not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        return other_num.__rshift__(int(self))
    
    def __ror__(self, other_num: Union["HighPrecision", int]):
        if not self.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        if isinstance(other_num, HighPrecision):
            if not other_num.is_integer():
                raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
            other_num = int(other_num)
        elif isinstance(other_num, float) and not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        return other_num.__or__(int(self))
    
    def __rxor__(self, other_num: Union["HighPrecision", int]):
        if not self.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        if isinstance(other_num, HighPrecision):
            if not other_num.is_integer():
                raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
            other_num = int(other_num)
        elif isinstance(other_num, float) and not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        return other_num.__xor__(int(self))
            
    def __rand__(self, other_num: Union["HighPrecision", int]):
        if not self.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        if isinstance(other_num, HighPrecision):
            if not other_num.is_integer():
                raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
            other_num = int(other_num)
        elif isinstance(other_num, float) and not other_num.is_integer():
            raise TypeError(f"不能对浮点数进行按位运算（{other_num} 和 {self}）")
        return other_num.__and__(int(self))

class HighPrecisionOperationEX:
    """HighPrecisionOperation类的拓展"""
    def __init__(self, basic_num:Union[float, int, HighPrecision, complex, str]):
        sys.set_int_max_str_digits(2**31-1)
        self.basic_num = basic_num
        self.list_result = []
        self.just_an_empty_str = ""
        self.just_a_num = 0
        self.rest_num = 0
    
    def __complex__(self):
        return complex(self.basic_num)

    def sqrt(self, float_part_length:int = 8):
        """
        平方根运算
        """
        if self.basic_num >= 0:
            pass
        else:
            raise HighPrecisionMathError(f"不被允许的数值 [basic_num={self.basic_num}] '你或许在寻找HighPrecisionOperationEX中的isqrt()函数' ")
        self.basic_num = float(self.basic_num)
        self.basic_num = str(self.basic_num)
        self.basic_num_int_part = self.basic_num.split(".")[0]
        self.basic_num_float_part = self.basic_num.split(".")[-1]
        if len(self.basic_num_int_part) % 2 == 0:
            pass
        else:
            self.basic_num = "0" + self.basic_num
        if len(self.basic_num_float_part) % 2 == 0:
            pass
        else:
            self.basic_num = self.basic_num + "0"
        if len(self.basic_num_float_part) /2 <= float_part_length:
            need_add_zero_times = float_part_length * 2 - len(self.basic_num_float_part)
            for i in range(need_add_zero_times - 1):
                self.basic_num = self.basic_num + "0"
        else:
            need_del_num_times = len(self.basic_num_float_part) - float_part_length * 2
            for i in range(need_del_num_times - 1):
                self.basic_num = self.basic_num[:-1]
        need_falsediv = int(len(self.basic_num.split(".")[-1]) / 2)
        basic_str = self.basic_num.split(".")[0] + self.basic_num.split(".")[-1]
        list_basic_num = [basic_str[u:u+2] for u in range(0, len(basic_str), 2)]
        for need_compare_num in list_basic_num:
            if self.just_an_empty_str == "":
                if need_compare_num.startswith("0"):
                    while need_compare_num.startswith("0"):
                        need_compare_num = need_compare_num[1:]
                    need_compare_num = int(need_compare_num)
                else:
                    need_compare_num = int(need_compare_num)
            else:
                need_compare_num = int(str(self.rest_num) + need_compare_num)
            if self.just_an_empty_str == "":
                while self.just_a_num * self.just_a_num <= need_compare_num:
                    self.just_a_num += 1
                self.just_a_num = self.just_a_num - 1
            else:
                while self.just_a_num * int(str(2 * int(self.just_an_empty_str)) + str(self.just_a_num)) <= need_compare_num:
                    self.just_a_num += 1
                self.just_a_num = self.just_a_num - 1
            if self.just_an_empty_str == "":
                self.rest_num = need_compare_num - self.just_a_num * self.just_a_num
            else:
                self.rest_num = need_compare_num - self.just_a_num * int(str(2 * int(self.just_an_empty_str)) + str(self.just_a_num))
            self.just_an_empty_str = self.just_an_empty_str + str(self.just_a_num)
            self.list_result.append(str(self.just_a_num))
            self.just_a_num = 0
        result_list = [self.just_an_empty_str[n:n+1] for n in range(0, len(self.just_an_empty_str), 1)]
        result_list.insert((len(self.just_an_empty_str) - need_falsediv), ".")
        self.list_result.insert((len(self.just_an_empty_str) - need_falsediv), ".")
        result = ""
        for i in result_list:
            result = result + i
        result_to_check = ""
        for string in self.list_result:
            result_to_check = result_to_check + string
        """
        Python自带的浮点精度只有16位
        What can I say?
        只好用str了
        """
        if result == result_to_check:
            return HighPrecisionOperationEX(result)
        else:
            raise HighPrecisionMathError(f"验证运算结果出错 [result={result}, result_to_check={result_to_check}]")
        
    def isqrt(self, float_part_length:int = 8):
        """
        负数平方根
        """
        if self.basic_num < 0:
            pass
        else:
            raise HighPrecisionMathError(f"不被允许的数值 [basic_num={self.basic_num}] '你或许在寻找HighPrecisionOperationEX中的sqrt()函数' ")
        self.basic_num = 0 - self.basic_num
        result = HighPrecisionOperationEX(self.basic_num).sqrt(float_part_length)
        return HighPrecisionOperationEX(str(result.basic_num) + "i")

    def to_str(self):
        return str(self.basic_num)
    
if __name__ == "__main__":
    a = HighPrecision(0.1) + HighPrecision(0.2)
    print(a)
    b = HighPrecision(114) ^ HighPrecision(51)
    print(b)
    c = ~int(114)
    print(c)
    d = ~HighPrecision(114)
    print(d)
    e = ~int(2**22-1)
    f = ~HighPrecision(2**22-1)
    print(e)
    print(f)
    g = HighPrecision(2)
    g+=HighPrecision(1)
    print(g)
    aaa = HighPrecisionOperationEX(2).sqrt(20).to_str()
    bbb = math.sqrt(2)
    ccc = HighPrecisionOperationEX(-2).isqrt(16).to_str()
    ddd = cmath.sqrt(-2)
    print(f"{aaa}\n{bbb}\n{ccc}\n{ddd}")