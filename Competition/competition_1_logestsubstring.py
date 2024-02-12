"""
This file for longest substring search algorithm
"""

class Competition():
    def __init__(self, text_1, text_2):
        self.text_1 = text_1
        self.text_2 = text_2

    def tao_algorithm(self):
        """
        Algorithm from tao
        """

    def kantong_algorithm(self):
        """
        Algorithm from kantong
        """

    def tonkaow_algorithm(self):
        """
        Algorithm from tonkaow
        """

    def ton_algorithm(self):
        """
        Algorithm from ton
        """
        import numpy as np
        possible_result, i = [], 0      # สร้างตัวแปร possible_result มาเพื่อเก็บค่าของ [word -> คำที่ซ้ำ, k -> จำนวนอักษร], i -> iteration couter.
        while i < len(self.text_1):     # while ใน self.text_1, iteration couter -> i.
            j, k, word = 0, 0, ""       # j -> iteration couter, k -> letter couter, word -> letter collecter.
            while j < len(self.text_2): # while ใน self.text_2, iteration couter -> j.
                if (text_1[i+k] == text_2[j]):      # เช็คว่าเจอตัวซ้ำมั้ย โดยถ้าเจอจะขยับขึ้นไปทีละ k หน่วย เพื่อไปยังตัวอักษรถัดไป.
                    word += text_2[j]               # เก็บตัวอักษรที่เจอไว้ใน word.
                    k += 1                          # เพิ่มค่าของ k ขึ้น 1 หน่วยเพื่อนับตัวซ้ำและใช้ในการขยับ.
                elif k != 0: possible_result.append([word, k]); k = 0   # กรณีที่ผ่าน if แล้ว k != 0 จะทำการเก็บค่าของ [word, k] ไว้ใน possible_result.
                j += 1  # increasing condition for loop j.
            i += 1      # increasing condition for loop i.
        result = possible_result[np.argmax(np.array(possible_result)[:,1])]                 # เก็บค่าผลลัพธ์ที่มากที่สุดไว้ในตัวแปร result.
        print(f"\nLongest substring is \"{result[0]}\" with \"{result[1]}\" letters.\n")    # ปริ้นท์ต่านั้นออกมา.
        return result   # return ค่านั้นออกไปเป็น list.

if __name__ == "__main__":
    text_1 = "parachute"
    text_2 = "shuttle"
    com = Competition(text_1 = text_1, text_2 = text_2)
    com.ton_algorithm()     # How to run your function.
