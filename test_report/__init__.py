import json
import os


# http calls with string building:
def build_report(responses, suite, ROOT_RESULT):
    filename = suite.get('filename', None)
    if filename is not None:
        clean_filename = filename.split('.json')[0]
        print('Building RAW Full Report for {0}'.format(suite.get('name')))
        with open(ROOT_RESULT + clean_filename + '_raw_report.json', 'w') as raw_report_file:
            json.dump(responses, raw_report_file, indent=4, separators=(',', ': '))

        print('Building Markdown Summary Report for {0}'.format(suite.get('name')))
        destination = ROOT_RESULT + clean_filename + '_summary.md'
        build_markdown_summary(destination, responses)


def build_markdown_summary(destination, responses):

    report = '''
# API Report results
    '''
    # TODO: HANDLE MULTIPLE ASSERTION STEPS
    assertions = list(filter(lambda x: x.get('type', 'ASSERT') == 'ASSERT', responses))[0]

    report += '''
* Total Tests: {total}
* Passed Tests: {passed}
* Failed Tests: {failed}
* Percentage: {percentage}
    '''.format(
        total=assertions['summary']['total'],
        passed=assertions['summary']['passed'],
        failed=assertions['summary']['failed'],
        percentage=str(round(assertions['summary']['passed'] * 100 / assertions['summary']['total'], 2)) + '%'
    )

    report += '''
| Check | Filled Check | Test Result |
| ------------ | --------- | ----- |
'''

    for result in assertions['results']:
        report += '| {check} | {filled} | {result} | \n'.format(
            check=result['check'],
            filled=result['filled_check'],
            result='&#x2611;' if result['result'] else '&#x2612;'
        )

    open(destination, 'w+').write(report)
