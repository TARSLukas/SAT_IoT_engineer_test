import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import time


#建立BodbusTCP的Client端
master = mt.TcpMaster('localhost', port = 502)
master.set_timeout(5.0)

#計算良品與不良品的總數
number_product_OK = 0
number_product_NG = 0
def check_compute(check):
    global number_product_OK,number_product_NG
    
    if check == 1:
        number_product_OK += 1
    elif check == 2:
        number_product_NG += 1
    
while True:
    try:
        #獲取6個檢測站的檢測狀態
        check_1 = master.execute(slave = 1, function_code = md.READ_HOLDING_REGISTERS, starting_address = 40001, quantity_of_x = 1)
        check_2 = master.execute(slave = 2, function_code = md.READ_HOLDING_REGISTERS, starting_address = 40003, quantity_of_x = 1)
        check_3 = master.execute(slave = 3, function_code = md.READ_HOLDING_REGISTERS, starting_address = 40005, quantity_of_x = 1)
        check_4 = master.execute(slave = 4, function_code = md.READ_HOLDING_REGISTERS, starting_address = 40007, quantity_of_x = 1)
        check_5 = master.execute(slave = 5, function_code = md.READ_HOLDING_REGISTERS, starting_address = 40009, quantity_of_x = 1)
        check_6 = master.execute(slave = 6, function_code = md.READ_HOLDING_REGISTERS, starting_address = 40011, quantity_of_x = 1)
        print("檢測站1狀態: ", check_1[0], ", 檢測站2狀態: ", check_2[0], ", 檢測站3狀態: ", check_3[0],
              ", 檢測站4狀態: ", check_4[0], ", 檢測站5狀態: ", check_5[0], ", 檢測站6狀態: ", check_6[0])
        
    except:
        print("connect fail")
        
    check = check_1 + check_2 + check_3 + check_4 + check_5 + check_6
    for n in range(len(check)):
        check_compute(check[n])
    print("目前的良品總數: ", number_product_OK, "目前的不良品總數: ", number_product_NG)
            
    time.sleep(1)