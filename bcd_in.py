import streamlit as st
import os
import ast
from tempfile import NamedTemporaryFile

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator

from InvoiceGenerator.pdf import SimpleInvoice
import urllib


import base64

urllib.request.urlretrieve("https://lh3.googleusercontent.com/W5-2w5v3ET_0xh40zJUDkL2Gd7Ls66yh1-rs12UMW4EZPaEyofl_Ix_NrxeybNJ1LNnRZxw=s93", "logo.png")

#os.chdir(r'C:\Users\MOHAMMED MUZZAMMIL\Desktop\Invoice')

def ganjakhet():
    # choose english as language
    os.environ["INVOICE_LANG"] = "en"

    client = Client('Bombay Coldrinks')
    provider = Provider('Bombay Softdrinks Private Ltd', bank_account='2600420569', bank_code='2010',logo_filename='logo.png')
    creator = Creator('Bombay Softdrinks')

    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'as_IN.UTF-8'
    invoice.currency= u'₹'
    #invoice.format_currency(5433422.8012, 'INR', locale='en_IN')
    return invoice





def shantinagar():
    # choose english as language
    os.environ["INVOICE_LANG"] = "en"

    client = Client('New Bombay Coldrinks')
    provider = Provider('Bombay Softdrinks Private Ltd', bank_account='2600420569', bank_code='2010',logo_filename='logo.png')
    creator = Creator('Bombay Softdrinks')

    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'as_IN.UTF-8'
    invoice.currency= u'₹'
    #invoice.currency_locale = 'en_US.UTF-1'
    #format_currency(5433422.8012, 'INR', locale='en_IN')
    return invoice






def mominpura():
    # choose english as language
    os.environ["INVOICE_LANG"] = "en"

    client = Client('Farheen Hotel')
    provider = Provider('Bombay Softdrinks Private Ltd', bank_account='2600420569', bank_code='2010',logo_filename='logo.png')
    creator = Creator('Bombay Softdrinks')

    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'as_IN.UTF-8'
    invoice.currency= u'₹'
    #invoice.currency_locale = 'en_US.UTF-1'
    #format_currency(5433422.8012, 'INR', locale='en_IN')
    return invoice


def hasanbagh():
    # choose english as language
    os.environ["INVOICE_LANG"] = "en"

    client = Client('Bombay Coldrinks Hasanbagh')
    provider = Provider('Bombay Softdrinks Private Ltd', bank_account='2600420569', bank_code='2010',logo_filename='logo.png')
    creator = Creator('Bombay Softdrinks')

    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'as_IN.UTF-8'
    invoice.currency= u'₹'
    #invoice.currency_locale = 'en_US.UTF-1'
    #format_currency(5433422.8012, 'INR', locale='en_IN')
    return invoice


def jafarnagar():
    # choose english as language
    os.environ["INVOICE_LANG"] = "en"

    client = Client('Bombay Coldrinks Jafarnagar')
    provider = Provider('Bombay Softdrinks Private Ltd', bank_account='2600420569', bank_code='2010',logo_filename='logo.png')
    creator = Creator('Bombay Softdrinks')

    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'as_IN.UTF-8'
    invoice.currency= u'₹'
    #invoice.currency_locale = 'en_US.UTF-1'
    #format_currency(5433422.8012, 'INR', locale='en_IN')
    return invoice


def sadar():
    # choose english as language
    os.environ["INVOICE_LANG"] = "en"

    client = Client('Cupz N Conez')
    provider = Provider('Bombay Softdrinks Private Ltd', bank_account='2600420569', bank_code='2010',logo_filename='logo.png')
    creator = Creator('Bombay Softdrinks')

    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'as_IN.UTF-8'
    invoice.currency= u'₹'
    #invoice.currency_locale = 'en_US.UTF-1'
    #format_currency(5433422.8012, 'INR', locale='en_IN')
    return invoice




def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href


st.markdown("<h1 style='text-align: center; color: Light gray;'>Bombay Softdrinks Private Ltd</h1>", unsafe_allow_html=True)

title,qt,br=st.beta_columns([4,1,1])


with title:
    flavours=('Orange 600 ml','Orange 300 ml','Rooh afza 600 ml','Rooh afza 300 ml','Awla Zeera 600 ml'
              ,'Awla Zeera 300 ml','Pudina 600 ml','Pudina 300 ml',
              'Fresh Lime 600 ml','Fresh Lime 300 ml','Ice Cream 600 ml'
              ,'Ice Cream 300 ml','Soda 600 ml','Soda 300 ml','Kashmiri Soda 600 ml','Kashmiri Soda 300 ml','Old-Crates-600-ml',
             'Old-Crates-300-ml')
    fl=st.selectbox('Choose',flavours)

    
with qt:
    options=(1,2,3,4,5,6,7,8,9,10)
    qut=st.selectbox('Quantity',options)
    
    
with br:
    br_options=('----','Ganjakhet','Shantinagar','Mominpura','Sadar','Jafar Nagar','Hasanbagh')
    branch=st.selectbox('Branch',br_options)
    

if st.button('Add Item'):
    le={}
    le={fl:qut}
    try: 
        geeky_file = open('geekyfile.txt', 'a') 
        geeky_file.write(str(le)) 
        geeky_file.write('\n')
        geeky_file.close() 

    except: 
        print("Unable to append to file")
              
        
