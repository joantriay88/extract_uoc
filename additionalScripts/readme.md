Additional Scripts
===================


These scripts have been created for process .JSON files from UCATx platform based on Open EDx.


----------

<i class="icon-cog"></i>convert_into_json.sh
-------------

This script convert a file from tracking logs into a .JSON file for been processed with python.
It adds a comma at the end of all lines except the last line and add "[" at the begining and "]" at final of the file.

> **How to use:**
```
./convert_into_json.sh fileName
```



<i class="icon-cog"></i>number_delete_line.sh
-------------

This script delete a line of a file.

> **How to use:**
```
./number_delete_line.sh fileName lineNumber
```
