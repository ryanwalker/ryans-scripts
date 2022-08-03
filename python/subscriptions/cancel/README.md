## Usage
This script reads a CSV file containing a list of subscription ids that need to be cancelled in chargebee.
The chargebee python lib is used to call chargebee.

The script is expecting two arguments:
1. The Chargebee hostname: keapint-test, keapnew-test or keapnew
2. The chargebee api key

```
python cancel-sub.py keapint-test test_55z***************wcu
```

There are 3 files:
1. to-cancel.txt - contains a newline separated list of subscription ids that need to be cancelled.
2. cancelled.txt - a list of subscription ids that have successfully been cancelled.
3. errors.txt - a list of any subscription ids that failed to cancel.