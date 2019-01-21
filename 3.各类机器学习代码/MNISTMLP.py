import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import scipy.misc
import random
import matplotlib.cm as cm
import itertools
import scipy.optimize
from scipy.special import expit

datafile = 'data/ex4data1.mat'
mat = scipy.io.loadmat(datafile)
X, y = mat['X'], mat['y']
X = np.insert(X, 0, 1, axis=1)
print(type(X),type(y))

def get_datum_img(row):
    width, height = 20, 20
    square = row[1:].reshape(width, height)
    return square.T


def display_data(indices_to_display=None):
    width, height = 20, 20
    n_rows, n_cols = 10, 10
    if not indices_to_display:
        indices_to_display = random.sample(range(X.shape[0]), 100)

    big_picture = np.zeros((height * n_rows, width * n_cols))

    i_row, i_col = 0, 0

    for idx in indices_to_display:
        if i_col == n_cols:
            i_row += 1
            i_col = 0
        i_img = get_datum_img(X[idx])
        big_picture[i_row * height:i_row * height + i_img.shape[0], i_col * width:i_col * width + i_img.shape[1]] \
            = i_img
        i_col += 1
    plt.figure(figsize=(6, 6))
    img = scipy.misc.toimage(big_picture)
    plt.imshow(img)
    plt.show()


display_data()

# Model representation
datafile = 'data/ex4weights.mat'
mat = scipy.io.loadmat(datafile)
Theta1, Theta2 = mat['Theta1'], mat['Theta2']

input_layer_size = 400
hidden_layer_size = 25
output_layer_size = 10
n_training_samples = X.shape[0]


def flatten_params(thetas_list):
    flattened_list = [my_thetas.flatten() for my_thetas in thetas_list]
    combined = list(itertools.chain.from_iterable(flattened_list))
    # assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。
    # 可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。
    assert len(combined) == (input_layer_size + 1) * hidden_layer_size + (hidden_layer_size + 1) * output_layer_size

    return np.array(combined).reshape((len(combined), 1))


def reshape_params(flattened_array):
    theta1 = flattened_array[:(input_layer_size + 1) * hidden_layer_size] \
        .reshape((hidden_layer_size, input_layer_size + 1))
    theta2 = flattened_array[(input_layer_size + 1) * hidden_layer_size:] \
        .reshape((output_layer_size, hidden_layer_size + 1))
    return [theta1, theta2]


def flatten_x(my_x):
    return np.array(my_x.flatten()).reshape((n_training_samples * (input_layer_size + 1), 1))


def reshape_x(flattened_x):
    return np.array(flattened_x).reshape((n_training_samples, input_layer_size + 1))


# Feed_forward and cost function
# forward的意义在于每次都提供新的z和a

def propagate_forward(row, thetas):
    features = row
    # The output is a vector with element[0] for the hidden layer,
    # and element[1] for the output layer
    # each element is a tuple of (zs, as)
    # where "zs" and "as" have shape (# of units in that layer, 1)
    zs_as_per_layer = []
    for i in range(len(thetas)):
        theta = thetas[i]
        z = theta.dot(features).reshape((theta.shape[0], 1))
        a = expit(z)
        zs_as_per_layer.append((z, a))
        if i == len(thetas) - 1:
            return np.array(zs_as_per_layer)
        a = np.insert(a, 0, 1)
        features = a


def compute_cost(my_thetas_flattened, my_x_flattened, my_y, my_lambda=0.):
    # First unroll the parameters
    my_thetas = reshape_params(my_thetas_flattened)

    # Unroll X
    my_x = reshape_x(my_x_flattened)

    total_cost = 0

    m = n_training_samples

    # sum of m (1)
    for i_row in range(m):
        my_row = my_x[i_row]

        # my hypo 就是拿random theta直接推得得值
        my_hypo = propagate_forward(my_row, my_thetas)[-1][1]   # 最后一个a值, a应该是10个数

        tmp_y = np.zeros((10, 1))
        tmp_y[my_y[i_row] - 1] = 1

        # tmp_y也是10个数 所以sum k在这里 点乘
        my_cost = - tmp_y.T.dot(np.log(my_hypo)) - (1 - tmp_y.T).dot(np.log(1 - my_hypo))
        total_cost += my_cost


    total_cost = float(total_cost) / m

    # sum of k (thetas(1)), sum of i layer(2), sum of i+1 layer(3)
    # then theta**2
    total_reg = 0.
    for my_theta in my_thetas:  # (1)
        total_reg += np.sum(my_theta * my_theta)    # (2),(3)
    total_reg *= float(my_lambda) / (2 * m)

    return total_cost + total_reg


