*Python3 is needed for this*
*Use version 3.12.3 for better compatibility*

Run the following command to install all requirements:
```
 pip install -r requirements.txt
```



*filter_test.py*
 ```
 python3 filter_test.py
```
 - this uses chromedriver, download chromedriver or use your preferred webdriver
 - change the path of Service to the path of your webdriver and change accordingly
 - to test other category, change the category variable (CASE SenSiTiVE)
 - other filter dropdowns can be tested using click_filter_button(filter_name) method



*compare_csvs.py*
 ```
python3 compare_csvs.py file1.csv file2.csv order_date
```
 - compare_csvs.py and both csvs to compare must be in the same folder
