import os, sys, random, time
from typing import Union
try:
    from src.error_type import *
except:
    from error_type import *

class HighPrecisionInt(int):
    def __init__(self, basic_num:Union[int, "HighPrecisionInt"]):
        super().__init__()
        sys.set_int_max_str_digits(2147483647)
        sys.setrecursionlimit(2147483647)
        self.basic_num = int(basic_num)
        self.list_result = []

    def __add__(self, other_num:Union[int, float, "HighPrecisionInt", "HighPrecisionFloat"], a_negative_sign_needs_to_be_added:bool = False):
        if type(other_num) == float:
            result = HighPrecisionFloat(self.basic_num) + HighPrecisionFloat(other_num)
            return result
        elif type(other_num) == HighPrecisionFloat:
            result = HighPrecisionFloat(self.basic_num) + HighPrecisionFloat(other_num)
            return result
        elif type(other_num) == HighPrecisionInt:
            self.other_num = other_num.basic_num
        elif type(other_num) == int:
            self.other_num = other_num
        elif type(other_num) == str:
            try:
                test = int(other_num)
                self.other_num = int(other_num)
            except:
                raise HighPrecisionTypeError(f"不被支持的数据类型 [type(other_num)={type(other_num)}]")
        else:
            raise HighPrecisionTypeError(f"不被支持的数据类型 [type(other_num)={type(other_num)}]")
        if self.basic_num > 0 and self.other_num > 0:
            a_negative_sign_needs_to_be_added = False
        elif self.basic_num < 0 and self.other_num > 0:
            result = HighPrecisionInt(self.other_num) - HighPrecisionInt(int(str(self.basic_num).split("-")[-1]))
            return result
        elif self.basic_num > 0 and self.other_num < 0:
            result = HighPrecisionInt(self.basic_num) - HighPrecisionInt(int(str(self.other_num).split("-")[-1]))
            return result
        elif self.basic_num < 0 and self.other_num < 0:
            a_negative_sign_needs_to_be_added = True
            self.basic_num = int(str(self.basic_num).split("-")[-1])
            self.other_num = int(str(self.other_num).split("-")[-1])
        basic_bin = bin(self.basic_num).split("0b")[-1]
        other_bin = bin(self.other_num).split("0b")[-1]
        basic_list_1 = [basic_bin[i:i+1] for i in range(0, len(basic_bin), 1)]
        other_list_1 = [other_bin[i:i+1] for i in range(0, len(other_bin), 1)]
        basic = ""
        other = ""
        for j in basic_list_1:
            basic = j + basic
        for k in other_list_1:
            other = k + other
        basic_list = [basic[i:i+1] for i in range(0, len(basic), 1)]
        other_list = [other[i:i+1] for i in range(0, len(other), 1)]
        if len(basic_list) != len(other_list):
            for i in range(len(basic_list)):
                other_list.append(str(0))
            for i in range(len(other_list)):
                basic_list.append(str(0))
        elif len(basic_list) == len(other_list):
            basic_list.append(str(0))
            other_list.append(str(0))
        else:
            print("?")
            raise HighPrecisionLengthError(f"意外的长度判断失败 [basic_list_length={len(basic_list)}, other_list_length={len(other_list)}]")
        flag = 0
        for x, y in zip(basic_list, other_list):
            if x == str(1) and y == str(1) and flag != 1:
                self.list_result.append(str(0))
                flag = 1
            elif x == str(0) and y == str(1) and flag != 1:
                self.list_result.append(str(1))
                flag = 0
            elif x == str(1) and y == str(0) and flag != 1:
                self.list_result.append(str(1))
                flag = 0
            elif x == str(0) and y == str(0) and flag != 1:
                self.list_result.append(str(0))
                flag = 0
            elif x == str(1) and y == str(1) and flag == 1:
                self.list_result.append(str(1))
                flag = 1
            elif x == str(0) and y == str(1) and flag == 1:
                self.list_result.append(str(0))
                flag = 1
            elif x == str(1) and y == str(0) and flag == 1:
                self.list_result.append(str(0))
                flag = 1
            elif x == str(0) and y == str(0) and flag == 1:
                self.list_result.append(str(1))
                flag = 0
            else:
                raise HighPrecisionBinError(f"在二进制中发现了意外的字符 [x={x}, y={y}]")
        result = ""
        for z in self.list_result:
            result = z + result
        if result.startswith(str(0)):
            while result.startswith(str(0)):
                result = result[1:]
        result = "0b" + result
        final_result = int(result, base=0)
        if a_negative_sign_needs_to_be_added:
            final_result = int(str("-") + str(final_result))
        return HighPrecisionInt(final_result)
    
    def __sub__(self, other_num:Union[int, float, "HighPrecisionInt", "HighPrecisionFloat"], a_negative_sign_needs_to_be_added:bool = False):
        if type(other_num) == float:
            result = HighPrecisionFloat(self.basic_num) - HighPrecisionFloat(other_num)
            return result
        elif type(other_num) == HighPrecisionFloat:
            result = HighPrecisionFloat(self.basic_num) - HighPrecisionFloat(other_num)
            return result
        elif type(other_num) == HighPrecisionInt:
            self.other_num = other_num.basic_num
        elif type(other_num) == int:
            self.other_num = other_num
        else:
            raise HighPrecisionTypeError(f"不被支持的数据类型 [type(other_num)={type(other_num)}]")
        if self.basic_num > 0 and self.other_num > 0 and self.basic_num > self.other_num:
            a_negative_sign_needs_to_be_added = False
        elif self.basic_num > 0 and self.other_num > 0 and self.basic_num < self.other_num:
            a_negative_sign_needs_to_be_added = True
            transit = self.basic_num
            self.basic_num = self.other_num
            self.other_num = transit
        elif self.basic_num < 0 and self.other_num > 0:
            result = HighPrecisionInt(self.basic_num) + HighPrecisionInt(int("-" + str(self.other_num)))
            return result
        elif self.basic_num > 0 and self.other_num < 0:
            result = HighPrecisionInt(self.basic_num) + HighPrecisionInt(int(str(self.other_num).split("-")[-1]))
            return result
        elif self.basic_num < 0 and self.other_num < 0 and self.basic_num > self.other_num:
            a_negative_sign_needs_to_be_added = False
            transit = int(str(self.basic_num).split("-")[-1])
            self.basic_num = int(str(self.other_num).split("-")[-1])
            self.other_num = transit
        elif self.basic_num < 0 and self.other_num < 0 and self.basic_num < self.other_num:
            a_negative_sign_needs_to_be_added = True
            self.basic_num = int(str(self.basic_num).split("-")[-1])
            self.other_num = int(str(self.other_num).split("-")[-1])
        basic_bin = bin(self.basic_num).split("0b")[-1]
        other_bin = bin(self.other_num).split("0b")[-1]
        basic_list_1 = [basic_bin[i:i+1] for i in range(0, len(basic_bin), 1)]
        other_list_1 = [other_bin[i:i+1] for i in range(0, len(other_bin), 1)]
        basic = ""
        other = ""
        for j in basic_list_1:
            basic = j + basic
        for k in other_list_1:
            other = k + other
        basic_list = [basic[i:i+1] for i in range(0, len(basic), 1)]
        other_list = [other[i:i+1] for i in range(0, len(other), 1)]
        if len(basic_list) != len(other_list):
            for i in range(len(basic_list)):
                other_list.append(str(0))
            for i in range(len(other_list)):
                basic_list.append(str(0))
        elif len(basic_list) == len(other_list):
            basic_list.append(str(0))
            other_list.append(str(0))
        else:
            print("?")
            raise HighPrecisionLengthError(f"意外的长度判断失败 [basic_list_length={len(basic_list)}, other_list_length={len(other_list)}]")
        flag = 0
        for x, y in zip(basic_list, other_list):
            if x == str(1) and y == str(1) and flag != 1:
                self.list_result.append(str(0))
                flag = 0
            elif x == str(0) and y == str(1) and flag != 1:
                self.list_result.append(str(1))
                flag = 1
            elif x == str(1) and y == str(0) and flag != 1:
                self.list_result.append(str(1))
                flag = 0
            elif x == str(0) and y == str(0) and flag != 1:
                self.list_result.append(str(0))
                flag = 0
            elif x == str(1) and y == str(1) and flag == 1:
                self.list_result.append(str(1))
                flag = 1
            elif x == str(0) and y == str(1) and flag == 1:
                self.list_result.append(str(0))
                flag = 1
            elif x == str(1) and y == str(0) and flag == 1:
                self.list_result.append(str(0))
                flag = 0
            elif x == str(0) and y == str(0) and flag == 1:
                self.list_result.append(str(1))
                flag = 1
            else:
                raise HighPrecisionBinError(f"在二进制中发现了意外的字符 [x={x}, y={y}]")
        result = ""
        for z in self.list_result:
            result = z + result
        if result.startswith(str(0)):
            while result.startswith(str(0)):
                result = result[1:]
        result = "0b" + result
        final_result = int(result, base=0)
        if a_negative_sign_needs_to_be_added:
            final_result = int(str("-") + str(final_result))
        return HighPrecisionInt(final_result)
    
    def __mul__(self, other_num:Union[int, float, "HighPrecisionInt", "HighPrecisionFloat"], a_negative_sign_needs_to_be_added:bool = False):
        if type(other_num) == float:
            result = HighPrecisionFloat(self.basic_num) * HighPrecisionFloat(other_num)
            return result
        elif type(other_num) == HighPrecisionFloat:
            result = HighPrecisionFloat(self.basic_num) * HighPrecisionFloat(other_num)
            return result
        elif type(other_num) == HighPrecisionInt:
            self.other_num = other_num.basic_num
        elif type(other_num) == int:
            self.other_num = other_num
        else:
            raise HighPrecisionTypeError(f"不被支持的数据类型 [type(other_num)={type(other_num)}]")
        if self.basic_num > 0 and self.other_num > 0:
            a_negative_sign_needs_to_be_added = False
        elif self.basic_num < 0 and self.other_num > 0:
            a_negative_sign_needs_to_be_added = True
            self.basic_num = int(str(self.basic_num).split("-")[-1])

        elif self.basic_num > 0 and self.other_num < 0:
            a_negative_sign_needs_to_be_added = True
            self.other_num = int(str(self.other_num).split("-")[-1])

        elif self.basic_num < 0 and self.other_num < 0:
            a_negative_sign_needs_to_be_added = False
            self.basic_num = int(str(self.basic_num).split("-")[-1])
            self.other_num = int(str(self.other_num).split("-")[-1])
        
        if self.basic_num >= self.other_num:
            self.basic_num = self.basic_num
            list_for_continue = [str(self.other_num)[i:i+1] for i in range(0, len(str(self.other_num)), 1)]
        else:
            list_for_continue = [str(self.basic_num)[i:i+1] for i in range(0, len(str(self.basic_num)), 1)]
            self.basic_num = self.other_num
        index = len(list_for_continue) - 1
        list_result = []
        for j in list_for_continue:
            result_not_final = HighPrecisionInt(0)
            for u in range(int(j)):
                result_not_final += HighPrecisionInt(self.basic_num)
            result_not_final = str(result_not_final)
            if index == 0:
                list_result.append(result_not_final)
            else:
                for ing in range(int(index)):
                    result_not_final += "0"
                result_not_final = HighPrecisionInt(result_not_final)
                list_result.append(result_not_final)
                index -= 1
        result = HighPrecisionInt(0)
        for re in list_result:
            result += HighPrecisionInt(re)
        if a_negative_sign_needs_to_be_added:
            result = "-" + str(result)
        return HighPrecisionInt(result)
        


        
