class Customer:
    def __init__(self,name, address):
        self.name = name
        self.address = address

    @property
    def get_name(self):
        return self.name.title()
    
    @property
    def get_address(self):
        return self.address
    
    def __repr__(self):
        return 'CUSTOMER INFORMATION \nName: %s \nAddress %s\n'%(self.get_name,self.get_address)


# Main program
Edube = Customer('edube','P.O.Box 245 upper Kawuga')
Oscar = Customer('Oscar','P.O.Box 226 lower Kawuga')
Customer_list = [Edube, Oscar]
print(Customer_list)