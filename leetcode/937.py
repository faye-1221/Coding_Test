class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        digit =[]

        for l in logs:
            if l.split()[1].isdigit():
                digit.append(l)
            else:
                letter.append(l)

        letter.sort(key= lambda x: (x.split()[1:], x.split()[0]))

        return (letter + digit)