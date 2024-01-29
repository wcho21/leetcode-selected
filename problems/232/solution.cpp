// Accepted: 4ms (6.77%), 7.54MB (14.56%)

class MyStack {
    vector<int> stack;
public:
    void push(int value) {
        stack.push_back(value);
    }

    int pop() {
        int pop = stack.back();
        stack.pop_back();
        return pop;
    }

    int peek() {
        return stack.back();
    }

    int size() {
        return stack.size();
    }
};

class MyQueue {
    MyStack stack1;
    MyStack stack2;
public:
    void push(int x) {
       stack1.push(x); 
    }

    int pop() {
        if (stack2.size() == 0) {
            while (stack1.size() > 0) {
                stack2.push(stack1.pop());
            }
        }

        return stack2.pop();
    }

    int peek() {
        if (stack2.size() == 0) {
            while (stack1.size() > 0) {
                stack2.push(stack1.pop());
            }
        }

        return stack2.peek();
    }

    bool empty() {
        return stack1.size() == 0 && stack2.size() == 0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
