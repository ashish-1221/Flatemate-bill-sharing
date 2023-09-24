from fpdf import FPDF
import webbrowser

class Bill:
    """
    Object that contains data about a bill
    such as total amount of the bill and the 
    period of the bill
    """
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period
    
class Flatmate:
    """
    Creates a flatmate object which gives the 
    following information,
    1. name of the flatmate
    2. how many days the flatmate hass stayed
    3. Taking the bill class how much of the 
    bill is he owed??
    """
    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    
    def pays(self,bill,flatmate2):
        weight = self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        return weight*bill.amount

class Pdfreport:
    """
    create a PDF report containing the flatmate
    details such as name, due amount and
    """
    def __init__(self,filename) -> None:
        self.filename = filename
    
    def generate(self,flatmate1,flatmate2,bill):
        pdf = FPDF(orientation="portrait",unit="pt",format="A4")
        pdf.add_page()
        
        # Add title
        pdf.set_font(family="Times",size=24,style="B")
        pdf.cell(w=0,h=80,txt="Flatmates' Bill Report Summary",align="C",ln=1)
        
        # Insert the labels Flatmate, period and amount 
        pdf.cell(w=100,h=40,txt="Flatmate",border=1,align="C")
        pdf.cell(w=130,h=40,txt='Period',border=1,align="C")
        pdf.cell(w=100,h=40,txt="Amount",border=1,align="C",ln=1)
        
        #Insert the first flatmate name, bill period and amount owed
        pdf.set_font(family="Times",size=18)
        pdf.cell(w=100,h=40,txt=flatmate1.name,border=1)
        pdf.cell(w=130,h=40,txt=bill.period,border=1)
        pdf.cell(w=100,h=40,txt=str(round(flatmate1.pays(bill,flatmate2),2)),border=1,ln=1)
        
        #Insert the second flatmate name, bill period and amount owed
        pdf.cell(w=100,h=40,txt=flatmate2.name,border=1)
        pdf.cell(w=130,h=40,txt=bill.period,border=1)
        pdf.cell(w=100,h=40,txt=str(round(flatmate2.pays(bill,flatmate1),2)),border=1,ln=1)
        
        pdf.output(self.filename)
        webbrowser.open(self.filename)
        
# Calling of the functions
bill_amount = float(input('Hey user enter the bill amount:-'))
bill_period = input("Please enter the bill period:-")
bill = Bill(amount=bill_amount,period=bill_period)

flatmate1_name = input("Enter the name of the first flatmate:-")
flatmate1_days_in_house = int(input("Enter the no of days flatmate stayed:-"))
ashish = Flatmate(name=flatmate1_name,days_in_house=flatmate1_days_in_house)

flatmate2_name = input("Enter the name of the second flatmate:-")
flatmate2_days_in_house = int(input("Enter the no of days flatmate stayed:-"))
jeevan = Flatmate(name=flatmate2_name,days_in_house=flatmate2_days_in_house)

pdf_file = Pdfreport("billsummary.pdf")
pdf_file.generate(ashish,jeevan,bill)

    