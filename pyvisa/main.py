import pyvisa
rm = pyvisa.ResourceManager(visa_library="C:\\Windows\\System32\\nivisa64.dll")
print(rm.list_resources())
my_instrument = rm.open_resource('ASRL13::INSTR')
print(my_instrument.query('*IDN?'))


