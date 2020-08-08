from fastapi import FastAPI, Request
from fastapi.responses import Response
import xlsxwriter
import os
import re

# For checking if the word is real english word
import enchant


from io import BytesIO
from utils import getMaxConfidence, getAddress

app = FastAPI()


@app.get("/getXLSX")
async def root(request: Request):
    request_body = await request.json()

    model_output = request_body['model_output']
    print(model_output)

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

    en_dictionary = enchant.Dict("en_US")

    _, final_seller_state = getMaxConfidence(model_output, 'SELLER_STATE')
    print("SELLER_STATE:", final_seller_state)

    _, final_seller_id = getMaxConfidence(model_output, 'SELLER_ID')
    final_seller_id = re.sub(r'[^\w]', '', final_seller_id)
    if(en_dictionary.check(final_seller_id)):
        final_seller_id = ''
    print("SELLER_ID:", final_seller_id)

    _, final_seller_name = getMaxConfidence(model_output, 'SELLER_NAME')
    print("SELLER_NAME:", final_seller_name)

    _, final_seller_gstin_number = getMaxConfidence(model_output, 'SELLER_GSTIN_NUMBER')
    final_seller_gstin_number = final_seller_gstin_number.replace('GSTIN', '')
    final_seller_gstin_number = final_seller_gstin_number.replace('gstin', '')
    final_seller_gstin_number = re.sub(r'[^\w]', '', final_seller_gstin_number)
    if(en_dictionary.check(final_seller_gstin_number)):
        final_seller_gstin_number = ''
    print("SELLER_GSTIN_NUMBER:", final_seller_gstin_number)

    _, final_country_of_origin = getMaxConfidence(model_output, 'COUNTRY_OF_ORIGIN')
    print("COUNTRY_OF_ORIGIN:", final_country_of_origin)

    _, final_currency = getMaxConfidence(model_output, 'CURRENCY')
    print("CURRENCY:", final_currency)

    _, final_invoice_number = getMaxConfidence(model_output, 'INVOICE_NUMBER')
    print("INVOICE_NUMBER:", final_invoice_number)

    _, final_invoice_date = getMaxConfidence(model_output, 'INVOICE_DATE')
    print("INVOICE_DATE:", final_invoice_date)

    _, final_due_date = getMaxConfidence(model_output, 'DUE_DATE')
    print("DUE_DATE:", final_due_date)

    _, final_po_number = getMaxConfidence(model_output, 'PO_NUMBER')
    print("PO_NUMBER:", final_po_number)

    _, final_buyer_gstin_number = getMaxConfidence(model_output, 'BUYER_GSTIN_NUMBER')
    final_buyer_gstin_number = final_buyer_gstin_number.replace('GSTIN', '')
    final_buyer_gstin_number = final_buyer_gstin_number.replace('gstin', '')
    final_buyer_gstin_number = re.sub(r'[^\w]', '', final_buyer_gstin_number)
    if(en_dictionary.check(final_buyer_gstin_number)):
        final_buyer_gstin_number = ''
    print("BUYER_GSTIN_NUMBER:", final_buyer_gstin_number)

    print("***************")

    final_seller_address = getAddress(model_output, 'SELLER_ADDRESS')
    print('SELLER_ADDRESS:', final_seller_address)

    final_ship_to_address = getAddress(model_output, 'SHIP_TO_ADDRESS')
    print('SHIP_TO_ADDRESS:', final_ship_to_address)

    workbook.close()

    with open(os.path.join('results', 'response.xlsx'), 'rb') as f:
        xlsx_file = f.read()

    return Response(content=xlsx_file,
                    media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
