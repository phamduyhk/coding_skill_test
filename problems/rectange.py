"""
coding test: given 2 rectangles with top-right and bottom-left coordinates
return the top-right and bottom-left coordinates of the intersection.
"""
t = 5
r = 15
b = 20
l = 0

arr = [i for i in range(10)]
arr.extend([1,2,3])
# print(arr)


import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    for i, v in enumerate(lines):
        lines[i].replace("o", "t")
        lines[i].replace("x", "o")
        lines[i].replace("t", "x")
        print(lines[i])
    return lines

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    result = main(lines)
    for item in result:
        print(item)
    
