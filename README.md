The Poor Linear Probing hash table worked the worst of all. It had the worst time to build and had an incredibly large amount of collisions.
However, It did utalize a lot of the space with minimal wasted space.

The Poor Linked List was the second worst. It was about twice as fast as the linear probing, but it still had a ton of collisons and by far the 
most amount of wasted space with almost the whole table being empty.

The Good Linear Probing was in 3rd place. it preformed significantly better than the other attempts and had a significant reduction in collisions.
Despite the linear probing method having much less wasted space than the Linked list. I chose this as third instead of second as I prioritized 
table build time over wasted space.

The Good Linked List was in 2nd place. It preformed very similarly to the linear probing method however it had more wasted space. Despite this
it took less time to create the table as previously mentioned so it was ranked higher. These places can be easily switched if wasted space was 
a greater priority for the user.

The Best approach was a Linked List. A Linked List was chosen to optimize for the reasons previously mentioned. The optimization to the hash function
make this approach even faster than the Good Linked List. It did, however, leave the collisions and wasted space still around the same.


The 3 final methods were the most effective because the hash function was much more evenly distributed. The poor hash function makes all the keys the same
meaning they would go into the same location causing a ton of collisions and lots of wasted space for the linked list. The better hash function attempts to evenly distribute the keys as mentioned in order to minimize collisions and use as much of the space as possible.