import os
import json
import api
import assertion
import test_report

ROOT = 'sts/'
ROOT_SUITE = ROOT + 'suites/'
ROOT_RESULT = ROOT + 'results/'


def load_suites():
    suites = []
    for filename in os.listdir(ROOT_SUITE):
        suite = open(ROOT_SUITE + filename).read()
        json_suite = json.loads(suite)
        json_suite['filename'] = filename
        suites.append(json_suite)
    return suites


def execute_suite(suite):
    print('Initializing suite: {}'.format(suite.get('name', 'unnamed suite')))
    config = suite.get('config', {})
    steps = suite.get('steps', [])
    responses = []
    for step_number, step in enumerate(steps):
        step_type = step.get('type')
        step_name = step.get('name', 'WARNING: MISSING NAME')
        step_desc = step.get('description', 'WARNING: MISSING DESCRIPTION')
        print('Testing [{step_number}/{total_steps} : {percentage}]{type}: {name} ({desc})'.format(
            step_number=step_number,
            total_steps=len(steps),
            percentage=str(round((step_number / len(steps) * 100), 1)) + '%',
            type=step_type,
            name=step_name,
            desc=step_desc)
        )
        if step_type == 'HTTP':
            res = api.call(step['request'], responses, config)
            responses.append(res)
        elif step_type == 'ASSERT':
            print('Assertion: ', step.get('checks'))
            responses.append(assertion.assertion(step.get('checks'), responses))

    test_report.build_report(responses, suite, ROOT_RESULT)


def main():
    for suite in load_suites():
        execute_suite(suite)


main()
