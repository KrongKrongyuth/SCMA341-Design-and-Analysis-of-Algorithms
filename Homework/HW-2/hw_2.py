"""
Homework 2

********** Q1 **********
Quesion/Task -> Write the algorithm that can return binary operation as tree expression.
"""

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class MathematicalExpressionParser():
    """
    Mathematidal expression pareser class
    """
    def __init__(self, input) -> None:
        self.input = input
        self.current_index = self.update_start_index()
        self.head = None

    def update_start_index(self) -> int:
        """
            Update start index for recursive function.
        Returns:
            int: start index for recursive function.
        """
        for index, _ in enumerate(self.input):
            if index != 0 and index != len(self.input) - 1 and self.input[index-1] == ")" and self.input[index+1] == "(":
                start_index = index
        return start_index

    def create_tree(self, root = None, left = None, right = None, current_index = 10):
        """
            Create the tree.
        """
        current_element = self.input[self.current_index]

        if self.head == None:
            self.head = Node(current_element)
            root = self.head

        left = root.left
        right = root.right

        print((root.data, left, right), end = "\n")
        # if current_element not in "()":
        #     left_path = self.create_tree(root = root.left, left = None, right = None, current_index = current_index-1)
        if left == None and current_index > 1:
            # print(self.input[current_index - 1])
            root.left = Node(self.input[current_index - 1])
            return self.create_tree(root = root.left, left = None, right = None, current_index = current_index-1)
        # if right == None and self.current_index < len(self.input) - 1:
        #     current_index += 1
        #     root = right
        #     return self.create_tree(root, left, right)

        return root

if __name__ == "__main__":
    test_case = "(((6/2)*7)+(6-2))"
    Express = MathematicalExpressionParser(test_case)
    print(Express.create_tree())
    # print(Express.head.data, Express.head.left.data, Express.head.right)