#Theta_list = [Theta1, Theta2]

#print(compute_cost(flatten_params(Theta_list), flatten_x(X), y, my_lambda=1.))


# Back_propagation
# Sigmoid gradient

# z = theta.dot(a)
# a = g(z)
# sigmoid is the derivative of g
# g is the expit()

def sigmoid_gradient(z):
    dummy = expit(z)
    return dummy * (1 - dummy)

# goal: min J(theta)
# derivative ~ = (1/m) * sum(a*error_for_layer)

# In back_propagate
# set delta = 0 for all (accumulator)
# iter: delta = delta + error_for_layer(a)


# Initialize random theta
def get_rand_thetas():
    epsilon_init = 0.12
    theta1_shape = (hidden_layer_size, input_layer_size + 1)
    theta2_shape = (output_layer_size, hidden_layer_size + 1)
    # The * unpacks a tuple in multiple input arguments
    rand_thetas = [np.random.rand(*theta1_shape) * 2 * epsilon_init - epsilon_init, \
                   np.random.rand(*theta2_shape) * 2 * epsilon_init - epsilon_init]
    return rand_thetas

# part1:
# error(delta in same meaning) = theta.T.dot(error(i+1)).dot(sigmoid_gradient(z))
# this error is implement in layers
# J(theta) likes a total cost
# der(J(theta)) = (1/m)sum(a(l)delta(l+1))
# set new delta_set all 0
# delta += a.dot(delta(i+1)) the right side is old delta
# we use capital-delta D, D = 1/m(new_delta + reg), we take it as "accumulator"
# we find capital-delta D is our der(J(theta)) in a involved way
# summary: old_delta-> new_delta-> capital-delta-> der(J(theta))
# part2:
# we know J(theta) function before
# and capital-delta = der(J(theta)) for any t in m
# now let us do the unroll, it just is the flatten. We unroll both theta and capital d we get
# check part: we have der(j(theta)) = (J(theta+epsilon) - J(theta-epsilon))/(2*epsilon)
# we iterative this formula to get best theta
# for more epsilon = root_square(6)/root_s(L_output+L_input)
# and let theta ini between -eps,eps
# the actual part is that we have d1 d2 by back_propagate
# then we can just the machine learning function to find the minimum
# !!!
# theta = theta - alpha*capital_D


def back_propagate(my_thetas_flattened, my_x_flattened, my_y, my_lambda=0.):
    my_thetas = reshape_params(my_thetas_flattened)

    my_x = reshape_x(my_x_flattened)

    Delta1 = np.zeros((hidden_layer_size, input_layer_size + 1))
    Delta2 = np.zeros((output_layer_size, hidden_layer_size + 1))

    m = n_training_samples
    for i_row in range(m):
        my_row = my_x[i_row]
        a1 = my_row.reshape((input_layer_size + 1, 1))
        temp = propagate_forward(my_row, my_thetas)
        z2 = temp[0][0]
        a2 = temp[0][1]
        a3 = temp[1][1]
        tmp_y = np.zeros((10, 1))
        tmp_y[my_y[i_row] - 1] = 1
        delta3 = a3 - tmp_y
        delta2 = my_thetas[1].T[1:, :].dot(delta3) * sigmoid_gradient(z2)
        a2 = np.insert(a2, 0, 1, axis=0)
        Delta1 += delta2.dot(a1.T)
        Delta2 += delta3.dot(a2.T)

    d1 = Delta1 / float(m)
    d2 = Delta2 / float(m)

    d1[:, 1:] = d1[:, 1:] + (float(my_lambda) / m) * my_thetas[0][:, 1:]
    d2[:, 1:] = d2[:, 1:] + (float(my_lambda) / m) * my_thetas[1][:, 1:]

    return flatten_params([d1, d2]).flatten()


