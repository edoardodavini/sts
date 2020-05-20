# STS: Simple Test Suite (or TAK: Test API Kit) 

Full API Integration tests made easy

* [The concept](#the-concept)
* [Test it right away](#test-it-right-away)
* [How it works](#how-it-works)
+ [The main object](#the-main-object)
+ [The Steps](#the-steps)
  - [The Request](#the-request)
  - [The Check](#the-check)
* [Placeholders](#placeholders)
* [Full Example for reference](#full-example-for-reference)


## The concept

Testing an API is pretty easy and straightforward:  
`curl google.com`, get the response and `assert(true)`

But what if you want to test the entire `REST` resource?  
What if you want to test the `POST`, `PATCH` and `DELETE` in a specified order, 
checking that every step is doing what you would expect?  
And what if you want these steps to be completely described by a **single file**?  
And what if you want those files to be placed in a *Repository* and maintained easily?

## Test it now!

1. Clone this repo: `git clone https://github.com/edavini/sts.git`
2. Navigate into the newly created folder: `cd sts`
3. Run the *local server* (OPTIONAL: for testing purpose only):
    1. Install `flask` dependency: `pip install flask`
    2. Run the `flask` server: `python test_server/app.py`
    3. If you don't want to execute this step, just delete the `two.json` suite in the `suite` folder
4. Run the *suites tester* (in a different shell/prompt): `python suite.py`

You should get a lot of test executed. Seeing both requests, responses and the checks being done
You'll be able to find the report generated in the `results` folder


## How it works

This is a small example of standardized `json-like` format

### The main object

The main object is the **Suite** definition, with just a _name_ and a _description_  
Contains an array of [Steps](#the-steps)

| Property | Description | Valid Values |
|----------|-------------|--------------|
| `name`   | The name of the suite | A `string` |
| `description` | The description of the suite | A `string` |
| `steps` | The steps of the suite | An array of [Steps](#the-steps) |

Example of Suite
```json
{
  "name": "Suite number 001",
  "description": "A longer description of the incredible suite number 001",
  "steps": []
}
```

### The Steps

This is the _core_ object of the entire process.  
For each suites there are a number of steps which are executed in the given order.  
These steps can be an `HTTP` call (classic API call) or an `ASSERT` check.

Each step response (both coming from a [Request](#the-request) or from an array of [Checks](#the-check)) is placed in an array of objects, 
available for reference during the whole process of testing.
See 

| Property | Description | Valid Values |
|----------|-------------|--------------|
| `type`   | The type of the step | `HTTP` or `ASSERT` |
| `name`   | The name of the step | A `string` |
| `description` | The description of the step | A `string` |
| `request` | Only for `HTTP` steps: the request to be sent | A [Request](#the-request) |
| `checks` | Only for `ASSERT` steps: the checks to be made | An array of [Checks](#the-check) |

An `HTTP` example
```json
    {
      "type": "HTTP",
      "name": "Get Comment",
      "description": "Get Comment with Id: 1",
      "request": {
        "url": "https://jsonplaceholder.typicode.com/comments/1",
        "method": "GET",
        "data": null
      }
    }
```

An `ASSERT` example
```json
    {
      "type": "ASSERT",
      "name": "Final Check",
      "description": "Check a bunch of stuff",
      "checks": [
        "'{{2.json.name}}' == 'Leanne Graham'",
        "{{2.json.id}} == {{1.json.userId}}",
        "{{3.json.title}} == 'A Test'"
      ]
    }
```

#### The Request

Every `http` request is made using a simple description of what it needs.

| Property | Description | Valid Values |
|----------|-------------|--------------|
| `url`   | The url to be called, placeholder availables | A `string` with placeholders |
| `method`   | The HTTP Method | A Valid HTTP Method (`string`) |
| `data` | The body of the HTTP call. As a string, with backslashes before double quotes | A `string` with placeholders |

A Request Example: a GET without placeholders
```json
{
    "url": "https://jsonplaceholder.typicode.com/comments/1",
    "method": "GET",
    "data": null
}
```
A Request Example: a POST with a 2 placeholders in the body (data)
```json
{
    "url": "https://jsonplaceholder.typicode.com/posts/",
    "method": "POST",
    "data": "{\"title\": \"A Test\", \"body\": \"A body created by {{1.json.userId}}\", \"userId\": {{1.json.userId}}}"
}
```

##### The request's Response

| Property | Description | Example |
|----------|-------------|--------------|
| `type`   | Used for distinguish the `http` from the `check` | `HTTP` |
| `headers`   | JSON-like headers | `{"Content-Type": "application/json", [...]}` |
| `data` | The body of the response, raw as text string | `{\"email\": \"another@utente.it\"}` |
| `status` | The HTTP status: integer | `200` |
| `request` | The Request made for this response. `body`, `headers`, `method` and `url` available  | `{"body": {}, "headers": {}, "method": "", "url": "` |
| `json` | The body of the response as a json, if possible | `{ "email": "another@utente.it" }` |

Full Example: 
```json
{
    "type": "HTTP",
    "headers": {
        "Content-Type": "application/json",
        "Content-Length": "116"
    },
    "body": "{\n  \"email\": \"another@utente.it\", \n  \"id\": 17, \n  \"name\": \"uno\", \n  \"surname\": \"utente\", \n  \"username\": \"another\"\n}\n",
    "status": 201,
    "request": {
        "body": {
            "username": "another",
            "name": "uno",
            "surname": "utente",
            "email": "another@utente.it"
        },
        "headers": {
            "User-Agent": "python-requests/2.22.0",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Content-Length": "89",
            "Content-Type": "application/json"
        },
        "method": "POST",
        "url": "http://localhost:5000/users"
    },
    "json": {
        "email": "another@utente.it",
        "id": 17,
        "name": "uno",
        "surname": "utente",
        "username": "another"
    }

}
```

#### The Check
Checks are just an array of `string` like  
`"'{{2.name}}' == 'Leanne Graham'"`  
with full placeholders usage.
The check is made using python `eval`, so it accepts a huge lot of tests in one single shot.

Those functions are the one tested right now:
* use directly a `string` as a comparison: `'{{1.json.username}}' == 'marco'`
* use directly a `number` (both a `float` or an `int`): `{{2.status}} == 200`
* use `between`: `200 <= {{2.status}} <= 300`
* checks different object at once: `{{3.json}} == {{2.json}}`
* use `!=`: `{{4.json.surname}}' != '{{3.json.surname}}`
* multiple conditions at once, using `and`, `or`: `{{4.json.surname}}' != '{{3.json.surname}} or {{4.json.surname}}' == '{{3.json.surname}}`


## Placeholders
Placeholders are as easy as possible:  
`{{x.this.is.a.nested.path}}`
* The double brackets are used to identify inside a string. 
* `x` is always an integer, representing the array index of the responses (so it starts from 0)
* `this.is.a.nested.path` is the nested path of the object of the response. 

## The results
This process generates 2 different reports: 
* a `raw_report` available as a `json` with all the information gathered during the test execution
* a `summary` available as a `markdown` with a small summary of how well the test went

An example of a Summary Report is available [here](results/two_summary.md)

## To be done / next steps
* Add support for headers in the request object
* Add support for login-interceptors
* Add documentation for Placeholder
* Better error handling
* Add MOCK step type, for mocked data just to be verified in the next steps
* Test more checks, like usage of functions, including filters and map
* more stuff

## Full Example for reference

Check updated references in the [Suites](blob/master/suites/) directory

## Contribute

Feel free to join this project. This was born to meet the need of a pre-defined tests suite.