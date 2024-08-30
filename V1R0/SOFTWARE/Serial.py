import serial  # used to open serial port
import serial.tools.list_ports  # used to list the avaliable serial ports

def print_available_com_ports():
    """ Prints all the available serial ports
    :returns: A list of the serial ports available on the system
    """
    ports = serial.tools.list_ports.comports()
    print("Available COM ports:")
    port_found_n = 0
    for port, description, hw_id in sorted(ports):
        if description.startswith("STMicroelectronics STLink Virtual COM Port") or \
                description.startswith("Silicon Labs Dual CP2105 USB to UART Bridge:"):
            print("\t{}".format(description))
            port_found_n += 1

    if port_found_n == 0:
        print("\tNo compatible COM port found")
    print("")


def send_msg(ser, msg, wait_answer=True):
    bytes(msg)
    ser.write(msg)
    if wait_answer:
        response = read_msg(ser)
        return response

    return None

def read_msg(ser):
    msg = ser.read()
    print(msg)
    return msg


if __name__ == "__main__":
    print_available_com_ports()
    port_name_cord = input(
        "Enter the serial port name for the coordinator (e.g., COM1 or /dev/ttyUSB0): ")
    
    baud_rate = 115200  # standart baud_rate
    ser = serial.Serial(port_name_cord, baud_rate, timeout=3)
    msg = 30
    
    send_msg(ser, msg)
    
    


