# Trees

One example of data abstraction is with **trees**.

In computer science, **trees** are recursive data structures that are widely used in various settings and can be implemented in many ways. The diagram below is an example of a tree.
![[chrome_Ngz3oz7i7s.png]]

Notice that the tree branches downward. In computer science, the **root** of a tree starts at the top, and the **leaves** are at the bottom.

Some terminology regarding trees:

-   **Parent Node**: A node that has at least one branch.
-   **Child Node**: A node that has a parent. A child node can only have one parent.
-   **Root**: The top node of the tree. In our example, this is the `1` node.
-   **Label**: The value at a node. In our example, every node's label is an integer.
-   **Leaf**: A node that has no branches. In our example, the `4`, `5`, `6`, `2` nodes are leaves.
-   **Branch**: A subtree of the root. Trees have branches, which are trees themselves: this is why trees are _recursive_ data structures.
-   **Depth**: How far away a node is from the root. We define this as the number of edges between the root to the node. As there are no edges between the root and itself, the root has depth 0. In our example, the `3` node has depth 1 and the `4` node has depth 2.
-   **Height**: The depth of the lowest (furthest from the root) leaf. In our example, the `4`, `5`, and `6` nodes are all the lowest leaves with depth 2. Thus, the entire tree has height 2.
- 
## Working with Trees

A tree has both a value for the root node and a sequence of branches, which are also trees. In our implementation, we represent the branches as a list of trees. Since a tree is a data abstraction, our choice to use lists is just an implementation detail.

-   The arguments to the constructor `tree` are the value for the root node and an optional list of branches. _If no branches parameter is provided, the default value `[]` is used._
-   The selectors for these are `label` and `branches`.

Remember `branches` returns a list of trees and not a tree directly. It's important to distinguish between working with a tree and working with a **list of** trees.

We have also provided a convenience function, `is_leaf`.

Let's try to create the tree from above:

```
t = tree(1,
      [tree(3,
          [tree(4),
           tree(5),
           tree(6)]),
      tree(2)])
```