// Accepted: 47ms (93.75%), 42.90MB (44.53%)

class MyStack {
    private stack: number[];

    constructor() {
        this.stack = [];
    }

    push(value: number): void {
        this.stack.push(value);
    }

    pop(): number {
        const pop = this.stack.pop();
        if (pop === undefined) {
            throw new Error("stack underflow");
        }

        return pop;
    }

    peek(): number {
        const peek = this.stack[this.stack.length-1];
        if (peek === undefined) {
            throw new Error("stack underflow");
        }

        return peek;
    }

    size(): number {
        return this.stack.length;
    }
}

class MyQueue {
    private stack1: MyStack;
    private stack2: MyStack;

    constructor() {
        this.stack1 = new MyStack();
        this.stack2 = new MyStack();
    }

    push(x: number): void {
        this.stack1.push(x);
    }

    pop(): number {
        if (this.stack2.size() === 0) {
            while (this.stack1.size() > 0) {
                this.stack2.push(this.stack1.pop());
            }
        }

        return this.stack2.pop();
    }

    peek(): number {
        if (this.stack2.size() === 0) {
            while (this.stack1.size() > 0) {
                this.stack2.push(this.stack1.pop());
            }
        }

        return this.stack2.peek();
    }

    empty(): boolean {
        return this.stack1.size() === 0 && this.stack2.size() === 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
