import os
import json
import api
import assertion


def load_suites():
    root = 'sts/suites/'  # TODO: refactor/rename
    suites = []
    for filename in os.listdir(root):
        suite = open(root + filename).read()
        suites.append(json.loads(suite))
    return suites


def execute_suite(suite):
    print('Initializing suite: {}'.format(suite.get('name', 'unnamed suite')))
    steps = suite.get('steps', [])
    responses = []
    for step in steps:
        step_type = step.get('type')
        step_name = step.get('name', 'WARNING: MISSING NAME')
        step_desc = step.get('description', 'WARNING: MISSING DESCRIPTION')
        print('Testing {type}: {name} ({desc})'.format(type=step_type, name=step_name, desc=step_desc))
        if step_type == 'HTTP':
            res = api.call(step['request'], responses)
            responses.append(res)
        elif step_type == 'ASSERT':
            print('Assertion: ', step.get('checks'))
            assertion.assertion(step.get('checks'), responses)


def main():
    for suite in load_suites():
        execute_suite(suite)


main()
