import sys

from typing import Any


class HighPrecision:
    def __init__(self, basic_num):
        sys.set_int_max_str_digits(2147483647)
        self.basic_num = basic_num
        

    
    def __divmod__(self, value: int, /) -> tuple[int, int]: ...
    def __rdivmod__(self, value: int, /) -> tuple[int, int]: ...
    def __rpow__(self, value: int, mod: int | None = None, /) -> Any: ...
    def __and__(self, value: int, /) -> int: ...
    def __or__(self, value: int, /) -> int: ...
    def __xor__(self, value: int, /) -> int: ...
    def __lshift__(self, value: int, /) -> int: ...
    def __rshift__(self, value: int, /) -> int: ...
    def __rand__(self, value: int, /) -> int: ...
    def __ror__(self, value: int, /) -> int: ...
    def __rxor__(self, value: int, /) -> int: ...
    def __rlshift__(self, value: int, /) -> int: ...
    def __rrshift__(self, value: int, /) -> int: ...
    def __neg__(self) -> int: ...
    def __pos__(self) -> int: ...
    def __invert__(self) -> int: ...
    def __trunc__(self) -> int: ...
    def __ceil__(self) -> int: ...
    def __floor__(self) -> int: ...
    def __getnewargs__(self) -> tuple[int]: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __ne__(self, value: object, /) -> bool: ...
    def __lt__(self, value: int, /) -> bool: ...
    def __le__(self, value: int, /) -> bool: ...
    def __gt__(self, value: int, /) -> bool: ...
    def __ge__(self, value: int, /) -> bool: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __abs__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __index__(self) -> int: ...
        
    def __add__(self, other_num: "HighPrecision"):
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
            self.result = result
            return HighPrecision(self.result)
        else:
            result = self.basic_num + other_num.basic_num
            self.result = result
            return HighPrecision(self.result)
    
    def __iadd__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        res = self.__add__(other_num)
        self.basic_num= res.basic_num
        return self
    
    def __radd__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return self.__add__(other_num)
        
    def __sub__(self, other_num: "HighPrecision"):
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
            self.result = result
            return HighPrecision(self.result)
        else:
            result = self.basic_num - other_num.basic_num
            self.result = result
            return HighPrecision(self.result)
        
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
        return other_num.__truediv__(self)
        
    def __mul__(self, other_num: "HighPrecision"):
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
            self.result = result
            return HighPrecision(self.result)
        else:
            result = self.basic_num * other_num.basic_num
            self.result = result
            return HighPrecision(self.result)
        
    def __truediv__(self, other_num: "HighPrecision"):
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
            self.result = result
            return HighPrecision(self.result)
        else:
            result = self.basic_num / other_num.basic_num
            self.result = result
            return HighPrecision(self.result)
        
    def __mod__(self, other_num: "HighPrecision"):
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
            self.result = result
            return HighPrecision(self.result)
        else:
            result = self.basic_num % other_num.basic_num
            self.result = result
            return HighPrecision(self.result)
        
    def __floordiv__(self, other_num: "HighPrecision"):
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
            self.result = result
            return HighPrecision(self.result)
        else:
            not_final_result = self.basic_num / other_num.basic_num
            result = int(str(not_final_result).split(".")[0])
            self.result = result
            return HighPrecision(self.result)
        
    def __rfloordiv__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        return other_num.__floordiv__(self)
    
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
            return HighPrecision(int(self.basic_num) & int(other_num.basic_num))
        else:
            raise TypeError(f"无法对浮点数进行按位与操作（{self.basic_num}）")
        
    def __or__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        is_int = self.basic_num % 1 == 0 and other_num.basic_num % 1 == 0

        if is_int:
            return HighPrecision(int(self.basic_num) | int(other_num.basic_num))
        else:
            raise TypeError(f"无法对浮点数进行按位或操作（{self.basic_num}）")
        
    def __xor__(self, other_num: "HighPrecision"):
        if not isinstance(other_num, HighPrecision):
            other_num = HighPrecision(other_num)
        is_int = self.basic_num % 1 == 0 and other_num.basic_num % 1 == 0

        if is_int:
            return HighPrecision(int(self.basic_num) ^ int(other_num.basic_num))
        else:
            raise TypeError(f"无法对浮点数进行按位异或操作（{self.basic_num}）")

    def __repr__(self):
        return F"{repr(self.basic_num)}"
        

if __name__ == "__main__":
    a = HighPrecision(2) + HighPrecision(3) * HighPrecision(2) / HighPrecision(4) - HighPrecision(0.1) * HighPrecision(3) - HighPrecision(2)
    print(a)
    b = HighPrecision(114.5) % HighPrecision(1.4)
    print(b)
    e = 114.5 % 1.4
    print(e)
    c = HighPrecision(114.9) // HighPrecision(23)
    print(c)
    d = 114.9 // 23
    print(d)
    