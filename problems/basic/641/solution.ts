// Accepted: 109ms (66.67%), 60.58MB (9.52%)

class MyCircularDeque {
    private internalSize: number;
    private array: number[];
    private front: number;
    private rear: number;

    constructor(k: number) {
        this.internalSize = k+1;
        this.array = new Array(k+1).fill(0);
        this.front = 0;
        this.rear = 0;
    }

    private getNextIndex(i: number) {
        return (i+1) % this.internalSize;
    }

    private getPrevIndex(i: number) {
        return (i+this.internalSize-1) % this.internalSize;
    }

    insertFront(value: number): boolean {
        if (this.isFull()) {
            return false;
        }

        this.array[this.front] = value;
        this.front = this.getNextIndex(this.front);
        return true;
    }

    insertLast(value: number): boolean {
        if (this.isFull()) {
            return false;
        }

        this.rear = this.getPrevIndex(this.rear);
        this.array[this.rear] = value;
        return true;
    }

    deleteFront(): boolean {
        if (this.isEmpty()) {
            return false;
        }

        this.front = this.getPrevIndex(this.front);
        return true;
    }

    deleteLast(): boolean {
        if (this.isEmpty()) {
            return false;
        }

        this.rear = this.getNextIndex(this.rear);
        return true;
    }

    getFront(): number {
        if (this.isEmpty()) {
            return -1;
        }

        const front = this.getPrevIndex(this.front);
        return this.array[front];
    }

    getRear(): number {
        if (this.isEmpty()) {
            return -1;
        }

        return this.array[this.rear];
    }

    isEmpty(): boolean {
        return this.front === this.rear;
    }

    isFull(): boolean {
        return this.getNextIndex(this.front) === this.rear;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */
