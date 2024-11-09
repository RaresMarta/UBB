    #include "SMIterator.h"
    #include "SortedMap.h"
    #include <exception>
    #include <stdexcept>

    using namespace std;


    /// 0(CAP)
    SortedMap::SortedMap(Relation r): root(-1), pairs(0), rel(r) {
        for (int i = 0; i < CAP; ++i) {
            nodes[i] = Node();
        }
    }


    /// O(tree height)
    TValue SortedMap::add(TKey k, TValue v) {
        /// If the key already exists in the map then its value is replaced by the new value and the old value is returned
        /// If the key does not exist, a new pair is added and the value null is returned
        int current = root;
        int prev = -1;
        bool leftChild = false;

        while (current != -1) {
            if (nodes[current].key == k) {
                // key exists, replace value and return old one
                TValue oldValue = nodes[current].value;
                nodes[current].value = v;
                return oldValue;
            }
            prev = current;
            // traverse tree based on key relation
            if (rel(k, nodes[current].key)) {
                current = nodes[current].left;
                leftChild = true;
            } else {
                current = nodes[current].right;
                leftChild = false;
            }
        }
        Node newNode = Node(k, v);
        int freeIndex = findFreeIndex();
        if (freeIndex == -1)
            throw std::overflow_error("No space left in the SortedMap");

        nodes[freeIndex] = newNode;
        // if tree is empty add new node as root
        if (prev == -1) {
            root = freeIndex;
        }
        // otherwise, insert new node as one of the children of 'prev'
        else {
            if (leftChild) {
                nodes[prev].left = freeIndex;
            } else {
                nodes[prev].right = freeIndex;
            }
        }
        pairs++;
        return NULL_TVALUE;
    }


    /// O(tree height)
    TValue SortedMap::search(TKey k) const {
        /// searches for the key and returns its value if the map contains the key or NULL_TVALUE otherwise
        int current = root;
        while (current != -1) {
            if (nodes[current].key == k)
                return nodes[current].value;

            if (rel(k, nodes[current].key)) {
                current = nodes[current].left;
            } else {
                current = nodes[current].right;
            }
        }
        return NULL_TVALUE;
    }


    /// O(tree height)
    TValue SortedMap::remove(TKey k) {
        /// removes a key from the map and returns its value if the key existed or NULL_TVALUE otherwise
        int current = root;
        int prev = -1;
        bool leftChild = false;

        // search for the key
        while (current != -1 && nodes[current].key != k) {
            prev = current;
            if (rel(k, nodes[current].key)) {
                current = nodes[current].left;
                leftChild = true;
            } else {
                current = nodes[current].right;
                leftChild = false;
            }
        }

        // key wasn't found
        if (current == -1)
            return NULL_TVALUE;

        TValue value = nodes[current].value;
        // no children
        if (nodes[current].left == -1 && nodes[current].right == -1) {
            if (prev == -1)
                root = -1;
            else {
                if (leftChild) {
                    nodes[prev].left = -1;
                } else {
                    nodes[prev].right = -1;
                }
            }
            nodes[current].used = false;
            nodes[current].key = nodes[current].value = NULL_TVALUE;
        }
        // one child
        else if (nodes[current].left == -1 || nodes[current].right == -1) {
            // one child
            int childIndex = (nodes[current].left != -1) ? nodes[current].left : nodes[current].right;
            if (prev == -1)
                root = childIndex;
            else {
                if (leftChild) {
                    nodes[prev].left = childIndex;
                } else {
                    nodes[prev].right = childIndex;
                }
            }
            nodes[current].used = false;
            nodes[current].key = nodes[current].value = NULL_TVALUE;
        }
        // two children
        else {
            int successor, successorParent;
            // successor will be the min node in the right subtree
            findMinNode(nodes[current].right, successor, successorParent);
            // replace current node's element with successor's element
            nodes[current].key = nodes[successor].key;
            nodes[current].value = nodes[successor].value;

            if (successorParent != current) {
                nodes[successorParent].left = nodes[successor].right;
            } else {
                nodes[successorParent].right = nodes[successor].right;
            }
            nodes[successor].used = false;
            nodes[successor].key = nodes[successor].value = NULL_TVALUE;
        }
        pairs--;
        return value;
    }


    /// 0(1)
    int SortedMap::size() const {
        return pairs;
    }


    /// 0(1)
    bool SortedMap::isEmpty() const {
        return pairs == 0;
    }


    /// 0(1)
    SMIterator SortedMap::iterator() const {
        return SMIterator(*this);
    }


    /// 0(CAP)
    SortedMap::~SortedMap() {
        for (int i = 0 ; i < CAP; ++i) {
            nodes[i].key = nodes[i].value = NULL_TVALUE;
            nodes[i].right = nodes[i].left = -1;
            nodes[i].used = false;
        }
        pairs = 0;
        root = -1;
    }


    /// O(CAP
    int SortedMap::findFreeIndex() {
        /// find first empty position
        for (int i = 0; i < CAP; ++i)
            if (!nodes[i].used)
                return i;
        return -1;
    }


    /// 0(height(start))
    void SortedMap::findMinNode(int start, int &min, int &minParent) {
        /// find smallest node in a subtree
        int current = start;
        int prev = -1;
        while (nodes[current].left != -1) {
            prev = current;
            current = nodes[current].left;
        }
        min = current;
        minParent = prev;
    }

    /// O(tree height)
    void SortedMap::replace(TKey k, TValue oldValue, TValue newValue) {
        if (search(k) != oldValue)
            return;

        int current = root;
        while (current != -1) {
            if (nodes[current].key == k) {
                if (nodes[current].value == oldValue)
                    nodes[current].value = newValue;
                else
                    return;
            }
            if (rel(k, nodes[current].key)) {
                current = nodes[current].left;
            } else {
                current = nodes[current].right;
            }
        }
    }
