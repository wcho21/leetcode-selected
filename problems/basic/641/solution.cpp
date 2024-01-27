// Accepted: 21ms (67.23%), 21.30MB (5.35%)

class MyCircularDeque {
    int internalSize;
    vector<int> array;
    int front;
    int rear;

    int getNextIndex(int i) {
        return (i+1) % internalSize;
    }

    int getPrevIndex(int i) {
        return (i+internalSize-1) % internalSize;
    }

public:
    MyCircularDeque(int k) {
        internalSize = k+1;
        array.resize(internalSize);
        front = 0;
        rear = 0;
    }

    bool insertFront(int value) {
        if (isFull()) {
            return false;
        }

        array[front] = value;
        front = getNextIndex(front);
        return true;
    }

    bool insertLast(int value) {
        if (isFull()) {
            return false;
        }

        rear = getPrevIndex(rear);
        array[rear] = value;
        return true;
    }

    bool deleteFront() {
        if (isEmpty()) {
            return false;
        }

        front = getPrevIndex(front);
        return true;
    }

    bool deleteLast() {
        if (isEmpty()) {
            return false;
        }

        rear = getNextIndex(rear);
        return true;

    }

    int getFront() {
        if (isEmpty()) {
            return -1;
        }

        return array[getPrevIndex(front)];
    }

    int getRear() {
        if (isEmpty()) {
            return -1;
        }

        return array[rear];
    }

    bool isEmpty() {
        return front == rear;
    }

    bool isFull() {
        return getNextIndex(front) == rear;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
