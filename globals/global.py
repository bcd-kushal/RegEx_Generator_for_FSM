
null_state = chr(198)  
#the lambda of RE


#the next 5 variables store values of RE given by User
state=[]
transition=[]
initial_state=""
final_state=""
eqns={}


#program uses states of a,b,c,.... and 0,1,2,... transitions to be used
states='abcdefghijklmnopqrstuvwxyz'
transitions='0123456789'


#code object stores the same things but masked variations that is used by program
code={
      "eqns":{},
      "state":[],
      "transition":[],
      "initial_state":"",
      "final_state":""
      }


