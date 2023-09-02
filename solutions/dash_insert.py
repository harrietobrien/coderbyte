"""
22    For this challenge you will be manipulating a string using dashes (-).

Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str.
For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

Sample Test Cases
Input:99946
Output:9-9-946

Input:56730
Output:567-30
"""


def DashInsert(s: str):
    i = 0
    while i < len(s) - 1:
        if (int(s[i]) % 2 == 1 and
                int(s[i + 1]) % 2 == 1):
            s = f'{s[:i + 1]}-{s[i + 1:]}'
            i += 2
        else:
            i += 1
    return s


print(DashInsert("99946"))
print(DashInsert("56730"))
