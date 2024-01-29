// Accepted: 54ms (59.04%), 42.84MB (55.42%)

class MyQueue {
    private queue: number[];
    private popIndex: number;
    private pushIndex: number;

    constructor() {
        this.queue = [];
        this.popIndex = 0;
        this.pushIndex = 0;
    }

    push(value: number): void {
        this.queue[this.pushIndex++] = value;
    }

    pop(): number {
        return this.queue[this.popIndex++];
    }

    peek(): number {
        return this.queue[this.popIndex];
    }

    size(): number {
        return this.pushIndex - this.popIndex;
    }
}

class MyStack {
    private queue: MyQueue;

    constructor() {
        this.queue = new MyQueue();
    }

    push(x: number): void {
        this.queue.push(x);
        for (let i = 0; i < this.queue.size()-1; ++i) {
            this.queue.push(this.queue.pop())
        }
    }

    pop(): number {
        return this.queue.pop();
    }

    top(): number {
        return this.queue.peek();
    }

    empty(): boolean {
        return this.queue.size() === 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
