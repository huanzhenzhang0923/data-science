import numpy as np
#-------------------------------------------------------------------------
'''
    Problem 3: PageRank algorithm (version 1) 
    In this problem, we implement a simplified version of the pagerank algorithm, which doesn't consider about sink node problem or sink region problem.
    You could test the correctness of your code by typing `nosetests -v test3.py` in the terminal.
'''

#--------------------------
def compute_P(A):
    '''
        compute the transition matrix P from addjacency matrix A. P[j][i] represents the probability of moving from node i to node j.
        Input: 
                A: adjacency matrix, a (n by n) numpy matrix of binary values. If there is a link from node i to node j, A[j][i] =1. Otherwise A[j][i]=0 if there is no link.
        Output: 
                P: transition matrix, a (n by n) numpy matrix of float values.  P[j][i] represents the probability of moving from node i to node j.
    The values in each column of matrix P should sum to 1.
    '''
    #########################################
    ## INSER YOUR CODE HERE
    # sum of each column of A
    A = np.asarray(A)

    B=np.sum(A,axis=0)                     ##整列之和
    P=np.zeros(A.shape)                    
 
    for i in range(len(A)):
         P[:,i]=A[:,i]/B[i]                     ##将各列参数除以整列之和得出传递矩阵
    
    # create a diagonal matrix  


    # normalize each column of A

    #########################################
    return np.asmatrix(P)



#--------------------------
def random_walk_one_step(P, x_i):
    '''
        compute the result of one step random walk.
        Input: 
                P: transition matrix, a (n by n) numpy matrix of float values.  P[j][i] represents the probability of moving from node i to node j.
                x_i: pagerank scores before the i-th step of random walk. a numpy vector of shape (n by 1).
        Output: 
                x_i_plus_1: pagerank scores after the i-th step of random walk. a numpy vector of shape (n by 1).
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    x_i_plus_1=np.dot(P,x_i);


    #########################################
    return x_i_plus_1


#--------------------------
def random_walk(P, x_0, max_steps=10000):
    '''
        compute the result of multiple-step random walk. The random walk should stop if the score vector x no longer change (converge) after one step of random walk, or the number of iteration reached max_steps.
        Input: 
                P: transition matrix, a (n by n) numpy matrix of float values.  P[j][i] represents the probability of moving from node i to node j.
                x_0: the initial pagerank scores. a numpy vector of shape (n by 1).
                max_steps: the maximium number of random walk steps. an integer value.  
        Output: 
                x: the final pagerank scores after multiple steps of random walk. a numpy vector of shape (n by 1).
                n_steps: the number of steps actually used (for example, if the vector x no longer changes after 3 steps of random walk, return the value 3. 
        Hint: you could use np.allclose(x, previous_x) function to determine when to stop the random walk iterations.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    n_steps=0
    A=x_0          ##将pagerank矩阵初始值作为当前矩阵的排名
    for i in range(max_steps):
        n_steps=i+1
        x=random_walk_one_step(P,A)
        if np.allclose(x,A)==True:
            break
        else:
            A=x
    #########################################

    return x, n_steps


#--------------------------
def pagerank_v1(A):
    ''' 
        A simplified version of PageRank algorithm.
        Given an adjacency matrix A, compute the pagerank score of all the nodes in the network. 
        Here we ignore the issues of sink nodes and sink regions in the network.
        Input: 
                A: adjacency matrix, a numpy matrix of binary values. If there is a link from node i to node j, A[j][i] =1. Otherwise A[j][i]=0 if there is no link.
        Output: 
                x: the ranking scores, a numpy vector of float values, such as np.array([[.3], [.5], [.7]])
    '''

    # compute the transition matrix from adjacency matrix
    P = compute_P(A)

    # initialize the score vector with all one values
    num_nodes, _ = A.shape # get the number of nodes (n)
    x_0 =  np.ones((num_nodes,1)) # create an all-one vector of shape (n by 1)
    
    # random walk
    x, n_steps = random_walk(P, x_0)

    return x

