

class ClinicalTrialsData:

    studies = None
    db = None
    conn = None
    type_counts = None
    curr_group = 'phase'

    def __init__(self, db, conn):
        self.db = db
        self.conn = conn

    # Uncomment when tested and implemented
    # def remove_filter(self, filter_category, filter_name):
    #    """
    #    Removes a specified filter from the list of filters,
    #       and re-runs the query
    #    :param filter_category:
    #           the column in the DB that the user wants to filter
    #    :param filter_name:
    #           the specific value to filter on in that column
    #    """
    #    pass

    # Uncomment when tested and implemented
    # def apply_filter(self, filter_category, filter_name):
    #    """
    #    Adds the specified filter to the list of filters,
    #       and re-runs the current query
    #    :param filter_category:
    #           the column in the DB that the user wants to filter
    #    :param filter_name:
    #           the specific value to filter on in that column
    #    """
    #    pass

    # Uncomment when tested and implemented
    # def get_current_filters(self):
    #    """
    #    Get the list of currently applied filters
    #    :return: the list of human-readable strings
    #    """
    #    pass

    # Uncomment when tested and implemented
    def set_group_by(self, attribute):
        """
        Sets the attribute to group the data by,
           runs the query for the first time
        :param attribute:
               human-readable string
        """
        self.curr_group = attribute
        # self.type_counts = self.studies.groupby(attribute).size()

    def get_group_by(self):
        """
        Get the variable currently used to group the data
        :return: a human-readable string
        """
        return self.curr_group

    # Uncomment when tested and implemented
    # def get_labels(self):
    #    """
    #    Get the lists of strings describing each category
    #       for grouping the data
    #    :return:
    #           list of human-readable strings
    #    """
    #    return self.type_counts.index

    # Uncomment when tested and implemented
    # def get_values(self):
    #    """
    #    Get the list of integers describing the amounts for each label
    #    :return: an array of ints
    #    """
    #    pass

    # Uncomment when tested and implemented
    # def get_variables(self):
    #    """
    #    Get the variables describing the options for displaying data
    #    :return:
    #           a list of dictionaries containing
    #           the label for human-readable display
    #           and the corresponding string in terms
    #           of the XML Schema
    #    ex - {'label': 'Study Type', 'value': 'study_type'}
    #    """
    #    pass

    # Uncomment when tested and implemented
    def populate_tables(self):
        self.studies = self.db.read_sql('select * from studies', con=self.conn)