// Accepted: 0ms (100.00%), 7.29MB (51.84%)

class MyQueue {
    queue<int> queue;
public:
    void push(int value) {
        queue.push(value);
    }

    int pop() {
        int pop = queue.front();
        queue.pop();
        return pop;
    }

    int peek() {
        return queue.front();
    }

    int size() {
        return queue.size();
    }
};

class MyStack {
    MyQueue queue;
public:
    void push(int x) {
        queue.push(x);
        for (int i = 0; i < queue.size()-1; ++i) {
            queue.push(queue.pop());
        }
    }

    int pop() {
        return queue.pop();
    }

    int top() {
        return queue.peek();
    }

    bool empty() {
        return queue.size() == 0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
