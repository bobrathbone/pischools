import smbus
 import sys

 import time

 bus = smbus.SMBus(1)

 address = 0x20
 bus.write_byte_data(address,0x00,0x07) # set A7-A3 as output pins and A2-A0 as input pins                            
 bus.write_byte_data(address,0x01,0x00) # set B7-B0 as output pins

 def main():
      a = 0 
      b = 0
      inp = 0
 delay = 0.05

 while True: 
   # turn of all LEDs in bank B
   b = 0    # 00000000   
   bus.write_byte_data(address,0x13,b)

   # turn on LED connected to A7 (used as power for input circuit)    
   a = 128  # 10000000  
   bus.write_byte_data(address,0x12,a)

   # read input from bank a and store to "inp" variable
    inp = bus.read_byte_data(address,0x12)

   # check if button at A0 is pressed, if true run LEDs from B0 to B7     
   if inp == 129:  # 10000001      
     for x in range(0,8):
       a = 1 << x
       bus.write_byte_data(address,0x13,a)
       time.sleep(delay)
           
   # check if button at A1 is pressed, if true run LEDs from B7 to B0
   if inp == 130:  # 10000010       
      for x in range(7,-1,-1):
        a = 1 << x
        bus.write_byte_data(address,0x13,a)
        time.sleep(delay)

   # check if button at A2 is pressed, if true run two LEDs at a time  from B0 to B7 and back
   if inp == 132: # 10000100
      for x in range(0,8):
        a = 3 << x
        bus.write_byte_data(address,0x13,a)
        time.sleep(delay)
        
      for x in range(7,-1,-1):
        a = 3 << x
        bus.write_byte_data(address,0x13,a)
        time.sleep(delay)
          
 if __name__ == "__main__":
   
    main()
