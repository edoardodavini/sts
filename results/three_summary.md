
# Report Demo suite 003
> A simple demo test with Mocked data

* Total Tests: 4
* Passed Tests: 3
* Failed Tests: 1
* Percentage: **75.0%**  :green_square::green_square::green_square::red_square:

**Final Check**
> Final Check

| Check | Filled Check | Result |
| ------------ | --------- | ----- |
| len({{0.json}}) == 8 | len([{'email': 'pippo@baudo.it', 'id': 1, 'name': 'pippo', 'surname': 'baudo', 'username': 'mannaggia'}, {'email': 'marco@bartali.it', 'id': 2, 'name': 'marco', 'surname': 'bartali', 'username': 'marco'}, {'email': 'gino@bartali.it', 'id': 3, 'name': 'gino', 'surname': 'bartali', 'username': 'gino'}, {'email': 'gino@barta.it', 'id': 4, 'name': 'ginuccia', 'surname': 'bartalosa', 'username': 'ginella'}, {'email': 'another@utente.it', 'id': 5, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 6, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 7, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 8, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 9, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 10, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 11, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 12, 'name': 'uno', 'surname': 'utente', 'username': 'another'}, {'email': 'another@utente.it', 'id': 13, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 14, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 15, 'name': 'due', 'surname': 'utentazzo', 'username': 'another'}, {'email': 'another@utente.it', 'id': 16, 'name': 'uno', 'surname': 'utente', 'username': 'another'}]) == 8 | :x: | 
| {{0.status}} == 200 | 200 == 200 | :heavy_check_mark: | 
| '{{1.json.username}}' == 'marco' | 'marco' == 'marco' | :heavy_check_mark: | 
| {{1.status}} == 200 | 200 == 200 | :heavy_check_mark: | 
