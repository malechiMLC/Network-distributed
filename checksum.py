import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

data = ['0110011001100000', '0101010101010101', '1000111100001100']


def get_checksum(data):
    sum = 0
    op = 0b1 << 16
    for i in data:
        i = int(i, base=2)
        sum += i
        if sum >= op:
            sum += 0b1
            sum -= op

    result = sum ^ (op - 0b1)
    return result


def get_sum(data, checksum):
    sum = 0
    op = 0b1 << 16
    for i in data:
        i = int(i, base=2)
        sum += i
        if sum >= op:
            sum += 0b1
            sum -= op
    result = sum + checksum
    return result


data1 = TextBox(plt.axes([0.3, 0.8, 0.3, 0.05]), 'data 1', initial=data[0])
data2 = TextBox(plt.axes([0.3, 0.7, 0.3, 0.05]), 'data 2', initial=data[1])
data3 = TextBox(plt.axes([0.3, 0.6, 0.3, 0.05]), 'data 3', initial=data[2])
checksum = TextBox(plt.axes([0.3, 0.5, 0.3, 0.05]), 'checksum')
result = TextBox(plt.axes([0.3, 0.4, 0.3, 0.05]), 'result')
button = Button(plt.axes([0.4, 0.2, 0.3, 0.03]), 'check')


def button_click(event):
    data.clear()
    data.append(data1.text)
    data.append(data2.text)
    data.append(data3.text)
    checksum_txt = str(bin(get_checksum(data)).replace('0b', ''))
    checksum.set_val(checksum_txt)
    result_txt = str(
        bin(get_sum(data, int(checksum.text, 2))).replace('0b', ''))
    result.set_val(result_txt)
    plt.show()


button.on_clicked(button_click)

plt.show()
