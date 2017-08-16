#!/usr/bin/env python

import pyexotica as exo
from numpy import array
from numpy import matrix
from pyexotica.publish_trajectory import *
import math

def figureEight(t):
    return array([0.0, math.sin(t * 2.0 * math.pi * 0.5) * 0.1, math.sin(t * math.pi * 0.5) * 0.2, 0.0, 0.0, 0.0])

(sol, prob)=exo.Initializers.loadXMLFull(exo.Setup.getPackagePath('exotica_examples')+'/resources/aico_solver_demo_eight.xml')
# Set UDRF and SRDF file paths (overrides using robot_description)
prob[1]['PlanningScene'][0][1]['URDF'] = exo.Setup.getPackagePath('exotica_examples')+'/resources/lwr_simplified.urdf'
prob[1]['PlanningScene'][0][1]['SRDF'] = exo.Setup.getPackagePath('exotica_examples')+'/resources/lwr_simplified.srdf'

problem = exo.Setup.createProblem(prob)
solver = exo.Setup.createSolver(sol)
solver.specifyProblem(problem)

for t in range(0,problem.T):
    if t<problem.T/5:
        problem.setRho('Frame',0.0,t)
    else:
        problem.setRho('Frame',1e5,t)
        problem.setGoal('Frame',figureEight(t*problem.tau),t)

solution = solver.solve()

plot(solution)


