"""
This file for longest substring search algorithm
"""

class Competition():
    def __init__(self, text_1:str, text_2:str):
        self.text_1 = text_1
        self.text_2 = text_2

    def tao_algorithm(self):
        """
        Algorithm from tao
        """
        # ใช้ เซต ในการช่วยหาตัวอักษรที่ซ้ำกันก่อน
        common_chars = set(self.text_1) & set(self.text_2)
        #print(f"common characters in both texts are :{common_chars}")
        #เราเช็คได้ทันทีว่า ถ้ามันไม่มีตัวอักษรที่เหมือนเลยจะได้เซตว่างแล้วหยุดการทำงานได้เลยไม่ต้อง run ต่อ
        if common_chars == set() or (self.text_1 == "" and self.text_2 == "") :
            print("There is no common substring found between the two texts")
            return (-1,-1,0)
        else:
            common_chars = sorted(common_chars)
            #max_length จะเก็บค่าความยาวที่มากที่สุดของ subtext ที่เหมือนกัน
            max_length = 0
            #start_index จะเอาไว้เช็คว่าตัวที่เริ่มเหมือนกัน(ดูจาก text1 เป็นหลัก) ว่าอยู่ index ไหน
            start_index = 0
            start_index2 = 0

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
                            start_index2 = i2
                            #จะ print คำ ก็ให้เริ่มจาก start index ที่ update แล้ว ไปถึง start index ที่ + ความยาวเข้าไป
                            longest_common = self.text_1[start_index:start_index + max_length]
        
            print(f"Starting index : {start_index}")
            print(f"Length of longest common substring : {max_length}")
            print(f"Longest common substring : {longest_common}")
        
            return (start_index,start_index2, max_length)

    def kantong_algorithm(self):
        """
        Algorithm from kantong
        """

    def tonkaow_algorithm(self):
        """
        Algorithm from tonkaow
        """

    def ton_algorithm(self) -> tuple:
        """
        Algorithm from ton
        """
        # null_condition = len(self.text_1) == 0 or len(self.text_2) == 0 or len(set(self.text_1).intersection(set(self.text_2))) == 0
        # equal_condtion = self.text_1 == self.text_2
        # # condition เอาไว้เช็คว่าตัว text ที่เข้ามามีขนาดเป็น 0 หรือ ไม่มีตัวซ้ำกันมั้ย ถ้าใช่จะ return ออกไปเลย
        # if null_condition:
        #     print(f"\nDon't match any substring.")
        #     return (-1, -1, 0)
        # if equal_condtion:
        #     print(f"\nFirst index: {0}\nSecond index: {0}\nLength: {len(self.text_1)} letters.")
        #     return (0, 0, len(self.text_1))

        # result, i, max_k = [], 0, 0                                                     # สร้างตัวแปรมาเก็บค่าของ result, i และ max_k (เก็บค่าความยาวคำสูงสุด)
        # while i < len(self.text_1):
        #     j, k = 0, 0                                                                 # สร้างตัวแปร ่่k มาเพื่อใช้ในการนับคำและขยับ
        #     while j < len(self.text_2):
        #         if i + k < len(self.text_1) and self.text_1[i+k] == self.text_2[j]:     # เช็คว่าเจอคำเหมือนหรือเปล่าถ้าเจอจะทำการเพ่ิ่มค่า k ขึ้น 1 หน่วย
        #             k += 1
        #         elif k > max_k:                                                         # ถ้าผ่าน if แรกมาได้จะทำการเช็ตว่าค่า k > max_k หรือไม่
        #             max_k = k                                                           # ทำการอัปเดตค่า max_k
        #             result = (i, j-k, max_k)                                            # ทำการอัปเดตค่า result ปัจจุบัน
        #             k = 0; j = i                                                        # เช็ตค่า k = 0 เพื่อเริ่มเช็คคำใหม่
        #             # j = i + 1                                                           # สำหรับ case15
        #         elif j-k > 0: k = 0
        #         j += 1
        #     if k > max_k:                                                               # กรณีผ่าน if แรกมาได้จะทำการเช็คซ้ำเป็นครั้งที่ 2 (ใช่กรณีคำซ้ำกัน)
        #         max_k = k
        #         result = (i, j-k, max_k)
        #         k = 0
        #     i += 1

        # print(f"\nFirst index: {result[0]}\nSecond index: {result[1]}\nLength: {result[2]} letters.")
        # return result
        text_1, text_2 = self.text_1, self.text_2
        text_1_size, text_2_size = len(text_1), len(text_2)

        base_matrix = [[[0] * text_1_size] * text_2_size, [[0] * text_1_size] * text_2_size]
        print(base_matrix)

        # for i in range(len(text_1)):
        #     for j in range(len(text_2)):
        #         print(base_matrix[i][j])