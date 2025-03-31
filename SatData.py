import json


class SatData:
    def __init__(self):

        with open('sat.json', 'r') as infile:
            self._data = json.load(infile)
            # header for file
            self._header = []

            # add header names to the header list
            for i in range(8, 14):
                self._header.append(self._data['meta']['view']['columns'][i]['name'])

    def save_as_csv(self, schools):
        # titles = ['DBN', 'School Name', 'Number of Test Takers', 'Critical Reading Mean', 'Mathematics Mean',
        #           'Writing Mean']
        # with open('output.csv', 'w') as outfile:
        #     # hard code column titles
        #     for i in range(len(titles)):
        #         if i == len(titles) - 1:
        #             outfile.write(titles[i] + '\n')
        #         else:
        #             outfile.write(titles[i] + ',')
        with open('output.csv', 'w') as outfile:
            # add header list to the
            outfile.write(','.join(self._header))
            outfile.write('\n')

            for row in self._data['data']:
                # check if id in schools dbn list
                if row[8] in schools:
                    for i in range(8, len(row)):
                        # the last item of the row is added, start a new row
                        if i == len(row) - 1:
                            outfile.write(str(row[i]) + "\n")
                        # if there is a coma in the "cell" data then include the data inside ""
                        elif ',' in str(row[i]):
                            outfile.write(f'"{row[i]}"')
                        else:
                            # add the data followed by a coma
                            outfile.write(str(row[i]) + ",")



sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)
# with open('sat.json', 'r') as infile:
#     all_data = json.load(infile)
#
#     with open('outfile.csv', 'w') as outfile:
#         print(all_data['meta']['view']['columns'][8]['name'])