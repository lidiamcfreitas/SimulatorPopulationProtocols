#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*--------------------------------------------------------------------
| Definitions
---------------------------------------------------------------------*/

#define MAXNODES        4 // numero maximo de nos
#define EXPERIMENTS     2 // numero de experiencias
#define RUNS_PER_EXP    10 // numero de vezes que corre
#define ROUNDS_PER_RUN  10

#define MAXNODEVAL      200

typedef struct t_node {
  int my_val;
} Node;


/*--------------------------------------------------------------------
| Global Variables
---------------------------------------------------------------------*/

Node nodes[MAXNODES]; // vector of nodes

/*--------------------------------------------------------------------
| macro getmax(x,y)
---------------------------------------------------------------------*/

#define getmax(x,y) (x>y?x:y)

/*--------------------------------------------------------------------
| Function select_random_int (returns random value in [0,maxvalue-1])
---------------------------------------------------------------------*/

int select_random_int (int maxvalue) {
  long l = random ();
  double ll = (double) l / (double) RAND_MAX * maxvalue;
  int result  = (int) ll;

  return result;
}

/*--------------------------------------------------------------------
| Function initnodes
---------------------------------------------------------------------*/

void* initnodes (int experiment) {
  int  *max_in_network = (int*) malloc (sizeof(int));
  int  i;
  int  randval;

  switch (experiment) {
  case 0:
    // all nodes with the same random value
    randval = select_random_int (MAXNODEVAL);
    *max_in_network = randval;
    for (i=0; i<MAXNODES; i++)
      nodes[i].my_val = randval;
    return (void*) max_in_network;
  case 1:
    // all nodes with a different value
    *max_in_network = 0;
    for (i=0; i<MAXNODES; i++) {
      randval = select_random_int (MAXNODEVAL);
      *max_in_network = getmax (*max_in_network, randval);
      nodes[i].my_val = randval;
    }
    return (void*) max_in_network;
  default:
    return 0;
  }
  return 0;
}

/*--------------------------------------------------------------------
| Function assert
---------------------------------------------------------------------*/

int assert (void* inistate) {
  if (inistate) {
    int  max_in_network = *((int*)inistate);
    int  i;

    free (inistate);
    for (i=0; i<MAXNODES; i++) {
      if (nodes[i].my_val != max_in_network)
	return 0;
    }
    return 1;
  }
  return 0;
}

/*--------------------------------------------------------------------
| Function dumpstates
---------------------------------------------------------------------*/

void dumpstates () {
  int  i;
  
  for (i=0; i<MAXNODES; i++) 
    printf ("----Node[%i].my_val=%d;\n", i, nodes[i].my_val);
}

/*--------------------------------------------------------------------
| Function encounter
---------------------------------------------------------------------*/

void encounter (int i, int j) { // nodes[i] encounters nodes[j], it's directioned
  nodes[i].my_val =  getmax (nodes[i].my_val,nodes[j].my_val);
}

/*--------------------------------------------------------------------
| Function select_random_node
---------------------------------------------------------------------*/

int select_random_node () {
  return select_random_int (MAXNODES);
}

/*--------------------------------------------------------------------
| Main
---------------------------------------------------------------------*/

int main () {
  int  experiment;
  int  seed = time(NULL);

  srandom ((unsigned) seed);
  
  printf ("STARTING %d experiments, %d runs each\n", EXPERIMENTS, RUNS_PER_EXP);
  for (experiment=0; experiment<EXPERIMENTS; experiment++) {
    int  run;
    
    for (run=0; run<RUNS_PER_EXP; run++) {
      int    round;
      void*  inistate;

      inistate = initnodes (experiment);
      for (round=0; round<ROUNDS_PER_RUN; round++) {
	int i = select_random_node ();
	int j = select_random_node ();
	encounter (i, j);
      }
      if (assert (inistate))
	printf ("--Experiment %d, run %d, OK\n", experiment, run);
      else 
	printf ("--Experiment %d, run %d, FAILED\n", experiment, run);
      dumpstates ();
    }
  } 
  printf ("DONE.\n");
}

