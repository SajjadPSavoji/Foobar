# final solution
def solution(h, q):
    parents = []
    for idx in q:
      max_idx = 2**h - 1
      if max_idx < idx:
          return -1
      else:
          node_offset = 0
          continue_flag = True
          subtree_size = max_idx
          result = -1
          while continue_flag:
              if subtree_size == 0:
                  continue_flag = False
              subtree_size = subtree_size >> 1
              left_node = node_offset + subtree_size
              right_node = left_node + subtree_size
              my_node = right_node + 1
              if (left_node == idx) or (right_node == idx):
                  result = my_node
                  continue_flag = False
              if (idx > left_node):
                  node_offset = left_node
          parents.append(result)

    return parents