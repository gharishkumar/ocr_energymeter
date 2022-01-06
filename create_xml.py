import xml.etree.cElementTree as ET

log = ET.Element("LOG")
reasing = ET.SubElement(log, "READING")

ET.SubElement(reasing, "OLD").text = "1231.5"
ET.SubElement(reasing, "NEW").text = "1359.5"
ET.SubElement(reasing, "CONSUMPTION").text = "127"
ET.SubElement(reasing, "TAMPERING").text = " "
ET.SubElement(reasing, "COMPLAINT").text = " "

tree = ET.ElementTree(log)
tree.write("log_1.xml")