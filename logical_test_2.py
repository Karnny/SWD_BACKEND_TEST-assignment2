
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def arabic_to_roman(number):
    if not 0 < number < 1000:
        raise ValueError("Number must be between 1 and 1000")

    arabic_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]

    roman_numeral = ""
    for i in range(len(arabic_values)):
        while number >= arabic_values[i]:
            roman_numeral += roman_numerals[i]
            number -= arabic_values[i]

    return roman_numeral


if __name__ == "__main__":
    try:
        # Example usage
        arabic_number = int(input("Enter arabic number: "))
        roman_number = arabic_to_roman(arabic_number)
        print(f"{arabic_number} in Roman number is: {roman_number}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Invalid input. Please enter a valid number.", e)