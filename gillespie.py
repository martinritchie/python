def gillespie(A_list, initial, tau, gamma, Tend, dpoints):
  # The Gillespie algorithm implemented by Martin Ritchie, 08/06/2016.
  # This algorithm will simulate a susceptible-infected-recovered 
  # epidemic on the input network. This algorithm is 
  # asyncronous, so at the end of the function code is 
  # included to ensure that the data is returned over even
  # time steps. (MR to check: is this current implementaiton 
  # stretching the time to fit up until Tend? Validation against
  # ODE will confirm this)
  # ------------------- Inputs --------------------------
  # A_list: adjacency list. 
  # Initial: initial infectious seed.
  # tau: per-link rate of infection.
  # gamma: rate of recovery. 
  # Tend: end time for the epidemic.
  # dpoints: the number of time steps. 
  # ------------------- Outputs -------------------------
  # S: the number of susceptible. 
  # I: the number of susceptible.
  # R: the number of infected.
  # T: time.
  import numpy as np
  import random
  import ipdb
  # ipdb.set_trace()
  N = len(A_list)
  # state = 0, 1, 2 corresponds to S, I and R respectively. 
  state = [0]*N
  rate_vector = [0]*2
  I_event_list = []
  R_event_list = [] 
  # Population counts and time.
  S = []
  I = []
  R = []
  T = []

  # Initialisation
  S.append(N - initial)
  I.append(initial)
  R.append(0)
  T.append(0)

  # Update the states for the I_0 nodes and associated rates
  for i in range(initial):
    state[i] = 1
    rate_vector[1] += gamma # recovery
    R_event_list.append(i)
    for j in range(len(A_list[i])):
      rate_vector[0] +=  tau # infection of neighbors
      I_event_list.append(A_list[i][j])
  # The Gillespie procedure.
  ipdb.set_trace()
  while I[-1]>0:
    rate = sum(rate_vector)
    # The time is asynchronous.
    # Exponential CDF inverse. 
    tstep = np.log(random.random())/(-rate)
    T.append(T[-1]+tstep)
    # Next, randomly select an event. 
    c_rate = np.cumsum(rate_vector)
    Event = random.random()*rate
    
    if Event <= c_rate[0]: #infection
      # Select a node and update. 
     # ipdb.set_trace()
      node = I_event_list[random.randrange(len(I_event_list))]
      state[node] = 1    
      while node in I_event_list:
        I_event_list.remove(node)
        rate_vector[0] -= tau
      R_event_list.append(node)
      
      rate_vector[1] += gamma
      # Now update the neighbour descriptions.  
      for j in range(len(A_list[node])):
        if state[A_list[node][j]] == 0:
          rate_vector[0] += tau
          I_event_list.append(A_list[node][j])
      # Finally, update the population counters          
      S.append(S[-1]-1)
      I.append(I[-1]+1)
      R.append(R[-1])      

    else: # Recovery
      # Select a node and update.
      #ipdb.set_trace()
      node = R_event_list[random.randrange(len(R_event_list))]
      R_event_list.remove(node)
      state[node] = 2
      rate_vector[1] -= gamma
      # Now update the neighbour descriptions.  
      for j in range(len(A_list[node])):
        if state[A_list[node][j]] == 0:
          rate_vector[0] -= tau
          I_event_list.remove(A_list[node][j])
     # Finally, update the population counters          
      S.append(S[-1])
      I.append(I[-1]-1)
      R.append(R[-1]+1)

  # Convert to uniform timesteps 
  Stemp = S 
  Itemp = I 
  Rtemp = R 
  Ttemp = T  
  S = np.zeros(dpoints,dtype=np.int16)
  I = np.zeros(dpoints,dtype=np.int16)
  R = np.zeros(dpoints,dtype=np.int16)
  T = np.linspace(0,Tend,dpoints)
  j = 0
  for i in range(dpoints):
    while j < len(Ttemp)-1 and Ttemp[j]<T[i]:
      j = j + 1
    S[i] = Stemp[j]
    I[i] = Itemp[j]
    R[i] = Rtemp[j]

  return (S, I, R, T)