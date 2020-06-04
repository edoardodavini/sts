
# Report Demo Suite number 002
> A nice description for the Demo Suite. This uses more advanced tests and checks. Needs localhost server

* Total Tests: 22
* Passed Tests: 16
* Failed Tests: 6
* Percentage: **72.73%**  :green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::red_square::red_square::red_square::red_square::red_square::red_square:

**First assertion check**
> First assertion check

| Check | Filled Check | Result |
| ------------ | --------- | ----- |
| '{{1.json.username}}' == 'marco' | 'marco' == 'marco' | :heavy_check_mark: | 
| {{2.status}} == 201 | 201 == 201 | :heavy_check_mark: | 
| 200 <= {{2.status}} <= 300 | 200 <= 201 <= 300 | :heavy_check_mark: | 
| {{3.json}} == {{2.json}} | {'email': 'another@utente.it', 'id': 17, 'name': 'uno', 'surname': 'utente', 'username': 'another'} == {'email': 'another@utente.it', 'id': 17, 'name': 'uno', 'surname': 'utente', 'username': 'another'} | :heavy_check_mark: | 
| '{{3.json.username}}' == '{{2.json.username}}' | 'another' == 'another' | :heavy_check_mark: | 
| '{{3.json.surname}}' == '{{2.json.surname}}' | 'utente' == 'utente' | :heavy_check_mark: | 
| {{4.status}} == 200 | 200 == 200 | :heavy_check_mark: | 
| 200 <= {{4.status}} <= 300 | 200 <= 200 <= 300 | :heavy_check_mark: | 
| '{{4.json.surname}}' != '{{3.json.surname}}' | 'crazy surname' != 'utente' | :heavy_check_mark: | 
| '{{3.json.name}}' != '{{4.json.name}}' | 'uno' != 'due' | :heavy_check_mark: | 
| '{{4.json.surname}}' == 'crazy surname' | 'crazy surname' == 'crazy surname' | :heavy_check_mark: | 
| {{5.status}} == 200 | 200 == 200 | :heavy_check_mark: | 
| '{{5.json.surname}}' == 'crazy surname' | 'crazy surname' == 'crazy surname' | :heavy_check_mark: | 
| '{{5.json.name}}' == '{{4.json.name}}' | 'due' == 'due' | :heavy_check_mark: | 
| '{{5.json.name}}' != '{{3.json.name}}' | 'due' != 'uno' | :heavy_check_mark: | 
| {{6.status}} == 200 | 200 == 200 | :heavy_check_mark: | 
| {{7.status}} == 404 | 500 == 404 | :x: | 


**Second check**
> Second check

| Check | Filled Check | Result |
| ------------ | --------- | ----- |
| {{2.status}} == 'PIZZA!' | 201 == 'PIZZA!' | :x: | 
| '{{5.json.surname}}' == 'this is going to fail miserably' | 'crazy surname' == 'this is going to fail miserably' | :x: | 
| True == False | True == False | :x: | 
| len('{{5.json.name}}') == 7 | len('due') == 7 | :x: | 
| {{7.status}} == 404 | 500 == 404 | :x: | 