#flatten_d1_d2 = back_propagate(flatten_params(Theta_list), flatten_x(X), y, my_lambda=0.)
#d1, d2 = reshape_params(flatten_d1_d2)


# Gradient checking

def check_gradient(my_thetas, my_ds, my_x, my_y, my_lambda=0.):
    my_eps = 5
    flattened = flatten_params(my_thetas)
    flattened_ds = flatten_params(my_ds)
    flattened_my_x = flatten_x(my_x)
    n_elems = len(flattened)
    for i in range(10):
        x = int(np.random.rand() * n_elems)
        epsvec = np.zeros((n_elems, 1))
        epsvec[x] = my_eps
        cost_high = compute_cost(flattened + epsvec, flattened_my_x, my_y, my_lambda)
        cost_low = compute_cost(flattened - epsvec, flattened_my_x, my_y, my_lambda)
        my_grad = (cost_high - cost_low) / float(2 * my_eps)
        print("Element: %d. Numerical Gradient = %f. BackProp Gradient = %f." % (x, my_grad, flattened_ds[x]))
        #print(x, my_grad, flattened_ds[x])


#check_gradient(Theta_list, [d1, d2], X, y)


# Regularized Neural Networks

# here we use scipy.optimze to finish training
# actually, we need to these
# 1. Randomly initialize the weights
# 2. do forward propagation to get h(x)
# 3. implement cost function of it
# 4. implement back_propagation to compute partial derivatives
# 5. use gradient checking to confirm backpropagation works
# actual work start here
# 6.use the epsilon function to finish all of the work in other way
# be care that back_propagate is just use to return gradient of f at x
def train_nn(my_lambda=0.):
    random_thetas_unrolled = flatten_params(get_rand_thetas())
    result = scipy.optimize.fmin_cg(compute_cost, x0=random_thetas_unrolled, fprime=back_propagate, \
                                    args=(flatten_x(X), y, my_lambda), maxiter=50, disp=True, full_output=True)

    return reshape_params(result[0])


#learned_thetas = train_nn()


def predict_nn(row, thetas):
    classes = list(range(1, 10)) + [10]
    output = propagate_forward(row, thetas)
    return classes[np.argmax(output[-1][1])]


def compute_accuracy(my_x, my_thetas, my_y):
    n_correct, n_total = 0, my_x.shape[0]
    for i_row in range(n_total):
        if int(predict_nn(my_x[i_row], my_thetas)) == int(my_y[i_row]):
            n_correct += 1
    print("accuracy: %0.1f%%" % (100 * (float(n_correct) / n_total)))


#compute_accuracy(X, learned_thetas, y)

#learned_regularized_thetas = train_nn(my_lambda=1.)

#compute_accuracy(X, learned_regularized_thetas, y)


# Visualizing the hidden layer

def display_hidden_layer(my_theta):
    my_theta = my_theta[:, 1:]
    assert my_theta.shape == (25, 400)

    width, height = 20, 20
    n_rows, n_cols = 5, 5

    big_picture = np.zeros((height * n_rows, width * n_cols))

    i_row, i_col = 0, 0
    for row in my_theta:
        if i_col == n_cols:
            i_row += 1
            i_col = 0
        # add bias unit back in?
        iimg = get_datum_img(np.insert(row, 0, 1))
        big_picture[i_row * height:i_row * height + iimg.shape[0], i_col * width:i_col * width + iimg.shape[1]] = iimg
        i_col += 1
    plt.figure(figsize=(6, 6))
    img = scipy.misc.toimage(big_picture)
    plt.imshow(img, cmap=cm.Greys_r)
    plt.show()

#display_hidden_layer(learned_thetas[0])

from sklearn.model_selection import train_test_split
X, X_test,y,y_test = train_test_split(X,y,test_size=0.1)
import MLPGenerator
print(X_test[0].shape)
MLPG = MLPGenerator.MLPGenerator([400,25,10],'digitRecognition',X,y,X_test,y_test)
learn = MLPG.trainNN()
total = len(X_test)
correct = 0
for i in range(len(X_test)):
    print(np.argmax(MLPG.propagateForward(X_test[i],learn)[-1][1]) + 1,y_test[i])
    if np.argmax(MLPG.propagateForward(X_test[i],learn)[-1][1]) + 1 == y_test[i][0]:
        correct += 1
print(correct/total)