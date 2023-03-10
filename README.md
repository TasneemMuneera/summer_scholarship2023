# A constraint-based local search library for Python

We have tried to create a local search library written in python with an aim of solving puzzle problems (eg: Magic-square , N-queen, etc.).  This library is not written to solve only a specific problem, rather it's written generally for all the puzzle problems. Due to the limitation of time, we have only showed an example of solving a 3x3 Magic-square based on random-walk search algorthim with our library. This project can be further developed by adding more features and search algorithms (eg: hill-climbing) in future. 

Currently, this repository has three versions on three branches. 
- Master
- 2nd_version
- third_version

Other than these three, a main branch is here for a readme file for the description of the entire project.

### Master branch:
This branch is consists of the first version of the project. We have created the search propagation tree for N numbers of independent variables and the nodes dependent of them.

A search propagation tree can be created by initialising the independent variables. A user can initialise the variables by assigning random values of a given range. Later, there are "Create_sum()" and "Create_product()" expression classes so that the user have the option to create the tree by using only sum, only product or a mixture of them. An example of search propagation tree is shown in Figure: 1.

<p align="center">
<img src="331434010_1258854395046835_4817167728494435071_n.jpg" width="400" height="400">
</p>
<p align ="center">
Figure 1: Search Propagation Tree
</p>

#### Issues: 
- This version of the project successfully generated the search propagation tree with the ability to update the tree, but here we can update the tree by changing only one independent. Moreover, the change is not permanent for the update. Therefore, if we update an independent again, it will update its value based on the values that were used for the initialisation of the tree. It will not change its value based on the first update. 
- This version only works when the upper nodes of the tree only depend on parameters that are just below them. If the upper nodes are dependent on the parameters that are not on the same level, the update function becomes faulty, because we did not assign any levels when creating the tree for this version. As a result, when it is time to update, the parameters do not maintain sequence. 

### 2nd_version :
In this version, we have fixed the first issue of the Master branch by assigning a global clock and self-clock for the variables. Each time, if a variable is updated or not can be known by comparing the clocks. By doing this, now it can update as many variables as we need and as many times. Moreover,  to solve the second issue of the Master branch, we have assigned levels to each node and variable. But the total issue is not solved in this branch. 

### third_version :
Here, we have totally fixed the update issue by assigning level by level in a 2d_array. Now, it can update properly even if the parameters of a node are sitting on different levels and we can update the tree by changing variables as much as we need. 
After that, we have written random-walk search algorithm and showed an example of solving 3x3 Magic_square. 



