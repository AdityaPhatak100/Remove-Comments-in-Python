import re
import sys
ip_f, op_f = sys.argv[1], sys.argv[2]
with open(ip_f, "r") as ip:
    with open(op_f, "w") as op:
        for line in ip.readlines():
            if re.match('^#', str(line).strip()):
                continue
            op.write(line)
