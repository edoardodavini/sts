# STS: Simple Test Suite

### The concept
It's easier to test single APIs or single functions (unit tests) but what about **BBEA**: *big bad evil application*?

The main concept is to create a `json-like` standard for testing sequences of tests. Suites.

A Developer should be able to write just a bunch of `requests` and expected `responses` and then let the machine do the tests for him/her.


### How it works.
This is a small example of standardized `json-like` format

#### The main object

| Property | Description | Valid Values |
|----------|-------------|--------------|
| `name`   | The name of the suite | A `string` |
| `description` | The description of the suite | A `string` |
| `steps` | The steps of the suite | An array of `step` |

Example of Suite
```json
{
  "name": "Suite number 001",
  "description": "A longer description of the incredible suite number 001",
  "steps": []
}
```

#### The Steps
| Property | Description | Valid Values |
|----------|-------------|--------------|
| `type`   | The type of the step | `HTTP` or `ASSERT` |
| `name`   | The name of the step | A `string` |
| `description` | The description of the step | A `string` |
| `request` | Only for `HTTP` steps: the request to be sent | A `request` |
| `checks` | Only for `ASSERT` steps: the checks to be made | An array of `check` |

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
        "'{{2.name}}' == 'Leanne Graham'",
        "{{2.id}} == {{1.userId}}",
        "{{3.title}} == 'A Test'"
      ]
    }
```

#### The Request
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
    "data": "{\"title\": \"A Test\", \"body\": \"A body created by {{1.userId}}\", \"userId\": {{1.userId}}}"
}
```

#### The Check
Checks are just an array of `string` like  
`"'{{2.name}}' == 'Leanne Graham'"`  
with full placeholders usage.
The check is valid only if:
 * compares only 2 things at a time (a == b)
 * the comparison is made using:
    * `==`: equal
    * `<=`: less than equal
    * `>=`: greater than equal
    * `<`: less than
    * `>`: greater than
    * `!=`: different


### Full Example for reference

```json
{
  "name": "Suite number 001",
  "description": "A longer description of the incredible suite number 001",
  "steps": [
    {
      "type": "HTTP",
      "name": "Get Comment",
      "description": "Get Comment with Id: 1",
      "request": {
        "url": "https://jsonplaceholder.typicode.com/comments/1",
        "method": "GET",
        "data": null
      }
    },
    {
      "type": "HTTP",
      "name": "Get Post",
      "description": "Get the post of the previous comment",
      "request": {
        "url": "https://jsonplaceholder.typicode.com/posts/{{0.postId}}",
        "method": "GET",
        "data": null
      }
    },
    {
      "type": "HTTP",
      "name": "Get User",
      "description": "Get the user that made the previous post",
      "request": {
        "url": "https://jsonplaceholder.typicode.com/users/{{1.userId}}",
        "method": "GET",
        "data": null
      }
    },
    {
      "type": "HTTP",
      "name": "Add a Post",
      "description": "Add a post just for fun",
      "request": {
        "url": "https://jsonplaceholder.typicode.com/posts/",
        "method": "POST",
        "data": "{\"title\": \"A Test\", \"body\": \"A body created by {{1.userId}}\", \"userId\": {{1.userId}}}"
      }
    },
    {
      "type": "ASSERT",
      "name": "Final Check",
      "description": "Check a bunch of stuff",
      "checks": [
        "'{{2.name}}' == 'Leanne Graham'",
        "{{2.id}} == {{1.userId}}",
        "{{3.title}} == 'A Test'"
      ]
    }
  ]
}
```