def parse(d): 
	dictionary = dict() 
	# Removes curly braces and splits the pairs into a list 
	pairs = d.strip('{}').split(', ') 
	for i in pairs: 
		pair = i.split(': ') 
		# Other symbols from the key-value pair should be stripped. 
		dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"') 
	return dictionary 



def ga_bill(invoice,dictionary):
    for i,j in dictionary.items():
        if i == 'Orange 600 ml':
            invoice.add_item(Item(j, 290, description=i))
        elif i == 'Rooh afza 600 ml':
            invoice.add_item(Item(j, 370, description=i))
        elif i == 'Pudina 600 ml':
            invoice.add_item(Item(j, 310, description=i))
        elif i == 'Awla Zeera 600 ml':
            invoice.add_item(Item(j, 310, description=i))
        elif i == 'Fresh Lime 600 ml':
            invoice.add_item(Item(j, 290, description=i))
        elif i == 'Ice Cream 600 ml':
            invoice.add_item(Item(j, 290, description=i))
        elif i == 'Orange 300 ml':
            invoice.add_item(Item(j, 206, description=i))
        elif i== 'Rooh afza 300 ml':
            invoice.add_item(Item(j, 231, description=i))
        elif i == 'Awla Zeera 300 ml':
            invoice.add_item(Item(j, 221, description=i))
        elif i == 'Pudina 300 ml':
            invoice.add_item(Item(j, 221, description=i))
        elif i == 'Fresh Lime 300 ml':
            invoice.add_item(Item(j, 206, description=i))
        elif i == 'Ice Cream 300 ml':
            invoice.add_item(Item(j, 206, description=i))
        elif i == 'Soda 600 ml':
            invoice.add_item(Item(j, 230, description=i))
        elif i == 'Soda 300 ml':
            invoice.add_item(Item(j, 171, description=i))
        elif i == 'Old-Crates-600-ml':
            invoice.add_item(Item(j,-150, description=i))    
        elif i == 'Old-Crates-300-ml':
            invoice.add_item(Item(j,-104, description=i))
            

            
    return
    
    



def c_bill(invoice,dictionary):
    for i,j in dictionary.items():
        if i == 'Orange 600 ml':
            invoice.add_item(Item(j, 390, description=i))
        elif i == 'Rooh afza 600 ml':
            invoice.add_item(Item(j, 480, description=i))
        elif i == 'Pudina 600 ml':
            invoice.add_item(Item(j, 730, description=i))
        elif i == 'Awla Zeera 600 ml':
            invoice.add_item(Item(j, 730, description=i))
        elif i == 'Kashmiri Soda 600 ml':
            invoice.add_item(Item(j, 730, description=i))
        elif i == 'Fresh Lime 600 ml':
            invoice.add_item(Item(j, 480, description=i))
        elif i == 'Ice Cream 600 ml':
            invoice.add_item(Item(j, 390, description=i))
        elif i == 'Orange 300 ml':
            invoice.add_item(Item(j, 240, description=i))
        elif i== 'Rooh afza 300 ml':
            invoice.add_item(Item(j, 285, description=i))
        elif i == 'Awla Zeera 300 ml':
            invoice.add_item(Item(j, 410, description=i))
        elif i == 'Pudina 300 ml':
            invoice.add_item(Item(j, 410, description=i))
        elif i == 'Fresh Lime 300 ml':
            invoice.add_item(Item(j, 285, description=i))
        elif i == 'Ice Cream 300 ml':
            invoice.add_item(Item(j, 240, description=i))
        elif i == 'Kashmiri Soda 300 ml':
            invoice.add_item(Item(j, 410, description=i))
        elif i == 'Old-Crates-600-ml':
            invoice.add_item(Item(j,-120, description=i))    
        elif i == 'Old-Crates-300-ml':
            invoice.add_item(Item(j,-96, description=i))
                
                
    return
            
    
    




        
if st.button('Create'):
    geeky_file = open('geekyfile.txt', 'rt') 
    dictionary = dict()
    lines = geeky_file.read().split('\n') 
    for l in lines: 
        if l != '': 
            dictionary.update(parse(l))
            geeky_file.close()  
    
    #format_currency(5433422.8012, 'INR', locale='en_IN')
    if branch == 'Ganjakhet':
        invoice=ganjakhet()
        ga_bill(invoice,dictionary)
    
    elif branch == 'Shantinagar':
        invoice=shantinagar()
        ga_bill(invoice,dictionary)
        
    elif branch == 'Mominpura':
        invoice=mominpura()
        c_bill(invoice,dictionary)
        
    elif branch == 'Sadar':
        invoice=sadar()
        c_bill(invoice,dictionary)
        
    elif branch ==  'Hasanbagh':
        invoice=hasanbagh()
        c_bill(invoice,dictionary)
        
    elif branch == 'Jafar Nagar':
        invoice=jafarnagar()
        c_bill(invoice,dictionary)
                    
            
            
    file = open("geekyfile.txt","r+")
    file. truncate(0)
    file. close()
    pdf = SimpleInvoice(invoice)
    pdf.gen("invoice.pdf", generate_qr_code=False)
    
    
    st.markdown(get_binary_file_downloader_html('invoice.pdf', 'Bill'), unsafe_allow_html=True)
    
    
    #b64 = base64.b64encode(
     #   file.encode()
    #).decode()
    
        
            
            
            
    
    

   

    #pdf = SimpleInvoice(invoice)
    #pdf.gen("invoice.pdf", generate_qr_code=False)



