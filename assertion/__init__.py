import filler


def assertion(checks, responses):
    checks_results = []
    for check in checks:
        filled_check = filler.fill_regex(check, responses)
        if '==' in filled_check:
            left = check.split('==')[0].strip()
            right = check.split('==')[0].strip()
            check_result = left == right
        if '<=' in filled_check:
            print(filled_check)
        if '>=' in filled_check:
            print(filled_check)
        if '<' in filled_check:
            print(filled_check)
        if '>' in filled_check:
            print(filled_check)
        if '!=' in filled_check:
            print(filled_check)
        print('check {0} :: {1}'.format(check, check_result))
        checks_results.append(check_result)
    print('checks results', checks_results)
