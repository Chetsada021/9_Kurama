from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry("600x500")
GUI.title("โปรแกรมคำนวณ vat")

FONT1 = ("Angsana New",20)
FONT2 = ("Angsana New",15)
#ช่องกรอกข้อมูล (ชื่อสินค้า)
L = ttk.Label (GUI,text = "ชื่อสินค้า",font = FONT1).pack() #ข้อความแสดง

v_product = StringVar() #ตัวแปรสำหรับเก็บชื่อสินค้าตอนพิมพ์
E1 =ttk.Entry(GUI,textvariable = v_product)
E1.pack(ipadx=30 ,ipady=10)
#ช่องกรอกราคา
L = ttk.Label (GUI,text = "ราคาสินค้า",font = FONT1).pack() #ข้อความแสดง

v_price = StringVar() #ตัวแปรสำหรับเก็บราตาสินค้าตอนพิมพ์
E2 =ttk.Entry(GUI,textvariable = v_price)
E2.pack(ipadx=30 ,ipady=10)
#ช่องกรอกจำนวนสินค้า
L = ttk.Label (GUI,text = "จำนวนสินค้า",font = FONT1).pack() #ข้อความแสดง

v_quantity = StringVar() #ตัวแปรสำหรับเก็บจำนวนสินค้าตอนพิมพ์
E3 =ttk.Entry(GUI,textvariable = v_quantity)
E3.pack(ipadx=30 ,ipady=10)

## Radio เลือกประเภท vat ##

F1 =Frame(GUI)
F1.pack()

v_radio = StringVar()

R1 = ttk.Radiobutton(F1,text="ราคารวม vat แล้ว",variable=v_radio,value="ic")
R1.grid(row=0,column=0)

R1.invoke() #เลือกเป็นค่าเริ่มต้น

R2 = ttk.Radiobutton(F1,text="ราคา +  vat 7%",variable=v_radio,value="av")
R2.grid(row =0 ,column=1)

R3 = ttk.Radiobutton(F1,text="ราคาไม่รวม vat แล้ว",variable=v_radio,value="nic")
R3.grid(row=0,column=2)

#ปุ่มกดเพื่อคำนวณ
def Calc(event=None):
    #print('RADIO:',v_radio.get())
    #print(type(int(v_price.get())))
    product = v_product.get()
    price = int(v_price.get()) #int เป็นคำสั่งแปลงข้อความเป็นตัวเลข "2"--> 2
    quantity = int(v_quantity.get())
    total = price * quantity

    if v_radio.get() == 'ic':
        vat7 = total*(7/107)
        nettotal = total*(100/107) 
        #print("ราคาก่อน VAT :{:.2f} (VAT 7% : {:.2f})".format(nettotal,vat7))

        v_result.set("สินค้า : {} จำนวน  {:,} ชิ้น ทั้งหมด {:,} บาท ({:,} บาท/ชิ้น) \n ราคาสินค้า: {:.2f}.- VAT 7%: {:.2f}.- ".format(product,
                                                                                                                quantity,
                                                                                                                total,
                                                                                                                price,
                                                                                                                nettotal,
                                                                                                                vat7)) #เรียงตามลำดับ
    elif v_radio.get() =='av':
        vat7 = total*(7/107)
        nettotal = total*(100/107)
        sumtotal = total + vat7 
        v_result.set("สินค้า : {} จำนวน {:,} ชิ้น ทั้งหมด {:.2f} บาท ({:.2f} บาท/ชิ้น) \n ราคาสินค้า: {:.2f}.- VAT 7%: {:.2f}.- ".format(product,
                                                                                                                quantity,
                                                                                                                sumtotal,
                                                                                                                price + (vat7/quantity),
                                                                                                                nettotal,
                                                                                                                    vat7))
    else:
        v_result.set("สินค้า : {} จำนวน {:,} ชิ้น ทั้งหมด {:.2f} บาท ({:.2f} บาท/ชิ้น) \n  ".format(product,
                                                                                                                quantity,
                                                                                                                total,
                                                                                                                price))                                
                                                                                                        

B1 =ttk.Button(GUI,text = 'Calculate',command=Calc)
B1.pack(ipadx = 20,ipady=10,pady=10)

E3.bind("<Return>",Calc)

#ผลลัพธ์จากการคำนวณ
v_result=StringVar()
v_result.set("<<<ผลลัพธ์โชว์จุดนี้>>>") #โชว์ข้อมูลเริ่มต้น
R1 = ttk.Label(GUI,textvariable=v_result,font = FONT1)
R1.pack()




GUI.mainloop()