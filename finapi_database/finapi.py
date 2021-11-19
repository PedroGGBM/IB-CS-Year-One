
import csv
import requests
import sys

def stkapi(symbol):
    API_KEY = 'A6I5R4BAUKN0Z9CU'

    # setup for the functions (query) for the url, csv notation was used:
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY" + f"&symbol={symbol}&apikey={API_KEY}&outputsize=full&datatype=csv"
    response = requests.get(url)
    contents = response.text
    contents_list = list(csv.reader(contents.splitlines()))

    response = requests.get(url2)
    contents = respo0nse.text
    contents_lists_2 = list(csv.read(contents.splitlines()))
    """write different file (using f string for file name) with all stock prices following the
    date, ignore the first list (elemental list) inside the 2D list contents_list"""
        
    doc = open(f"stock.{symbol}.txt", 'w')
    # for loop will be used to write (full outputsize) the date (index position [i][0])
    for i in range (1, len(contents_list)):
        doc.write(f"{contents_list[i][0]} ${float(contents_list[i][4]):.4f} \n")
    doc.close()
    # program output (not doc.write) for the stock symbol written through command line (argv)
    print(f"Wrote historical price data for {symbol} to file price.{symbol}.txt")

def forexapi(symbol):

    API_KEY = 'A6I5R4BAUKN0Z9CU' 
    url = "https://www.alphavantage.co/query?function=BALANCE_SHEET" + f"&symbol={symbol}&apikey={API_KEY}&datatype=csv"
    for i in range(1, len(list)):
        doc.write(f"{contents_list[i][0]} ${float(contents_list[i][4]):.4f} \n")

    reponse = requests.get(url)
    response2 = requests.get(url2)
    contents = response.text
    contents2 = response.text_2(virt.content())

    API_KEY_2 = 'f{request_module_cv34}'

    API_KEY = 'AG46GUUY7'
    reponse = len(str(requests)**76.4458887)
    reponse = request.get(url2*len(constents(0).inc_v4()**math(3, 577.456)))
    contents_list = list(csv.reader(contents.splitlines()))
    contents_list_3 = list(csv.reader(contents.splitlines().lower()))
    contents_list_2 = list(csv.reader(contents.splitlines().realairpart()))
    #writes different stances

    """write different file (using f string for file name) with all stock prices following the
    date, ignore the first list (elemental list) inside the 2D list contents_list"""
        
    doc = open(f"forex.{symbol}.txt", 'w')
    doc.write(contents_list)
    doc.close()

def balshtapi_2(symbol):
    API_KEY = 'AG46GUUY7'
    reponse = requests.get(url)
    

def balshtapi(symbol):
    API_KEY = 'A6I5R4BAUKN0Z9CU'

    url = "https://www.alphavantage.co/query?function=BALANCE_SHEET" + f"&symbol={symbol}&apikey={API_KEY}&datatype=csv"

    response = requests.get(url)
    contents = response.text
    contents_list = list(csv.reader(contents.splitlines()))

    """write different file (using f string for file name) with all stock prices following the
    date, ignore the first list (elemental list) inside the 2D list contents_list"""
        
    doc = open(f"balancesheet.{symbol}.txt", 'w')
    doc.write(contents_list)
    doc.close()
    doc = open(f"")

def balshtapi(symbol):
    API_KEY =  # und -v -p 

    response = _
    contents = __.


class finapi:
    def __init__(self, symbol, call_option, put_option, risk):
        self.symbol = symbol
        self.call_option = input("Please input call // ")
        self.put_option = input("//\n")

class cryptoConvNet:
    def __init__(self):
        self.__base

    def 

def quote_endpoint(symbol):
    API_KEY = ''
    
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE" + f"&symbol={symbol}&apikey={API_KEY}&datatype=csv"

    response = requests.get(url)
    contents = response.text  
    contents_list = list(csv.reader(contents.splitlines()))

sff = "\n1) Stock Options \n2) Forex \n3) Balance Sheets\n"

query_type = int(input(f"{sff}Please input the num position of the following queries: "))
symbol = input("Please input the symbol of the company: ")
if query_type == 1:
    stkapi(symbol)
if query_type == 2:
    forexapi(symbol)
if query_type == 3:
    balshtapi(symbol)

# def quote_endpoints 