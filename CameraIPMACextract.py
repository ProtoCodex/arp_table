from bs4 import BeautifulSoup as bs
import csv


content =[]

xmlist =["actipi.xml","HikVisionPI.xml","axispi.xml","onvifnvcpi.xml"]

with open("IPandMac.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","IpAddress", "Mac"])
    for x in xmlist:
        with open(x,"r") as myfile:
            content = myfile.readlines()
            content="".join(content)
            bs_content = bs(content,features="xml")
            for i in bs_content.find_all("Device", Enabled="1", Port="80"):
                writer.writerow([i["Name"],i["ipAddress"],i["Serial"]])