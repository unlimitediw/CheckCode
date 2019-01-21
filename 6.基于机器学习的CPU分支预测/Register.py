class LocalHistoryRegister:
    def __init__(self, local_history):
        """
        a map from trace pc address to a history list of bits
        the size of localHistory is the sum of all address in trace
        :param local_history: dictionary[address]
        """
        self.local_history = local_history


class GlobalHistoryRegister:
    def __init__(self, global_history):
        """
        the length of the global_history is set in a fixed number
        :param global_history: list[int]
        """
        self.global_history = global_history
