## KSM Customer Importer
This script reads the file `customers.csv` that containis a list of customer information
in the following format:
```
Customer Id,Exclude From Usage Gathering,Exclude From Usage Gathering Invoice Creation
169ljHTOoHgms27x9,FALSE,FALSE
AzqYQ9T1hfUAG9Oe,TRUE,TRUE
169liHT121g4v18Nn,FALSE,FALSE
```

The script requires two arguments:
1. The KSM base url: `https://subscription-management-service.intg.keapapis.com`
2. The KSM api key: `AIzaSyDOqUVm.....................`

```
python process.py https//subscription-management-service.intg.keapapis.com AIzaSyDOqUVmGsMf9O...................
```

There are 3 files:
1. `customers.csv` - see format above.
2. `success.txt` - customers that were successfully imported.
3. `failures.txt` - customers that were NOT imported correctly.