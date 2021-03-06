#!/usr/bin/env python
"""
NAME: Mengtao Xu
Assignment 1
CS440 / CS640 Artificial Intelligence
"""

import argparse
import random
import search
import time


class BinaryTreeProblem(search.Problem):
  """A search problem laid out as a binary tree."""

  def __init__(self, depth, goal):
    # FIXME implement me!
    self.depth = depth
    self.goal = goal
    self.initial = 1

  def actions(self, state):
    # FIXME implement me
    # non-leaf nodes can expand in left and right 
    if state < 2 ** (self.depth-1):
      return ['L', 'R']
    # leaf nodes with states do not have actions
    else:
      return []

  def result(self, state, action):
    # FIXME implement me
    # state number of left child is twice the state number of the parent
    if action == 'L':
      return state*2
    # state number of right child is twice the state number of the parent plus 1
    else:
      return state*2+1




def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--num_trials', default=10, type=int)
  parser.add_argument('--max_depth', default=10, type=int)
  args = parser.parse_args()
  print 'Metric,Average,BFS,IDS,DFS'
  for depth in range(1, args.max_depth):
    trees = [BinaryTreeProblem(depth, random.randint(2 ** (depth - 1),
                                                     2 ** depth - 1))
             for _ in range(args.num_trials)]
    average_memories = []
    average_times = []
    for search_algorithm in (search.breadth_first_tree_search,
                             search.iterative_deepening_search,
                             search.depth_first_tree_search):
      total_memory = 0
      start_time = time.time()
      for tree in trees:
        total_memory += search_algorithm(tree)
        search_algorithm(tree)
      end_time = time.time()
      average_times.append('%.6f' % ((end_time - start_time) / args.num_trials))
      average_memories.append('%.1f' % (total_memory / float(args.num_trials)))
    print ','.join(['time', str(depth)] + average_times)
    print ','.join(['memory', str(depth)] + average_memories)

if __name__ == '__main__':
  main()
