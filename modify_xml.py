import xml.etree.ElementTree as ET
import sys

mytree = ET.parse('log.xml')
myroot = mytree.getroot()
reading = float(sys.argv[1])
for old_value in myroot.iter('OLD'):
	for new_value in myroot.iter('NEW'):
		old_value.text = new_value.text
		for consumption in myroot.iter('CONSUMPTION'):
			consumption.text = str(round(reading - float(new_value.text), 1))
		new_value.text = str(reading)
mytree.write('log.xml')
