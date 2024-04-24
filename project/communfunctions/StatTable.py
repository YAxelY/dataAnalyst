class StatTable:
    def __init__(self):
        self.tables = {}

    def add_table(self, name, table):
        """
        Add a statistic table to the StatTable.

        Args:
        - name (str): The name of the table.
        - table (dict): The dictionary containing the statistic table.
        """
        self.tables[name] = table

    def get_table(self, name):
        """
        Retrieve a statistic table from the StatTable.

        Args:
        - name (str): The name of the table to retrieve.

        Returns:
        - dict: The requested statistic table.
        """
        return self.tables.get(name)

    def remove_table(self, name):
        """
        Remove a statistic table from the StatTable.

        Args:
        - name (str): The name of the table to remove.
        """
        if name in self.tables:
            del self.tables[name]
