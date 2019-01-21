class Trace:

    def __init__(self, PC, TNT):
        """
        PC is the address of each branch, TNT is the branch result
        :param PC: long
        :param TNT: int
        """
        self.PC = PC
        self.TNT = TNT


class TraceGenerator:

    @staticmethod
    def trace_list_generator(trace_file):
        """
        Transfer trace.txt into a list of trace, where trace.PC is the decimal address, trace.TNT is branch result
        :param trace_file: trace.txt
        :return: a list of trace
        """
        datafile = open(trace_file, 'r')
        trace_list = []
        while True:
            line = datafile.readline()
            if not line:
                break
            PC, TNT = line.split()
            PC = int(PC, 16)
            TNT = int(TNT)
            trace = Trace(PC, TNT)
            trace_list.append(trace)
        return trace_list

    @staticmethod
    def input_vector_generator( global_hr, local_hr, address, address_bit_len):
        """

        :param global_hr: global history register
        :param local_hr: local history register
        :param address: pc of trace
        :param address_bit_len: program counter bits set for free
        :return: the translated input x for the neuron network
        """
        binary_address = bin(int(address))[2:]
        binary_address = binary_address[-address_bit_len:]
        x = []
        for c in binary_address:
            if c == '1':
                x.append(1)
            else:
                x.append(0)
        x.extend(global_hr)
        x.extend(local_hr)
        return x
