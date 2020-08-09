# InvoicePlaceholder

## Overview

## How to run
```
pip install -r requirements.txt
```

* Start server using `uvicorn app:app --port=8001`
* The api is exposed at http://localhost:8001/getXLSX

> Run using docker
* Build doker image using `docker build -t invoiceplaceholder .`
* Run using `docker run -it --rm -p 8001:8001 invoiceplaceholder:latest`
* The api is exposed at http://localhost:8001/getXLSX