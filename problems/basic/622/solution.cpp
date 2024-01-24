// Accepted: 23ms (38.64%), 17.32MB (8.22%)

class MyCircularQueue {
    int internalSize;
    vector<int> array;
    int toPush;
    int toPop;

    int getNextIndex(int i) {
        return (i+1) % internalSize;
    }
    int getPrevIndex(int i) {
        return (i+internalSize-1) % internalSize;
    }

public:
    MyCircularQueue(int k) {
        internalSize = k+1;
        for (int i = 0; i < internalSize; ++i) {
            array.push_back(0);
        }
        toPush = toPop = 0;
    }

    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }

        array[toPush] = value;
        toPush = getNextIndex(toPush);
        return true;
    }

    bool deQueue() {
        if (isEmpty()) {
            return false;
        }

        toPop = getNextIndex(toPop);
        return true;
    }

    int Front() {
        if (isEmpty()) {
            return -1;
        }

        return array[toPop];
    }

    int Rear() {
        if (isEmpty()) {
            return -1;
        }

        int rear = getPrevIndex(toPush);
        return array[rear];
    }

    bool isEmpty() {
        return toPush == toPop;
    }

    bool isFull() {
        return getNextIndex(toPush) == toPop;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
