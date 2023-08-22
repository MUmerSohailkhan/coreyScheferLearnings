class Company:
    noOfCompanies=0
    def __init__(self,name,registrationNo,ntnNumber,CEOName,shareholderName,boardOfDirectors,initialInvestments):
        self.name=name
        self.registrationNo=registrationNo
        self.ntnNumber=ntnNumber
        self.CEOName=CEOName
        self.shareholderName=shareholderName
        self.boardOfdirectors=boardOfDirectors
        self.initialInvestments=initialInvestments
        Company.noOfCompanies+=1

    def saveshareholdernames(self):
        with open('shareHolderInfo.txt','w') as file:
            for x in self.shareholderName:
                print(x,',',end='\n',file=file)

    def displayShareHolderName(self):
        with open('shareHolderInfo.txt' ,'r') as file:
            data=file.readlines()
        return data


    def addShareHolder(self,name):
        with open('shareHolderInfo.txt','a') as file:
            print(name,',',end='\n',file=file)

    def showProducts(self):
        products=['sports ground','trainings']
        return products


    # @classmethod
    #
    # @staticmethod

zigmaxsports=Company('zigmaxsports','L1f16bscs0093',823892938,'M Umer Sohail Khan',['M Umer Sohail Khan','Irtan Afzal Khan','Sana Sohail Khan',
                     'Noor bakht','Talha Liaqat Khan','Sohail Younas Khan','Rashid Khan'],['Rashid Khan','Irtan Afzal Khan'],30000000)
# zigmaxsports.saveshareholdernames()
print(zigmaxsports.displayShareHolderName())
# zigmaxsports.addShareHolder('Asif Sohail Khan')
# print(zigmaxsports.displayShareHolderName())
