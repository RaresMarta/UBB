#ifndef LAB4_QUEUE_H
#define LAB4_QUEUE_H
#endif //LAB4_QUEUE_H
#include <istream>
#include <ostream>
using namespace std;
typedef int TElem;

class Dequeue {
private:
    int* array;
    int capacity, size;
    void resize();

public:
    // constructor and destructor
    Dequeue(int* array, int capacity, int size);
    ~Dequeue();

    // getters and setters
    int* get_array() const;
    int get_capacity() const;
    int get_size() const;
    void set_array(int* newArray);
    void set_capacity(int newCapacity);
    void set_size(int newSize);

    // queue operations
    void push_front(TElem value);
    void push_back(TElem value);
    int pop_front();
    int pop_back();
    int top() const;
    int back() const;

    // overloading stream insertion and extraction
    friend ostream& operator<<(ostream& os, const Dequeue& deq);
    friend istream& operator>>(istream& is, const Dequeue& deq);

    // copy constructor
    Dequeue(const Dequeue& other);
    // copy assignment operator
    Dequeue& operator=(const Dequeue& other);

};