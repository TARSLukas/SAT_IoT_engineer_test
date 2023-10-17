import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import random
import time


#建立BodbusTCP的Server端
server = mt.TcpServer(port = 502)
server.start()

#建立6個檢測站的暫存器
slave_1 = server.add_slave(1)
slave_1.add_block('0', md.HOLDING_REGISTERS, 40001, 100)
slave_2 = server.add_slave(2)
slave_2.add_block('0', md.HOLDING_REGISTERS, 40003, 100)
slave_3 = server.add_slave(3)
slave_3.add_block('0', md.HOLDING_REGISTERS, 40005, 100)
slave_4 = server.add_slave(4)
slave_4.add_block('0', md.HOLDING_REGISTERS, 40007, 100)
slave_5 = server.add_slave(5)
slave_5.add_block('0', md.HOLDING_REGISTERS, 40009, 100)
slave_6 = server.add_slave(6)
slave_6.add_block('0', md.HOLDING_REGISTERS, 40011, 100)

#模擬檢測站檢測產品，沒有產品:良品:不良品的比例設定為5:85:10
def product_state(x):
    if x < 6:
        return 0
    elif x < 90:
        return 1
    else:
        return 2

while True:
    #取得檢測站1的產品檢測狀態，並寫入到檢測站1的暫存器中
    slave = server.get_slave(1)
    set_value = product_state(random.randint(1,100))
    slave.set_values('0', 40001, set_value)
    value1 = slave.get_values('0', 40001, 1)
    print('檢測站1狀態: ', str(value1[0]), end = ' ,')
    
    #取得檢測站2的產品檢測狀態，並寫入到檢測站2的暫存器中
    slave = server.get_slave(2)
    set_value2 = product_state(random.randint(1,100))
    slave.set_values('0', 40003, set_value2)
    value2 = slave.get_values('0', 40003, 1)
    print('檢測站2狀態: ', str(value2[0]), end = ' ,')
    
    #取得檢測站3的產品檢測狀態，並寫入到檢測站3的暫存器中
    slave = server.get_slave(3)
    set_value3 = product_state(random.randint(1,100))
    slave.set_values('0', 40005, set_value3)
    value3 = slave.get_values('0', 40005, 1)
    print('檢測站3狀態: ', str(value3[0]), end = ' ,')
    
    #取得檢測站4的產品檢測狀態，並寫入到檢測站4的暫存器中
    slave = server.get_slave(4)
    set_value4 = product_state(random.randint(1,100))
    slave.set_values('0', 40007, set_value4)
    value4 = slave.get_values('0', 40007, 1)
    print('檢測站4狀態: ', str(value4[0]), end = ' ,')
    
    #取得檢測站5的產品檢測狀態，並寫入到檢測站5的暫存器中
    slave = server.get_slave(5)
    set_value5 = product_state(random.randint(1,100))
    slave.set_values('0', 40009, set_value5)
    value5 = slave.get_values('0', 40009, 1)
    print('檢測站5狀態: ', str(value5[0]), end = ' ,')
    
    #取得檢測站6的產品檢測狀態，並寫入到檢測站6的暫存器中
    slave = server.get_slave(6)
    set_value6 = product_state(random.randint(1,100))
    slave.set_values('0', 40011, set_value6)
    value6 = slave.get_values('0', 40011, 1)
    print('檢測站6狀態: ', str(value6[0]))
    
    time.sleep(1)