
# Report Demo suite 003
> A simple demo test with Mocked data

* Total Tests: 8
* Passed Tests: 5
* Failed Tests: 3
* Percentage: **62.5%**  :green_square::green_square::green_square::green_square::green_square::red_square::red_square::red_square:

**Final Check**
> Final Check

| Check | Filled Check | Result |
| ------------ | --------- | ----- |
| len({{0.json}}) == 8 | len([{'email': 'pippo@baudo.it', 'id': 1, 'name': 'pippo', 'surname': 'baudo', 'username': 'mannaggia'}, {'email': 'marco@bartali.it', 'id': 2, 'name': 'marco', 'surname': 'bartali', 'username': 'marco'}, {'email': 'gino@bartali.it', 'id': 3, 'name': 'gino', 'surname': 'bartali', 'username': 'gino'}, {'email': 'gino@barta.it', 'id': 4, 'name': 'ginuccia', 'surname': 'bartalosa', 'username': 'ginella'}, {'email': 'another@utente.it', 'id': 5, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 6, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 7, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 8, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 9, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 10, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 11, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 12, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 13, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 14, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 15, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 16, 'name': 'uno', 'surname': 'utente', 'username': 'another'}]) == 8 | :x: | 
| {{0.status}} == 200 | 200 == 200 | :heavy_check_mark: | 
| '{{1.json.username}}' == 'marco' | 'marco' == 'marco' | :heavy_check_mark: | 
| {{1.status}} == 200 | 200 == 200 | :heavy_check_mark: | 


**Check with mocked data**
> Check with mocked data

| Check | Filled Check | Result |
| ------------ | --------- | ----- |
| '{{3.json.email}}' == 'pippo@baudo.it' | 'pippo@baudo.it' == 'pippo@baudo.it' | :heavy_check_mark: | 
| '{{3.json.email}}' == '{{4.json.email}}' | 'pippo@baudo.it' == 'pippo@baudo.it' | :heavy_check_mark: | 
| '{{3.json.username}}' == '{{4.json.username}}' | 'mannaggia' == 'marco' | :x: | 
| '{{3.json.username}}' == '{{1.json.username}}' | 'mannaggia' == 'marco' | :x: | 
