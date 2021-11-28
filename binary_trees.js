
//Create a class to represent a node in a binary tree
///////////////////////////////////
class Node {
    constructor(val) {
         this.val   = val;
         this.left  = null;
         this.right = null;
    }
}

//Shape of tree
//////////////////////////////////
    //     a
    //    / \
    //   b   c
    //  / \   \
    // d   e   f 


//Build the above tree
/////////////////////////////////
const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;


//Depth first traversal
/////////////////////////////////
const depthFirstValues = (root) => {
    //Check if root in null if true return empty array
    if(root == null) return [];

    const result = [];
    const stack = [root]
    //While nodes are on the stack keep iterating
    while (stack.length > 0) {
        //Remove top node from the stack
        const current = stack.pop();
        //Store current node value in an array
        result.push(current.val)
        
        //If child nodes add them to the stack 
        if (current.right) stack.push(current.right);
        if (current.left) stack.push(current.left);
    };
    console.log(result)
};

//depthFirstValues([]);


//Depth first traversal recusively 
/////////////////////////////////////////
const depthFirstValuesRecursive = (root) => {
    if (root == null) return [];
    console.log(root.val)
    const leftValues = depthFirstValuesRecursive(root.left);
    const rightValues = depthFirstValuesRecursive(root.right);  
    return [root.val, ...leftValues, ...rightValues]
};

//depthFirstValuesRecursive(root=a);


//Breadth first traversal
///////////////////////////////////////
const breathFirstValues  = (root) => {
    if (root == null) return [];

    result = [];
    const queue = [root];
    while (queue.length > 0){
        //Remove/return index 0 of the queue
        const current = queue.shift();
        result.push(current.val)
        
        if (current.left) queue.push(current.left);
        if (current.right) queue.push(current.right);
    };
    console.log(result)
};
//breathFirstValues(a)


//Find a target node with breadth first 
//////////////////////////////////////////////
const treeSearch = (root, target) => {
    if (root == null) return false;

    result = [];
    const queue = [root];
    while (queue.length > 0){
        //Remove/return index 0 of the queue
        const current = queue.shift();
        console.log(current.val)
        if (current.val == target) return true;
        result.push(current.val)
        
        if (current.left) queue.push(current.left);
        if (current.right) queue.push(current.right);
    };
    return false;
};
// console.log(treeSearch(root=a, target='e'))
// console.log(treeSearch(a, 'g'))


//tree search with depth first 
////////////////////////////////////////////////////
const treeIncludes = (root, target) => {
    if (root == null) return false;
    if (root.val == target) return true;
    return treeIncludes(root.left, target) || treeIncludes(root.right, target);
};
//console.log(treeIncludes(root=a, target='e'))


//Shape of tree
//////////////////////////////////////////////
    //     3
    //    / \
    //   11  4
    //  / \   \
    // 4   2   1 


//Build the above tree
///////////////////////////////////////////////
const first     = new Node(3);
const second    = new Node(11);
const third     = new Node(4);
const fourth    = new Node(4);
const fifth     = new Node(2);
const sixth     = new Node(1);

first.left      = second;
first.right     = third;
second.left     = fourth;
second.right    = fifth;
third.right     = sixth;

//Sum of tree depth first
/////////////////////////////////////////////////////
const treeSum = (root) => {
if (root == null) return 0;
return root.val + treeSum(root.left) + treeSum(root.right)
};
//console.log(treeSum(first))

//Sum of tree breadth first
/////////////////////////////////////////////////////
const sumTree = (root) => {
    if (root == null) return 0;

    let sum = 0;
    const queue = [root];
    while (queue.length > 0){
         const current = queue.shift();
         sum += current.val;
        
         if (current.left) queue.push(current.left);
         if (current.right) queue.push(current.right);
    };
    return sum
};
//console.log(sumTree(first))


//Tree min value depth first
///////////////////////////////////////////////////////
const treeMin = (root) => {
    let smallest = Infinity;
    const stack = [root];
    while (stack.length > 0){
        const current = stack.pop();
        if (current.val < smallest) smallest = current.val;
        
        if (current.left) stack.push(current.left);
        if (current.right) stack.push(current.right);
    };
    return smallest;
};
//console.log(treeMin(first))


//Tree min breadth first
////////////////////////////////////////////////////////
const minTree = (root) => {
    let smallest = Infinity;
    const queue = [root];
    while (queue.length > 0){
        const current = queue.shift();
        if (current.val < smallest) smallest = current.val;
        
        if (current.left) queue.push(current.left);
        if (current.right) queue.push(current.right);
    };
    return smallest;
};
//console.log(minTree(first))


//Tree min recursive
////////////////////////////////////////////////////////
const treeMinRec= (root) => {
    if (root == null) return Infinity;
    const leftMin = treeMinRec(root.left);
    const rightMin = treeMinRec(root.right);
    return Math.min(root.val, leftMin, rightMin)
};
//console.log(treeMinRec(first));


//Longest path(max root to leaf)
//////////////////////////////////////////////////////////
const longestPath = (root) => {
    if (root == null) return -Infinity;
    if (root.left == null && root.right == null) return root.val;
    const maxChildPathSum = Math.max(longestPath(root.left), longestPath(root.right));
    return root.val + maxChildPathSum;
};
console.log(longestPath(first))
