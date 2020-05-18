import filler


def assertion(checks, responses):
    checks_results = []
    for check in checks:
        filled_check = filler.fill_regex(check, responses)
        check_result = eval(filled_check)
        print('check {0} >>> {1}'.format(check, check_result))
        checks_results.append(check_result)
    print('checks results', checks_results)
