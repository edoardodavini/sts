import json


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
        build_markdown(destination, responses, suite)


def build_markdown(destination, responses, suite):
    report = '''
# Report {name}
> {desc}
'''.format(name=suite.get('name', 'Unnamed Suite'), desc=suite.get('description', ''))

    assertions = list(filter(lambda x: x.get('type', 'ASSERT') == 'ASSERT', responses))

    report += build_markdown_summary(assertions)

    for assertion in assertions:
        report += build_markdown_detailed(assertion)

    open(destination, 'w+').write(report)


def build_markdown_summary(assertions):

    report = ""

    # stats
    total_checks = 0
    total_passed = 0
    total_failed = 0

    for assertion in assertions:
        total_checks += assertion.get('summary', {}).get('total', 0)
        total_passed += assertion.get('summary', {}).get('passed', 0)
        total_failed += assertion.get('summary', {}).get('failed', 0)

    percentage = round(total_passed * 100 / total_checks, 2)

    report += '''
* Total Tests: {total}
* Passed Tests: {passed}
* Failed Tests: {failed}
* Percentage: **{percentage}**  '''.format(
        total=total_checks,
        passed=total_passed,
        failed=total_failed,
        percentage=str(percentage) + '%'
    )

    for i in range(total_checks):
        if i < total_passed:
            report += ':green_square:'
        else:
            report += ':red_square:'

    return report


def build_markdown_detailed(assertion):
    report = '''

**{name}**
| Check | Filled Check | Result |
| ------------ | --------- | ----- |
'''.format(name=assertion.get('name'))

    for result in assertion['results']:
        report += '| {check} | {filled} | {result} | \n'.format(
            check=result['check'],
            filled=result['filled_check'],
            # result='&#x2714;' if result['result'] else '&#x2716;'
            result=':heavy_check_mark:' if result['result'] else ':x:'
        )
    return report

