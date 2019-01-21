import Common.Register as reg
import Common.Trace_Initializer as ti
import PerceptronWay.Perceptron_Table as pt


class Perceptron:

    def train(self, address, weight, yi, perceptron_table, global_hr):
        """
        According to the definition of perceptron, we update our f(x) model if f(x)*yi is less than 0 for each trace.
        While if f(x) is too small, it also need update.
        :param address: int PC address
        :param weight: float random set at first, and update it base on wx>0?
        :param yi: int previous branch result TNT == 1?1:-1
        :param perceptron_table: dictionary construct by 1000 perceptrons, each perceptron has 80 weight
        :param global_hr: list 80bit global history table
        :return: void
        """
        branch_weight = perceptron_table.perceptron[address]
        global_history = global_hr.global_history
        theta = len(global_history) * 2 + 20
        if weight * yi < 0 or abs(weight) < theta:
            for i in range(len(branch_weight)):
                branch_weight[i] += yi * global_history[i]

    def predict(self, address, perceptron_table, global_hr):
        """
        We use our perceptron model to generate a f(x) result where x is the our global history.
        If the result is larger than 0, taken, vice versa.
        :param address: int PC address
        :param perceptron_table: same as previous
        :param global_hr: same as previous
        :return: float predict result
        """
        weight = 0.0
        branch_weight = perceptron_table.perceptron[address]
        global_history = global_hr.global_history
        for i in range(len(global_history)):
            weight += branch_weight[i] * global_history[i]
        return weight

    def perceptron_go(self, trace_file):
        """

        :param trace_file:
        :return:
        """
        int_list = [1] * 80
        total_p = 0
        correct_p = 0
        global_hr = reg.GlobalHistoryRegister(int_list)
        perceptron_table = pt.PerceptronTable({})
        perceptron_table.perceptron_table_generator(len(int_list), 1000, perceptron_table.perceptron)
        trace_list = ti.TraceGenerator().trace_list_generator(trace_file)

        for trace in trace_list:
            yi = -1
            if trace.TNT == 1:
                yi = 1
            prediction = self.predict(trace.PC % 1000, perceptron_table, global_hr)
            self.train(trace.PC % 1000, prediction, yi, perceptron_table, global_hr)
            actual = False
            if trace.TNT == 1:
                actual = True
                del global_hr.global_history[0]
                global_hr.global_history.append(1)
            else:
                del global_hr.global_history[0]
                global_hr.global_history.append(-1)
            if (prediction > 0) == actual:
                correct_p += 1
            total_p += 1

        return correct_p, correct_p / total_p

