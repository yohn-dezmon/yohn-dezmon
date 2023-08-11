# Multidimensional Data, Video 1, Spatial Search Problems

https://www.youtube.com/watch?v=BV9Yi7eAEyY

Hash Table --> hash your keys
Search Tree --> requires that keys can be compared

Data indexed array: (requires that keys are small)
Trie: (if keys are strings) 


Keys are multidiemnsional! 
2D Range Searching:
- how many objects are in the highlighted rectangle 

Nearest Neighbors:
- what is the closest object to the space horse?

Suppose we have a set stored as a hash table.
Hash code of each Body is given below.
How would the nearest space horse be implemented?
What would be the runtime of nearest?

hashCode psuedocode:
    return xPos.hashCode() * 31^4 + yPos.hashCode() * 31^3 +
    xVel.hashCode() * 31^2 + yVel.hashCode() * 31^1 


Oh ok, so multidimensional as in (x, y) axis. 
Each point corresponds to a position on the x and y axis.
Yes... basically that is what people mean.
i.e. that each point maps onto a grid, and has associated metadata.

with a regular hash table, to get the nearest item, you have to 
iterate over every single item (O(N))
The location of each object in that scenario is effectively random.


### Uniform Partitioning 

* create buckets (bins) that are contiguous regions of space
* each (x, y) coordinate corresponds to a given bucket
* you store each bucket as a list 
* you know which bucket an object is in, so you can search for other points nearest to a given point easily within that bucket.
* we can also easily tell which bucket we need to look in when we want to get all points within a square drawn on the grid.

Simplest implementation:
- partition space into uniform rectangular buckets (bins)
- have the container (uniform partitioning table) compute a bucket number...
- each object provides getX() and getY()
- "spatial hashing" ... it's not official... "game dev".

https://youtu.be/Ua7vmGcY3Qg?t=193

still O(N) though, because it is just O(N) / 16 (if you have 16 grids).

### QuadTrees

Search Trees explicitly track the order of items.
(binary search tree is a kind of search tree)
Finding the minimum item in a BST is O(log(N)) time. 
This would be O(N) where N are the keys in a hash table.
**This is an advantage of Search trees over Hash Tables!**

Building Trees of Two Dimensional Data:
- you need an x based tree and a y based tree 
- because you could be less than in one dimension and greater than in another dimension 
- we need a total ordering for our objects
https://youtu.be/VC1kZ42XCkY?t=161