class HighPrecisionFloat(float):
    def __init__(self, basic_num:Union[int, float, str, "HighPrecisionFloat", HighPrecisionInt]):
        super().__init__()
        sys.set_int_max_str_digits(2147483647)
        self.basic_num_str = str(basic_num)
        if type(basic_num) == int:
            self.float_part_length = 0
            self.int_part_str = str(basic_num)
            self.int_part = str(basic_num).split(".")[0]
            self.float_part = 0

        elif type(basic_num) == float:
            self.float_part_length = len(str(basic_num).split(".")[-1])
            self.int_part_str = str(basic_num).replace(".", "")
            if "-" in self.int_part_str:
                self.int_part_str = self.int_part_str[1:]
                while self.int_part_str.startswith("0"):
                    self.int_part_str = self.int_part_str[1:]
                self.int_part_str = "-" + self.int_part_str
            self.int_part = str(basic_num).split(".")[0]
            self.float_part = str(basic_num).split(".")[-1]
            
        elif type(basic_num) == HighPrecisionFloat:
            self.float_part_length = basic_num.float_part_length
            self.int_part_str = basic_num.int_part_str
            if "-" in self.int_part_str:
                self.int_part_str = self.int_part_str[1:]
                while self.int_part_str.startswith("0"):
                    self.int_part_str = self.int_part_str[1:]
                self.int_part_str = "-" + self.int_part_str
            self.int_part = str(basic_num.basic_num_str).split(".")[0]
            self.float_part = str(basic_num.basic_num_str).split(".")[-1]
            
        elif type(basic_num) == HighPrecisionInt:
            self.float_part_length = 0
            self.int_part_str = str(basic_num.basic_num)
            self.int_part = str(basic_num).split(".")[0]
            self.float_part = 0
            
        elif type(basic_num) == str:
            try:
                test = float(basic_num)
                if "." in basic_num:
                    self.float_part_length = len(str(basic_num).split(".")[-1])
                    self.int_part_str = str(basic_num).replace(".", "")
                    if "-" in self.int_part_str:
                        self.int_part_str = self.int_part_str[1:]
                        while self.int_part_str.startswith("0"):
                            self.int_part_str = self.int_part_str[1:]
                    self.int_part_str = "-" + self.int_part_str
                    self.int_part = str(basic_num).split(".")[0]
                    self.float_part = str(basic_num).split(".")[-1]
                else:
                    self.float_part_length = 0
                    self.int_part_str = str(basic_num)
                    self.int_part = str(basic_num).split(".")[0]
                    self.float_part = 0
            except:
                raise HighPrecisionTypeError(f"意外的字符 [str={basic_num}]")
        else:
            raise HighPrecisionTypeError(f"不被支持的类型 [type={str(type(basic_num))}]")
        
    def __add__(self, other_num:Union[int, float, str, "HighPrecisionFloat", HighPrecisionInt]):
        other_num = HighPrecisionFloat(other_num)
        if self.float_part_length > other_num.float_part_length:
            final_float_part_length = self.float_part_length
            times = HighPrecisionInt(self.float_part_length) - HighPrecisionInt(other_num.float_part_length)
            for i in range(int(times)):
                other_num.int_part_str += str(0)
        elif self.float_part_length < other_num.float_part_length:
            final_float_part_length = other_num.float_part_length
            times = HighPrecisionInt(other_num.float_part_length) - HighPrecisionInt(self.float_part_length)
            for i in range(int(times)):
                self.int_part_str += str(0)
        else:
            final_float_part_length = self.float_part_length
        while self.int_part_str.startswith("0"):
            self.int_part_str = self.int_part_str[1:]
        while other_num.int_part_str.startswith("0"):
            other_num.int_part_str = other_num.int_part_str[1:]
        not_final_result = str(HighPrecisionInt(self.int_part_str) + HighPrecisionInt(other_num.int_part_str))
        result_list = [not_final_result[u:u+1] for u in range(0, len(not_final_result), 1)]
        if len(not_final_result) != final_float_part_length:
            point_index = int(HighPrecisionInt(len(not_final_result)) - HighPrecisionInt(final_float_part_length))
        else:
            point_index = 0
        result_list.insert(point_index, ".")
        result = ""
        for j in result_list:
            result += j
        if result.startswith("."):
            result = str(0) + result
        else:
            result = result
        return HighPrecisionFloat(result)
    
    def __sub__(self, other_num:Union[int, float, str, "HighPrecisionFloat", HighPrecisionInt]):
        other_num = HighPrecisionFloat(other_num)
        if self.float_part_length > other_num.float_part_length:
            final_float_part_length = self.float_part_length
            times = HighPrecisionInt(self.float_part_length) - HighPrecisionInt(other_num.float_part_length)
            for i in range(int(times)):
                other_num.int_part_str += str(0)
        elif self.float_part_length < other_num.float_part_length:
            final_float_part_length = other_num.float_part_length
            times = HighPrecisionInt(other_num.float_part_length) - HighPrecisionInt(self.float_part_length)
            for i in range(int(times)):
                self.int_part_str += str(0)
        else:
            final_float_part_length = self.float_part_length
        while self.int_part_str.startswith("0"):
            self.int_part_str = self.int_part_str[1:]
        while other_num.int_part_str.startswith("0"):
            other_num.int_part_str = other_num.int_part_str[1:]
        not_final_result = str(HighPrecisionInt(self.int_part_str) - HighPrecisionInt(other_num.int_part_str))
        result_list = [not_final_result[u:u+1] for u in range(0, len(not_final_result), 1)]
        if len(not_final_result) != final_float_part_length:
            point_index = int(HighPrecisionInt(len(not_final_result)) - HighPrecisionInt(final_float_part_length))
        else:
            point_index = 0
        result_list.insert(point_index, ".")
        result = ""
        for j in result_list:
            result += j
        if result.startswith(".-"):
            result = "-" + str(0) + result[2:]
        return HighPrecisionFloat(result)
    
    def __mul__(self, other_num: Union[int, float, HighPrecisionInt, "HighPrecisionFloat"]):
        other_num = HighPrecisionFloat(other_num)
        final_float_part_length = HighPrecisionInt(self.float_part_length) + HighPrecisionInt(other_num.float_part_length)
        not_final_result = str(HighPrecisionInt(self.int_part_str) * HighPrecisionInt(other_num.int_part_str))
        if "-" in not_final_result:
            not_final_result = not_final_result.replace("-", "")
            a_negative_sign_needs_to_be_added = True
        else:
            a_negative_sign_needs_to_be_added = False
        result_list = [not_final_result[u:u+1] for u in range(0, len(not_final_result), 1)]
        if len(not_final_result) > final_float_part_length:
            point_index = HighPrecisionInt(len(not_final_result)) - HighPrecisionInt(final_float_part_length)
            result_list.insert(point_index, ".")
        elif len(not_final_result) == final_float_part_length:
            point_index = 0
            result_list.insert(point_index, ".")
        else:
            need_add_zero = HighPrecisionInt(final_float_part_length) - HighPrecisionInt(len(not_final_result))
            for i in range(need_add_zero):
                result_list.insert(0, str(0))
            result_list.insert(0, ".")
        result = ""
        for j in result_list:
            result += j
        if result.startswith(".-"):
            result = "-" + str(0) + "." + result.split(".-")[-1]
        elif result.startswith("."):
            result = str(0) + result
        if a_negative_sign_needs_to_be_added:
            result = "-" + result
        return HighPrecisionFloat(result)
        


        
if __name__ == "__main__":
    HPI = HighPrecisionInt
    HPF = HighPrecisionFloat
    aaa = time.time()
    a = HPI(114514) ** HPI(3114514)
    aaaaa = time.time()
    b = 114514 ** 3114514
    bbbb = time.time()
    print(f"{aaaaa - aaa}\n{bbbb - aaaaa}")