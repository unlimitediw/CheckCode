import Common.Register as reg
import Common.Trace_Initializer as ti


class LVQ:
    """
    In LearningVectorQuantization we can take the bit address, globalHistory and local history for each new branch as a input x.
    What we need to do is to find the characteristic of it.
    The generate_vector is our training output, and we classify it as taken or not taken by hamming distance
    after classification we also update our global and local history according to the current trace TNT and PC
    """

    def __init__(self, pc_h_bl, local_h_bl, global_h_bl, alpha):
        """
        constructor of LearningVectorQuantization
        :param pc_h_bl: global history bit length
        :param local_h_bl: local history bit length
        :param global_h_bl: branch history bit length
        :param alpha: learning rate
        """
        self.pc_h_bl = pc_h_bl
        self.local_h_bl = local_h_bl
        self.global_h_bl = global_h_bl
        self.alpha = alpha
        self.correct_p = 0
        self.total_p = 0

    def train(self, generate_vector, input_vector, correctness, alpha):
        """
        LearningVectorQuantization algorithm, update learning vector part
        :param generate_vector: the learning generated vector
        :param input_vector: the original input vector, which is pc(last bit length) + local history + global history
        :param correctness: whether the last prediction is correct or not
        :param alpha: the learning rate
        :return: a new learning generated vector after an iteration
        """
        if correctness:
            for i in range(len(input_vector)):
                generate_vector[i] += alpha * (input_vector[i] - generate_vector[i])
        else:
            for i in range(len(input_vector)):
                generate_vector[i] -= alpha * (input_vector[i] - generate_vector[i])

        return generate_vector

    def calculate_hamming_distance(self, generate_vector, input_vector):
        """
        this value is used to compare to generate predict result
        :param generate_vector: both taken and not taken had it's own generate_vector
        :param input_vector: always the same
        :return: the sum of hamming distance for each bit of the vector
        """
        h_value = 0
        for i in range(len(input_vector)):
            h_value += pow(input_vector[i] - generate_vector[i], 2)
        return h_value

    def predict(self, input_vector, t_vector, nt_vector):
        """
        if the hamming_distance from taken vector to input vector is larger than the not taken one, it means that this address + local + global is more 'like' a taken one, than take it
        :param input_vector:
        :param t_vector:
        :param nt_vector:
        :return: take or not take
        """
        if self.calculate_hamming_distance(t_vector, input_vector) < self.calculate_hamming_distance(
                nt_vector, input_vector):
            return True
        else:
            return False

    def lvq_go(self, trace_file):
        global_hr = reg.GlobalHistoryRegister([1] * self.global_h_bl)
        local_hr = reg.LocalHistoryRegister({})

        t_vector = [1.] * (self.pc_h_bl + self.global_h_bl + self.local_h_bl)
        nt_vector = [0.] * (self.pc_h_bl + self.global_h_bl + self.local_h_bl)

        trace_list = ti.TraceGenerator().trace_list_generator(trace_file)
        for trace in trace_list:
            address = trace.PC
            if address not in local_hr.local_history:
                local_hr.local_history[address] = [1] * self.local_h_bl

            x = ti.TraceGenerator.input_vector_generator(global_hr.global_history,
                                                         local_hr.local_history[address],
                                                         address, self.pc_h_bl)

            prediction = self.predict(x, t_vector, nt_vector)
            actual = False
            if trace.TNT == 1:
                actual = True
            correct_prediction = False
            if prediction == actual:
                correct_prediction = True
                self.correct_p += 1

            if prediction:
                t_vector = self.train(t_vector, x, correct_prediction, self.alpha)
            else:
                nt_vector = self.train(nt_vector, x, correct_prediction, self.alpha)

            del global_hr.global_history[0]
            global_hr.global_history.append(trace.TNT)

            del local_hr.local_history[address][0]
            local_hr.local_history[address].append(trace.TNT)

            self.total_p += 1
        print('local history table: ',local_hr.local_history)
        print('global history table: ',global_hr.global_history)

        return self.correct_p, self.correct_p / self.total_p


