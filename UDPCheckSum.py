import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button


def calculate_checksum(datalist):
    sum = 0
    max_value = 0b1111111111111111
    sub_value = 0b10000000000000000
    for i in datalist:
        i = '0b' + i
        i = int(i, base=2)
        # print(i)
        sum += i
        # 产生了进位
        if sum > max_value:
            sum -= sub_value
            sum += 1
        # 和全1异或相当于取反
    return sum ^ max_value


# datalist 不包含检验和
# checksum 是检验和
def calculate_sum(datalist, checksum):
    sum = 0
    max_value = 0b1111111111111111
    sub_value = 0b10000000000000000
    for i in datalist:
        i = '0b' + i
        i = int(i, base=2)
        # print(i)
        sum += i
        # 产生了进位
        if sum > max_value:
            sum -= sub_value
            sum += 1
    return (sum + checksum)
    # sum = sum ^ max_value
    # return (sum + checksum) == max_value


datalist = ['0110011001100000','0101010101010101','1000111100001100']

textbox1 = TextBox(plt.axes([0.3, 0.8, 0.5, 0.075]), 'packet1',
                   initial=datalist[0])

textbox2 = TextBox(plt.axes([0.3, 0.7, 0.5, 0.075]), 'packet2',
                   initial=datalist[1])

textbox3 = TextBox(plt.axes([0.3, 0.6, 0.5, 0.075]), 'packet3',
                   initial=datalist[2])
button = Button(plt.axes([0.45, 0.2, 0.2, 0.075]), "check")

def button_click(event):
    datalist.clear()
    datalist.append(textbox1.text)
    datalist.append(textbox2.text)
    datalist.append(textbox3.text)
    textbox4 = TextBox(plt.axes([0.3, 0.5, 0.5, 0.075]), 'checksum',
                   initial=str(bin(calculate_checksum(datalist)).replace('0b','')))
    textbox5 = TextBox(plt.axes([0.3, 0.4, 0.5, 0.075]), 'sum',
                   initial=str(bin(calculate_sum(datalist, int(textbox4.text, 2))).replace('0b','')))
    content = " "
    if textbox5.text == "1111111111111111":
        content = "Check Successfully"
    else:
        content = "Check Failure"
    textbox6 = TextBox(plt.axes([0.3, 0.3, 0.5, 0.075]), 'result', initial=content)
    plt.show()


button.on_clicked(button_click)

plt.show()