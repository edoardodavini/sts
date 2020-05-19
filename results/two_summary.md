
# API Report results
    
* Total Tests: 18
* Passed Tests: 16
* Failed Tests: 2
* Percentage: 88.89%
    
| Check | Filled Check | Test Result |
| ------------ | --------- | ----- |
| '{{1.json.username}}' == 'marco' | 'marco' == 'marco' | &#x2714; | 
| {{2.status}} == 200 | 201 == 200 | &#x2716; | 
| {{2.status}} == 201 | 201 == 201 | &#x2714; | 
| 200 <= {{2.status}} <= 300 | 200 <= 201 <= 300 | &#x2714; | 
| {{3.json}} == {{2.json}} | {'email': 'another@utente.it', 'id': 17, 'name': 'uno', 'surname': 'utente', 'username': 'another'} == {'email': 'another@utente.it', 'id': 17, 'name': 'uno', 'surname': 'utente', 'username': 'another'} | &#x2714; | 
| '{{3.json.username}}' == '{{2.json.username}}' | 'another' == 'another' | &#x2714; | 
| '{{3.json.surname}}' == '{{2.json.surname}}' | 'utente' == 'utente' | &#x2714; | 
| {{4.status}} == 200 | 200 == 200 | &#x2714; | 
| 200 <= {{4.status}} <= 300 | 200 <= 200 <= 300 | &#x2714; | 
| '{{4.json.surname}}' != '{{3.json.surname}}' | 'crazy surname' != 'utente' | &#x2714; | 
| '{{3.json.name}}' != '{{4.json.name}}' | 'uno' != 'due' | &#x2714; | 
| '{{4.json.surname}}' == 'crazy surname' | 'crazy surname' == 'crazy surname' | &#x2714; | 
| {{5.status}} == 200 | 200 == 200 | &#x2714; | 
| '{{5.json.surname}}' == 'crazy surname' | 'crazy surname' == 'crazy surname' | &#x2714; | 
| '{{5.json.name}}' == '{{4.json.name}}' | 'due' == 'due' | &#x2714; | 
| '{{5.json.name}}' != '{{3.json.name}}' | 'due' != 'uno' | &#x2714; | 
| {{6.status}} == 200 | 200 == 200 | &#x2714; | 
| {{7.status}} == 404 | 500 == 404 | &#x2716; | 
