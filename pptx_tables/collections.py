from pptx_tables.columns import Columns
from pptx_tables.rows import Rows


class Collection(object):
    """  This class represents a collection of data that is to be separated into rows and columns.

    Attributes:
        data: this is the data to be placed in the table
        columns: this is column information of the given data, a Columns object
        rows: this is the row information of the given data, a Rows object

    """

    def __init__(self, data):
        """ Instantiate the class with data.  this class gets called from a PptxTable.

        :param data: this is the data to be placed in the table
                    must look like [[1, 0], [0, 0], [2, 1]]
                    OR
                    must look like [{"item1": 1, "item2": 2}, {"item1": 3, "item2": 3}]
        """
        self.data = data
        self.columns = Columns(data)
        self.rows = Rows(data)

    def set_column_headers(self, headers):
        """ Updates the column index to account for the headers and updates the data self.data.

        :param headers: a list of integers or keys
        :return: None
        """
        if isinstance(self.columns.idx[0], int):
            self.data = [sorted(headers)] + self.data

            increment = [i + 1 for i in self.rows.idx]
            self.rows.idx = [0] + increment

        elif isinstance(self.columns.idx[0], str):
            datum = {}
            for i, key in enumerate(self.columns.idx):
                datum.update({key: headers[i]})
            self.data = [datum] + self.data

            increment = [i + 1 for i in self.rows.idx]
            self.rows.idx = [0] + increment

    def set_column_footers(self, footers):
        """ Updates the column index to account for the headers and updates the data self.data.

        :param footers: a list of integers or keys
        :return: None
        """
        if isinstance(self.columns.idx[0], int):
            self.data += [sorted(footers)]

            increment = [i + 1 for i in self.rows.idx]
            self.rows.idx = [0] + increment

        elif isinstance(self.columns.idx[0], str):
            datum = {}
            for i, key in enumerate(self.columns.idx):
                datum.update({key: footers[i]})
            self.data += [datum]

            increment = [i + 1 for i in self.rows.idx]
            self.rows.idx = [0] + increment

