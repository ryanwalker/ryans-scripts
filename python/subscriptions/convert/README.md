## Usage
This script reads a CSV file containing a list of tenantIds that need to be converted to subscription Ids. 
A subscription is retrieved from KSM by tenant, and the subscription id is written to a file.

The script is expecting two arguments:
1. The KSM environment: intg, stge or prod
2. The api key, tenantApiKey

```
python convert-tenant-to-subId.py intg tA*****G7v
```

There are 3 files:
1. convert.txt - contains a newline separated list of tenants to convert to subscription ids
2. converted.txt - after executing the script it will contain the retrieved subscription ids.
3. errors.txt - any errors that occurred while the script was executing