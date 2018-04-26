# Data Structures Fun!

This is a repository meant to help people learn more about common Computer Science related Data Structures. Concepts, descriptions, and implementations (in Python and JavaScript) will be presented to any and all interested. Whether you're new to programming or a seasoned veteran, you're welcome to explore this repository to sharpen your understanding of Computer Science's most popular Data Structures. Let's get coding!

### The Abstract Data Type (ADT) - A Brief Introduction

In the wonderful world of programming and Computer Science, the term 'Data Structures' is pretty common. There are a few different types of Data Structures, and although this repository will ultimately refer to every type at various points, the type that this respository is mainly concerned with is called an Abstract Data Type (ADT).

Wikipedia defines an ADT as: "a mathematical model for data types, where a data type is defined by its behavior (semantics) from the point of view of a user of the data"<sup>1</sup>. Another way to describe an ADT is: a set of data values and associated operations that are precisely specified independent of any particular implementation.

###### Why should you take the time to learn this stuff?

If you're new to Data Structures you may be saying to yourself "But wait, don't languages like JavaScript already have built-in things like arrays and objects to house data? So why would anyone need to learn about Absract Data Types?". This is a great point! Many (if not *all*) programming languages utilize  built-in data structures with which to store data. So why learn how to implement an ADT?

There are a few reasons to learn about Abstract Data Types.

The first has to do with something called **Time/Space Complexity** and/or **Big-O Notation**. In programming, an ADT can be used to house data of all kinds and, depending on the specific ADT, can be used to *create faster and/or more memory efficient ways to access that data when needed*. Applied at a grand scale, even minor increases in efficiency can result in *millions* of dollars saved by large tech companies; so there's an enormous amount to gain from knowing your Data Structures!

The second has to do with pure academics. In programming, basic knowledge of Data Structures is a fairly large expectation even if actual implementations aren't used. Knowing how to implement an ADT will:
1. Strengthen your understanding of the language you choose to implement it in.
2. Solidify basic Computer Science concepts.
3. Greatly help you during potential whiteboard interviews.
4. Give you the ability to, at any time, impress your friends and family with fancy nerd-talk.

###### Quick example of an ADT

A great starting example of an ADT is a **Singly Linked List** (*which we will explore in much greater depth later on*). Although it can be implemented in many ways, a proper Singly Linked List must support a few basic operations and must possess certain attributes. Check out the code below.

```python
# Singly Linked List

[ 1 ] -> [ 2 ] -> [ 3 ] -> None
  |             |           |
#Node        Pointer       End
```

Above is a visual representation of what a Singly Linked List might look like in Python. The square brackets containing the number one ```[ 1 ]``` represent a key attribute of a Singly Linked List: a **Node**, which is a structure that houses a piece of data. Singly Linked Lists are built by linking one or more of these Nodes together by using **pointers**, which are represented in the above example by the ```->``` symbols. The last node in our example is the ```[ 3 ]``` above, which has a pointer that points to ```None```. This shows another common aspect of Singly Linked Lists. The last Node must always point to "nothing" which signifies the end of the list. This can be implemented in Python by ensuring that the last Node is always pointing to ```None```, and similarly in JavaScript by pointing instead to ```null```.

### Data Structures Quick Info Table
| Name | Big-O Lookup/Search |
| :-------------: | :-------------: |
| Singly Linked List | O(n) |
| Doubly Linked List | O(n) |

### Data Structures List

#### Doubly Linked List

**Overview**

**References:**
- 1 - [Wikipedia](https://en.wikipedia.org/wiki/Abstract_data_type)
