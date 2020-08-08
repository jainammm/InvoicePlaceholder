from fastapi import FastAPI, Request
from fastapi.responses import Response
import xlsxwriter
import os

from io import BytesIO

app = FastAPI()

@app.get("/getXLSX")
async def root(request: Request):
    request_body = await request.json()
    print(request_body['model_output'])

    workbook = xlsxwriter.Workbook(os.path.join('results', 'response.xlsx'))
    
    # The workbook object is then used to add new  
    # worksheet via the add_worksheet() method. 
    worksheet = workbook.add_worksheet() 
    
    # Use the worksheet object to write 
    # data via the write() method. 
    worksheet.write('A1', 'Hello..') 
    worksheet.write('B1', 'Geeks') 
    worksheet.write('C1', 'For') 
    worksheet.write('D1', 'Geeks')

    workbook.close()

    with open(os.path.join('results', 'response.xlsx'), 'rb') as f:
        xlsx_file = f.read()
    

    return Response(content=xlsx_file, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')