# RegEx_Generator_for_FSM

Program to generate Regular Expressions for some user input finite state machine states and transitions.

Field of interest - Theory of Computation (TOC)

### Aim

    Return back RE equations of all final states of a user provided FSM

### User pre-cautions:
      
      1.enter only distinct state and transition names
        ('q0','q1','q0' -> invalid and error in result)
      2.enter integer values when asked how many states or transitions
        (self explanatory, will be fixed later)

### The code takes care of:
      
      1.proper RE syntax was inserted
      2.no foreign transitions or states are there in local FSM
      3.user receives and stores their own states and transitions variables, making code robust
