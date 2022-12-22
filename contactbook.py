import csv
class person:
    def __init__(self,name,email,phone,nickname):
        self.name=name
        self.email=email
        self.phone=phone
        self.nickname=nickname
class contactbook:
    def __init__(self):
        self.contacts=[]
        
    def addperson(self,name,email,phone,nickname):
        contact=person(name,email,phone,nickname)
        self.contacts.append(contact)
        self.save()
    def showallmembers(self):
        for contact in contacts:
            self.printcontact(contact)
    def deletecon(self,name):
        for idx,contact in enumerate(self.contacts):
            if contact.name.lower()==name.lower():
                del self.contacts[idx]
                self.save()
                break
    def search(self,name):
        for contact in contacts:
            if contact.name.lower()==name.lower():
                self.printcontact(contact)
                break
        else:
            self.notfound()
    def update(self,name):
        for contact in contacts:
            if contact.name>lower()==name.lower():
                self.printcontact()
                for idx,contact in enumerate(contacts):
                    if contact.name.lower()==name.lower():
                        del self.contacts[idx]
                print(' ')
                print("enter updated detials: ")
                name=str(input('enter your updated name: '))
                phone=str(input('enter your updated phone number: '))
                email=str(input('enter your updated email: '))
                nickname=str(input('enter your updated nickname: '))
                contact=person(name,email,phone,nickname)
                self.contacts.append(contact)
                self.save()
                break
        else:
            self.notfound()
    def save(self):
        with open('contacts.csv','w') as f:
            writer=csv.writer(f)
            writer.writerow(('name','phone','email','nickname'))
            for contact in contacts:
                writer.writerow((contact.name,contact.phone,contact.email,contact.nickname))
    def printcontact(self,contact):
        print('---#---#---#---#---#---#--')
        print("number:{}".format(contact.name))
        print("phone number:{}".format(contact.phone))
        print("email:{}".format(contact.email))
        print("nickname:{}".format(contact.nickname))
        print('---#---#---#---#---#---#--')
    def notfound(self):
        print('no contact')
def run():
    cbook=contactbook()
    with open('contacts.csv','r')as f:
        reader=csv.reader(f)
        for idx,row in enumerate(reader):
            if idx==0:
                continue
            elif row==[]:
                continue
            else:
                cbook.addperson(row[0],row[1],row[2],roe[3])
    choice=0
    while choice!=6:
        choice=int(input('''
        1.create new contact
        2.deletate contact
        3.print contact
        4.update
        5.serch contact
        6.exit
        '''))
        if choice==1:
            name=str(input('enter your  name: '))
            phone=str(input('enter your  phone number: '))
            email=str(input('enter your  email: '))
            nickname=str(input('enter your  nickname: '))
            cbook.addperson(name,email,phone,nickname)
        elif choice==2:
            name=str(input('enter name to deleate: '))
            cbook.deletecon(name)
        elif choice==3:
            name=str(input('enter name to print: '))
            cbook.printcontact(name)
        elif choice==4:
            name=str(input('enter name to update: '))
            cbook.update(name)
        elif choice==5:
            name=str(input('enter name to search: '))
            cbook.search(name)
        else:
            print('exit')

if __name__=='__main__':
    run()
        




                