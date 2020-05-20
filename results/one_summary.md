
# Report Suite number 001
> A longer description of the incredible suite number 001

* Total Tests: 5
* Passed Tests: 2
* Failed Tests: 3
* Percentage: **40.0%**  :green_square::green_square::red_square::red_square::red_square:

**Final Check**
| Check | Filled Check | Result |
| ------------ | --------- | ----- |
| '{{2.json.name}}' == 'Leanne Graham' | 'Leanne Graham' == 'Leanne Graham' | :heavy_check_mark: | 
| {{2.json.id}} == {{1.json.userId}} | 1 == 1 | :heavy_check_mark: | 
| '{{3.json.title}}' == 'A Test' | '0' == 'A Test' | :x: | 
| {{3.json.userId}} == {{1.json.userId}} == {{2.json.id}} | 0 == 1 == 1 | :x: | 
| {{3.json.id}} == 101 | 0 == 101 | :x: | 
