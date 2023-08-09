import numpy as np

def residual(P_west, P_cell, P_east, P_cell_prev, dx, dt, eta):
    res = alpha(P_cell, P_east, P_west, dx) * P_east - \
          beta(P_cell, P_cell_prev, dx, dt, eta) * P_cell + \
          gamma(P_cell, P_east, P_west, dx) * P_west
    return res

def beta(P_cell, P_cell_prev, dx, dt, eta):
    b = (2 * (P_cell / (mu_gas(P_cell) * z_factor(P_cell))) / dx**2) + \
        ((1 / (eta * dt)) * ((1 / z_factor(P_cell)) - (P_cell_prev / (P_cell * z_factor(P_cell_prev)))))
    return b

def gamma(P_cell, P_east, P_west, dx):
    g = (-(P_west / (mu_gas(P_west) * z_factor(P_west))) +
         4 * (P_cell / (mu_gas(P_cell) * z_factor(P_cell))) +
         (P_east / (mu_gas(P_east) * z_factor(P_east)))) / (4 * dx**2)
    return g

# define P west and P east
def create_P_west_east(P_cell, P_left):
    P_west = np.zeros_like(P_cell)
    P_east = np.zeros_like(P_cell)

    for i in range(len(P_cell)):
        if i == 0:  # most-left grid
            P_west[i] = P_left
            P_east[i] = P_cell[i + 1]
        elif i == len(P_cell) - 1:  # most-right grid
            P_west[i] = P_cell[i - 1]
            P_east[i] = P_cell[i]
        else:
            P_west[i] = P_cell[i - 1]
            P_east[i] = P_cell[i + 1]
    return P_west, P_east

def alpha(P_cell, P_east, P_west, dx):
    a = ((P_west / (mu_gas(P_west) * z_factor(P_west))) +
         4 * (P_cell / (mu_gas(P_cell) * z_factor(P_cell))) -
         (P_east / (mu_gas(P_east) * z_factor(P_east)))) / (4 * dx**2)
    return a

def mu_gas(p):
    # Gas viscosity (Gonzalez, Bukacek and Lee, 1967)
    press = np.array([2000, 2500, 3000, 3500, 4000, 4500, 5000, 6000])
    visc = np.array([0.0164, 0.0174, 0.0186, 0.0197, 0.0209, 0.0220, 0.0233, 0.0257])
    fit = np.polyfit(press, visc, 1)
    mu = np.polyval(fit, p)
    return mu

def z_factor(p):
    # Papay correlation
    T = 679.7  # 220 F
    Pc = 673
    Tc = 344  # Critical properties of methane
    ppr = p / Pc
    tpr = T / Tc
    z_fact = 1 - ((3.53 * ppr) / (10**(0.9813 * tpr))) + ((0.274 * ppr**2) / (10**(0.815 * tpr)))
    return z_fact

# define Dn
def create_D_n(P_left, alpha_n):
    # return np.array([P_left, 0, 0, 0, 0]).reshape(5, 1) * -alpha_n
    return np.array([0, 0, 0, 0, 0]).reshape(5, 1)

# define On
def create_O_n(P_cell, P_left, alpha_n, beta_n, gamma_n):
    return np.array([alpha_n[0, 0]*P_left - beta_n[0, 0]*P_cell[0, 0] + gamma_n[0, 0]*P_cell[1, 0],
                     alpha_n[1, 0]*P_cell[0, 0] - beta_n[1, 0]*P_cell[1, 0] + gamma_n[1, 0]*P_cell[2, 0],
                     alpha_n[2, 0]*P_cell[1, 0] - beta_n[2, 0]*P_cell[2, 0] + gamma_n[2, 0]*P_cell[3, 0],
                     alpha_n[3, 0]*P_cell[2, 0] - beta_n[3, 0]*P_cell[3, 0] + gamma_n[3, 0]*P_cell[4, 0],
                     alpha_n[4, 0]*P_cell[3, 0] - beta_n[4, 0]*P_cell[4, 0] + gamma_n[4, 0]*P_cell[4, 0]]).reshape(5, 1)

# define x
def create_x(e_n, e_dot, D_n):
    return np.hstack([e_n, e_dot, D_n]).reshape(-1, 1)

# define rbf sigmoid activation function
def rbf_sigmoid(x):
    return 1 / (1 + np.e ** -np.abs(x))

# define derivative of rbf sigmoid
def rbf_sigmoid_derivative(x):
    return rbf_sigmoid(x) * (1 - rbf_sigmoid(x))

# define main algorithm
def solve_PDE():
    # Initialize parameters
    P_0 = 5000 * np.ones([5, 1]) # P init
    dx=2.5
    # P_0 = np.zeros([5, 1])
    P_prev = P_0.copy()
    P_left = 4500
    dt = 0.0069
    perm = 10
    por = 0.10
    eta = 0.00633 * perm / por
    tol = 1e-6
    lmbd = 300

    # Initialize x
    P_west_0, P_east_0 = create_P_west_east(P_0, P_left)
    alpha_0 = alpha(P_0, P_east_0, P_west_0, dx)
    beta_0 = beta(P_0, P_prev, dx, dt, eta)
    gamma_0 = gamma(P_0, P_east_0, P_west_0, dx)
    D_0 = create_D_n(P_left, alpha_0)
    O_0 = create_O_n(P_0, P_left, alpha_0, beta_0, gamma_0)
    print(O_0)
    print(alpha_0, beta_0, gamma_0)

    e_0 = D_0 - O_0
    e_prev = np.zeros([5, 1])
    e_dot = (e_0 - e_prev) / dt
    x = create_x(e_0, e_dot, D_0)
    # print(P_0.shape, alpha_0.shape, beta_0.shape, gamma_0.shape, D_0.shape, O_0.shape, e_0.shape, e_dot.shape, x.shape)

    # Initialize weights v and w
    v = np.random.rand(5, 15)
    # v = np.zeros([5, 15])
    Fv = 1600
    w = np.random.rand(5, 5)
    # w = np.zeros([5, 5])
    Fw = 1500

    # Initialize iteration counter
    n = 1
    max_n = 200
    while n < max_n:
        # print(n)
        # feed-forward, calculate delta p
        h = rbf_sigmoid(v @ x)
        delta_P = w @ h

        # calculate en, and create next x
        P_n = P_prev + delta_P
        P_west_n, P_east_n = create_P_west_east(P_n, P_left)
        alpha_n = alpha(P_n, P_east_n, P_west_n, dx)
        beta_n = beta(P_n, P_0, dx, dt, eta)
        gamma_n = gamma(P_n, P_east_n, P_west_n, dx)
        D_n = create_D_n(P_left, alpha_n)
        O_n = create_O_n(P_n, P_left, alpha_n, beta_n, gamma_n)
        # print(n)
        # print(alpha_n, beta_n, gamma_n)
        # print(O_n)

        e_n = D_n - O_n
        print(e_n)
        # stopping criteria
        if np.max(np.abs(e_n)) < tol:
            break
        e_dot = (e_n - e_prev) / dt
        x = create_x(e_n, e_dot, D_n)

        # update weights v and w
        S = e_dot + lmbd*e_n
        w += Fw * (S @ h.T)
        v += Fv * ((w.T @ S) * rbf_sigmoid_derivative(h)) @ x.T

        # update prev variables
        P_prev = P_n
        e_prev = e_n

        # increment iteration
        n += 1
    return P_n, e_n, S, v, w

solve_PDE()