import qrcode,webbrowser
from reportlab.pdfgen import canvas
def getTotal(list):
  total=0
  for data in list:
    total=total+data[4]
  return total

def getTotalTax(list):
  totalTax=0
  for data in list:
    totalTax=totalTax+data[5]
  return totalTax

def getTotalDis(list):
  totalDis=0
  for data in list:
    totalDis=totalDis+data[3]
  return totalDis

def rightalingn(pdf,string,left,right,ycoordinate):
  length=len(string)
  totalLength=(right-left)/7
  print(totalLength)
  spaces=int(totalLength-length)
  print(spaces)
  pdf.drawString(right,ycoordinate," "*spaces)
  left=left+(7*spaces)
  pdf.drawString(left,ycoordinate,string)

def header(header,pdf):
  pdf.setTitle(header.date+"Invoice")
  # logo="logo.jpeg"
  # pdf.drawInlineImage(logo,190,253)

  pdf.line(30,815,350,815)
  pdf.setFont("Courier-Bold",20)
  pdf.drawString(30,800,"          KILIG EVENTS")
  pdf.setFont("Courier-Bold",11)
  pdf.drawString(30,785,"(make your events more colourful with us)")
  pdf.drawString(30,770,"K.Kannan")
  pdf.drawString(30,755,"4002 TNHB COLONY VILLAPURAM, MADURAI")
  pdf.drawString(30,740,"Kiligevents610@gmail.com, Phone:7010516857 ")

  pdf.line(30,735,350,735)

  pdf.drawString(30,720,"Invoice Number: "+ str(int(header.InvoiceNumber)))
  pdf.drawString(30,705,"Customer Name: "+ str(header.CustomerName))
  pdf.drawString(30,690,"Contact Number: "+ str(header.CustomerContact))
  pdf.drawString(30,675,"Date: "+ str(header.date))
  
  qr = qrcode.QRCode(
      version=1,
      box_size=2,
      border=2
    )
    
  data = 'InvoiceNumber:'+str(int(header.InvoiceNumber))+'\nTime:'+(header.date+"--"+header.time)+"\nGoogle Map: https://goo.gl/maps/DV59uHs2eoYpuvsC9\nTerms & Conditions:\n1:Sold items will not be returned or changed.\n2:Every dispute will settled in Mau Court.\n3:Battery, Charger, Mobile warranty is provided by service center.\nTHANK YOU"
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill='black', back_color='white')
  #img="KILIG LOGO.jpg"
  pdf.drawInlineImage(img,400,680)
  

def middle(pdf):
  pdf.line(30,650,550,650)
  
  pdf.drawString(30,655,"Sr.No.")
  pdf.drawString(75,655,"Product Name")
  pdf.drawString(200,655,"Quantity")
  pdf.drawString(260,655,"Rate")
  pdf.drawString(320,655,"Discount")
  pdf.drawString(400,655,"Total")
  pdf.drawString(490,655,"Tax")
  
  pdf.line(30,665,550,665)
  pdf.line(73,662,73,150)
  pdf.line(198,662,198,150)
  pdf.line(258,662,258,150)
  pdf.line(318,662,318,150)
  pdf.line(398,662,398,150)
  pdf.line(488,662,488,150)
  pdf.line(30,150,550,150)

def additem(product,pdf,ycoordinate):
  while(len(product.name)>18):
    pdf.drawString(75,ycoordinate,product.name[:18]+"-")
    product.name=product.name[18:]
    ycoordinate=ycoordinate-15
  
  pdf.drawString(75,ycoordinate,product.name)
  pdf.drawString(200,ycoordinate,str(product.quantity))
  rightalingn(pdf,"%.2f" %product.rate,260,316,ycoordinate)
  print(product.rate)
  rightalingn(pdf,"%.2f" %product.discount,320,398,ycoordinate)
  rightalingn(pdf,"%.2f" %product.total,400,488,ycoordinate)
  rightalingn(pdf,"%.2f" %product.tax,490,552,ycoordinate)
  return (ycoordinate-15)

def footer(pdf,list):
  pdf.drawString(30,135,"Total Discount:")
  rightalingn(pdf,"-"+"%.2f" %getTotalDis(list)+" INR",393,488,135)
  pdf.drawString(30,120,"Gross Total(Discount Included):")
  rightalingn(pdf,"%.2f" %getTotal(list)+" INR",400,488,120)
  pdf.drawString(30,105,"Tax:")
  rightalingn(pdf,"+"+"%.2f" %getTotalTax(list)+" INR",393,488,105)
  pdf.line(30,100,550,100)
  pdf.drawString(30,90,"Grand Total: ")
  rightalingn(pdf,"%.2f" %(getTotal(list)+getTotalTax(list))+" INR",400,488,90)
  pdf.drawString(400,50,"Authorized Signatory")
  pdf.setFont("Courier-Bold",7)
    

def About():
  pdf=canvas.Canvas("D:\\InvoiceGenerator\\about.pdf")
  pdf.setFont("Courier-Bold",20)
  pdf.drawString(40,700,"Adithya Harish")
  pdf.setFont("Courier-Bold",15)
  pdf.drawString(40,650,"Student, Information Technology ")
  pdf.drawString(40,630,"")
  pdf.drawString(40,610,"PSG College of Technology")
  pdf.drawString(40,550,"Contact: 9489480346")
  pdf.save()
  webbrowser.open("D:\\InvoiceGenerator\\about.pdf")

