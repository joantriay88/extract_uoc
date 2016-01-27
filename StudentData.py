class StudentData:
    def __init__(slef):
        pass

    def calculateNameStudents(self, jsonfile):
        li_names = []
        for line in jsonfile:
            if len(line) > 0:
                if line['username'] not in li_names:
                    li_names.append(str(line['username']))
        return li_names
