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
        # ใช้ เซต ในการช่วยหาตัวอักษรที่ซ้ำกันก่อน
        common_chars = set(self.text_1) & set(self.text_2)
        print(f"common characters in both texts are :{common_chars}")
        
        #เราเช็คได้ทันทีว่า ถ้ามันไม่มีตัวอักษรที่เหมือนเลยจะได้เซตว่างแล้วหยุดการทำงานได้เลยไม่ต้อง run ต่อ
        if common_chars == set() :
            print("There is no common substring found between the two texts")
            return ["",0]
        else:
            #max_length จะเก็บค่าความยาวที่มากที่สุดของ subtext ที่เหมือนกัน
            max_length = 0
            #start_index จะเอาไว้เช็คว่าตัวที่เริ่มเหมือนกัน(ดูจาก text1 เป็นหลัก) ว่าอยู่ index ไหน
            start_index = 0
            #longest_common อันนี้เอาไว้ดูว่า subtext ที่ซ้ำกันคืออะไรเผื่อเฉยๆ อจ.ไม่ได้สั่ง
            longest_common = ""
            for char in common_chars:
            # i จะเป็น index ส่วน c จะเป็นตัวอักษร
            # ในที่นี้ indices1 และ indices2 จะให้มันเก็บค่า index (i) อย่างเดียว
            # แต่ให้มันเก็บเฉพาะตอนที่ตัวอักษร(c) ตรงกับ char ที่อยู่ในเซตของตัวอักษรที่ซ้ำกันอย่างเดียว
            # Find indices of char in text1
                indices1 = [i for i, c in enumerate(self.text_1) if c == char]
                '''print(indices1)'''
            # Find indices of char in text2
                indices2 = [i for i, c in enumerate(self.text_2) if c == char]
                '''print(indices2)'''
            #check index ทุกคู่
                for i1 in indices1:
                    for i2 in indices2:
                        length = 0
                        #ถ้า index + ความยาว(length อันนี้เป็นตัวเลื่อน index)แล้วมันยังไม่เกินความยาวของ text1 และ 2
                        #รวมทั้งถ้าตัวที่เช็คอยู่มันเหมือนกันจะให้เพิ่ม length ไป 1
                        #ถ้าไม่เข้าเงื่อนไข จะไปเปลี่ยน i2 กับ i1 จนดูครบทุกคู่ที่เป็นไปได้
                        while (i1 + length < len(self.text_1) and i2 + length < len(self.text_2) and
                        self.text_1[i1 + length] == self.text_2[i2 + length]):
                            length += 1

                # Update max_length and start_index if longer common substring found
                # Update ค่า ความยาวและ index ถ้ามี subtring ที่เหมือนกันอันใหม่ แต่มันยาวกว่า
                        if length > max_length:
                            max_length = length
                            start_index = i1
                            #จะ print คำ ก็ให้เริ่มจาก start index ที่ update แล้ว ไปถึง start index ที่ + ความยาวเข้าไป
                            longest_common = self.text_1[start_index:start_index + max_length]
        
        print(f"Starting index : {start_index}")
        print(f"Length of longest common substring : {max_length}")
        print(f"Longest common substring : {longest_common}")
        
        return [longest_common, max_length]

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
        # print(set(self.text_1), set(self.text_2), set(self.text_1).intersection(set(self.text_2)), len(set(self.text_1).intersection(set(self.text_2))))
        condition = len(self.text_1) == 0 or len(self.text_2) == 0 or len(set(self.text_1).intersection(set(self.text_2))) == 0
        # print(condition)
        if condition:                                                                    # เช็คว่าถ้าจำนวนสมาชิกเป็น 0/ไม่ซ้ำ return เลย
            print(f"\nLongest substring is \"\" with \"0\" letters.")
            return ["", 0]

        possible_result, i = [], 0                                                       # สร้างตัวแปร possible_result มาเพื่อเก็บค่าของ [word -> คำที่ซ้ำ, k -> จำนวนอักษร], i -> iteration couter.
        while i < len(self.text_1):                                                      # while ใน self.text_1, iteration couter -> i.
            j, k, word = 0, 0, ""                                                        # j -> iteration couter, k -> letter couter, word -> letter collecter.
            while j < len(self.text_2):                                                  # while ใน self.text_2, iteration couter -> j.
                if i + k < len(self.text_1) and self.text_1[i+k] == self.text_2[j]:      # เช็คว่าเจอตัวซ้ำมั้ย โดยถ้าเจอจะขยับขึ้นไปทีละ k หน่วย เพื่อไปยังตัวอักษรถัดไป.
                    word += self.text_2[j]                                               # เก็บตัวอักษรที่เจอไว้ใน word.
                    k += 1                                                               # เพิ่มค่าของ k ขึ้น 1 หน่วยเพื่อนับตัวซ้ำและใช้ในการขยับ.
                elif k != 0:
                    possible_result.append([word, k])                                    # กรณีที่ผ่าน if แล้ว k != 0 จะทำการเก็บค่าของ [word, k] ไว้ใน possible_result.
                    k = 0
                j += 1                                                                   # increasing condition for loop j.
            if k != 0:
                possible_result.append([word, k])                                        # เม่ือผ่าน loop แล้ว k != 0 จะทำการเก็บค่าของ [word, k] ไว้ใน possible_result.
                k = 0
            # if i == len(self.text_1) - 1 and possible_result == []:
            #     possible_result.append(["", 0])                                          # ถ้าจบลูปสุดท้ายแล้วไม่มีอะไรที่ตรงเลยจะ append ["", 0]
            i += 1                                                                       # increasing condition for loop i.

        result = max(possible_result, key = len)                                         # เก็บค่าผลลัพธ์ที่มากที่สุดไว้ในตัวแปร result.
        print(possible_result, result)
        print(f"\nLongest substring is \"{result[0]}\" with \"{result[1]}\" letters.")   # ปริ้นท์ต่านั้นออกมา.
        return result
