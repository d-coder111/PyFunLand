'''Missionaries and Cannibals problem:
Three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). The boat cannot cross the river by itself with no people on board.'''
class state:
    def __init__(self,state,b_pos,prev_state,path):
        self.state=state
        self.b_pos=b_pos
        self.prev_state=prev_state
        self.path=path
def next_move(stack):
    if len(stack)==0:
        print("GOAL cannot be reached")
        return
    now=stack[-1]
    stack.pop(-1)
    solve(now,stack)
def check(state):
    for i in state:
        if i[0]>0 and i[0]<i[1]:
            return False
    return True
def solve(curr,stack):
    if curr.state==goal:
        path=curr.path[:]
        path.append(curr.state)
        for i in path:
            k=i[0][0]
            for j in range(3):
                if k>0:
                    print("M",end=" ")
                else:
                    print(" ",end=" ")
                k=k-1
            print(" ",end=" ")
            k=i[0][1]
            for j in range(3):
                if k>0:
                    print("C",end=" ")
                else:
                    print(" ",end=" ")
                k=k-1
            print(" || ",end=" ")
            k=i[1][0]
            for j in range(3):
                if k>0:
                    print("M",end=" ")
                else:
                    print(" ",end=" ")
                k=k-1
            print(" ",end=" ")
            k=i[1][1]
            for j in range(3):
                if k>0:
                    print("C",end=" ")
                else:
                    print(" ",end=" ")
                k=k-1
            print("\n")
        return
    npath=curr.path[:]
    npath.append(curr.state)
    m=0
    if curr.b_pos==1:
        m=1
    if curr.state[m][0]>0:
        ns=[]
        ns_l=[]
        ns_r=[]
        ns_l.append(curr.state[0][0]+curr.b_pos)
        ns_l.append(curr.state[0][1])
        ns_r.append(curr.state[1][0]-curr.b_pos)
        ns_r.append(curr.state[1][1])
        ns.append(ns_l)
        ns.append(ns_r)
        if check(ns) and ns!=curr.prev_state:
           n_state=state(ns,0-curr.b_pos,curr.state,npath)
           stack.append(n_state)
    if curr.state[m][1]>0:
        ns=[]
        ns_l=[]
        ns_r=[]
        ns_l.append(curr.state[0][0])
        ns_l.append(curr.state[0][1]+curr.b_pos)
        ns_r.append(curr.state[1][0])
        ns_r.append(curr.state[1][1]-curr.b_pos)
        ns.append(ns_l)
        ns.append(ns_r)
        if check(ns) and ns!=curr.prev_state:
           n_state=state(ns,0-curr.b_pos,curr.state,npath)
           stack.append(n_state)
    if curr.state[m][0]>0 and curr.state[m][1]>0:
        ns=[]
        ns_l=[]
        ns_r=[]
        ns_l.append(curr.state[0][0]+curr.b_pos)
        ns_l.append(curr.state[0][1]+curr.b_pos)
        ns_r.append(curr.state[1][0]-curr.b_pos)
        ns_r.append(curr.state[1][1]-curr.b_pos)
        ns.append(ns_l)
        ns.append(ns_r)
        if check(ns) and ns!=curr.prev_state:
           n_state=state(ns,0-curr.b_pos,curr.state,npath)
           stack.append(n_state)
    if curr.state[m][0]>1:
        ns=[]
        ns_l=[]
        ns_r=[]
        ns_l.append(curr.state[0][0]+(curr.b_pos*2))
        ns_l.append(curr.state[0][1])
        ns_r.append(curr.state[1][0]-(curr.b_pos*2))
        ns_r.append(curr.state[1][1])
        ns.append(ns_l)
        ns.append(ns_r)
        if check(ns) and ns!=curr.prev_state:
           n_state=state(ns,0-curr.b_pos,curr.state,npath)
           stack.append(n_state)
    if curr.state[m][1]>1:
        ns=[]
        ns_l=[]
        ns_r=[]
        ns_l.append(curr.state[0][0])
        ns_l.append(curr.state[0][1]+(curr.b_pos*2))
        ns_r.append(curr.state[1][0])
        ns_r.append(curr.state[1][1]-(curr.b_pos*2))
        ns.append(ns_l)
        ns.append(ns_r)
        if check(ns) and ns!=curr.prev_state:
           n_state=state(ns,0-curr.b_pos,curr.state,npath)
           stack.append(n_state)
    next_move(stack)
init=[[3,3],[0,0]]
goal=[[0,0],[3,3]]
isp=[[-1,-1],[-1,-1]]
st=state(init,-1,isp,[])
solve(st,[])
