
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

txt_constant = {
    'default_result': 'ศูนย์',
    'single_unit_strs': ['', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า'],
    'place_name_strs': ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']
}


def numToWord(nums):
    result = ''
    length = len(nums)
    max_len = 7

    if length > max_len:
        overflow_index = length - max_len + 1
        overflow_nums = nums[:overflow_index]
        remaining_nums = nums[overflow_index:]
        return numToWord(overflow_nums) + 'ล้าน' + numToWord(remaining_nums)
    else:
        for i in range(length):
            digit = nums[i]
            if digit > 0:
                result += txt_constant['single_unit_strs'][digit] + txt_constant['place_name_strs'][length - i - 1]

    return result


def ten_grammar_fix(s):
    return s.replace('หนึ่งสิบ', 'สิบ').replace('สองสิบ', 'ยี่สิบ').replace('สิบหนึ่ง', 'สิบเอ็ด')


def numToThaiText(num):
    if num == 0:
        return txt_constant['default_result']
    
    if num >= 10_000_000:
        raise ValueError("Input value must not equal or greater than 10 million.")

    positive_num = abs(num)
    num_str = str(int(positive_num))

    num_arr = [int(d) for d in num_str]

    thai_text_str = numToWord(num_arr)

    thai_text_str = ten_grammar_fix(thai_text_str)

    return thai_text_str


if __name__ == "__main__":
    try:
        num = int(input("Enter a number to convert to Thai text: "))
        thai_text_str = numToThaiText(num)
        print(f"The Thai text representation of {num} is: {thai_text_str}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Invalid input. Please enter a valid number.", e)
