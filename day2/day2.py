def loadFile():
    reports = []
    with open("day2/input.txt") as file:
        for l in file:
            reports.append([int(n) for n in l.split(' ')])
    return reports

def reportSafeWithDamper(report):
    safe = reportSafe(report)
    if not safe[0]:
        for i in range(len(report)):
            safe = reportSafe(report[:i] + report[i+1:])
            if safe[0]:
                return safe
        return (False, -1)
    else:
        return safe

def reportSafe(report):
    print("Checking report {0} for safety".format(report))
    if len(report) <= 1:
        return (True, -1)
    if report[0] > report[1]:
        # decreasing
        for i in range(0, len(report)):
            if i > 0 and report[i] >= report[i-1]:
                return (False, i)
            if i > 0 and report[i] < report[i-1] - 3:
                return (False, i)
        return (True, -1)
    else:
        # increasing
        for i in range(1, len(report)):
            if report[i] <= report[i-1]:
                return (False, i)
            if report[i] > report[i-1] + 3:
                return (False, i)
        return (True, -1)

if __name__ == "__main__":
    reports = loadFile()
    safeReports = 0
    for r in reports:
        safe = reportSafe(r)[0]
        if safe:
            safeReports += 1
        print("Report {0} is {1}".format(r, "safe" if safe else "unsafe"))
    print("Safe reports: {0}".format(safeReports))

    safeWithDamperReports = 0
    for r in reports:
        safeWithDamper = reportSafeWithDamper(r)[0]
        if safeWithDamper:
            safeWithDamperReports += 1
            print("Report {0} is {1} with damper".format(r, "safe" if safe else "unsafe"))
    print("Safe with damper reports: {0}".format(safeWithDamperReports))
    