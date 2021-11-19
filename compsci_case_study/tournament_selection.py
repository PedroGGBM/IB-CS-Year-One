#tournament selection
import random 

def tournament_selection(k,total_pop):
    best = None 
    for i in range(1, k):
        ind = random.choice(total_pop)
        if (best == None) or fitness(ind) > fitness(best): #if fitness function in place
            best = ind
    return best

func tournament_selection(pop, k):
    best = null
    for i=1 to k
        ind = pop[random(1, N)]
        if (best == null) or fitness(ind) > fitness(best)
            best = ind
    return best 
