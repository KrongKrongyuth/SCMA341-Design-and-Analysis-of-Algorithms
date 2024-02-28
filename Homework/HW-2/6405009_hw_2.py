"""
Homework 2

********** Q1 **********
Quesion/Task -> Write the algorithm that can return binary operation as tree expression.
"""

#Code
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Build_xpression_Tree(expression):
    expression = expression.replace(" ", "")
    if expression[0] == '(' and expression[-1] == ')':
        expression = expression[1:-1]
    
    min_precedence = float('inf')
    split_index = -1
    parentheses_count = 0

    for i in range(len(expression) - 1, -1, -1):
        if expression[i] == ')':
            parentheses_count += 1
        elif expression[i] == '(':
            parentheses_count -= 1
        elif expression[i] in "+-*/" and parentheses_count == 0:
            precedence = Recedence(expression[i])
            if precedence <= min_precedence:
                min_precedence = precedence
                split_index = i

    if split_index == -1:
        return TreeNode(expression)

    operator = expression[split_index]
    left_expression = expression[:split_index]
    right_expression = expression[split_index + 1:]

    root = TreeNode(operator)
    root.left = Build_xpression_Tree(left_expression)
    root.right = Build_xpression_Tree(right_expression)

    return root

def Recedence(operator):
    if operator in "+-":
        return 1
    elif operator in "*/":
        return 2
    return 0

expression = "(((6/2)*7)+(6-2))"
expression_tree = Build_xpression_Tree(expression)

def Display_Expression_Tree(node, k):
    if node != None:
        Display_Expression_Tree(node.right, k + 1)
        print("    " * k, node.value)
        Display_Expression_Tree(node.left, k + 1)

Display_Expression_Tree(expression_tree, 0)

"""
********** Q2 **********
Quesion/Task -> Analyze the structure of recursion: pre and postconditions, sub-instance, recursive invariant, base case, and extra work.

* preconditon is input expression tree.
* postcondition is output numerical value of math expression represented by the tree.
* Sub-instance is half of the input left child and right child.
* Recursive invariant is The function parses the expression by breaking it down into smaller sub-expressions at each recursive call.
* Base case is if the left and right children are empty tree, value is data stored in the node itself.
* Extra work is each recursive call, the function advances the index to keep track of the current position in the expression.
"""

"""
********** Q3 **********
Quesion/Task -> Analyze the time complexity in terms of recurrence relation and estimating domination terms into big-O.

from the T(n) = aT(n/b) + f(n), we have T(n) = 2T(n/2) + n ; a = 2, b = 2, c = 1 and f(n) = n
BIG-O evaluation, logb(a) = log2(2) = 1 = c ---> O(f(n)log(n)) = O(nlog(n))
"""
