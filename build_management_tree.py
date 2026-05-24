class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    '''
    Returns level of the tree node
    
    '''
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    '''Prints tree node with name and designation'''
    def print_tree(self, type, level=3):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        data = self.name + ' (' + self.designation  + ')'
        if type == "name":
            data = self.name
        elif type == "designation":
            data = self.designation
        print(prefix + data)
        if self.children:
            for child in self.children:
                child.print_tree(type, level)

    '''Adds child node to tree'''
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
'''Build management tree'''
def build_management_tree():
    management_tree = TreeNode("Nilpul","CEO")

    level_1_tree_1 = TreeNode("Chinmay","CTO")
    level_1_tree_2 = TreeNode("Gels", "HR Head")

    level_2_tree_1 = TreeNode("Vishwa","Infrastructure Head")
    level_3_tree_1 = TreeNode("Dhaval","Cloud Manager")
    level_3_tree_2 = TreeNode("Abhijit", "App Manager")
    level_2_tree_1.add_child(level_3_tree_1)
    level_2_tree_1.add_child(level_3_tree_2)

    level_2_tree_2 = TreeNode("Aamir", "Application Head")
    level_1_tree_1.add_child(level_2_tree_1)
    level_1_tree_1.add_child(level_2_tree_2)

    level_2_tree_1 = TreeNode("Peter","Recruitement Manager")
    level_2_tree_2 = TreeNode("Waqas","Policy Manager")
    level_1_tree_2.add_child(level_2_tree_1)
    level_1_tree_2.add_child(level_2_tree_2)

    management_tree.add_child(level_1_tree_1)
    management_tree.add_child(level_1_tree_2)

    return management_tree

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
    root_node.print_tree("name",0)
