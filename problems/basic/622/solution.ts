// Accepted: 89ms (97.74%), 50.06MB (91.73%)

class MyCircularQueue {
    private internalSize: number;
    private array: number[];
    private toPush: number;
    private toPop: number;

    constructor(k: number) {
        this.internalSize = k+1;
        this.array = Array(this.internalSize).fill(0);
        this.toPush = this.toPop = 0;
    }

    private getNextIndex(i: number): number {
        return (i+1) % this.internalSize;
    }

    private getPrevIndex(i: number): number {
        return (i+this.internalSize-1) % this.internalSize;
    }

    enQueue(value: number): boolean {
        if (this.isFull()) {
            return false;
        }

        this.array[this.toPush] = value;
        this.toPush = this.getNextIndex(this.toPush);
        return true;
    }

    deQueue(): boolean {
        if (this.isEmpty()) {
            return false;
        }

        this.toPop = this.getNextIndex(this.toPop);
        return true;
    }

    Front(): number {
        if (this.isEmpty()) {
            return -1;
        }

        return this.array[this.toPop];
    }

    Rear(): number {
        if (this.isEmpty()) {
            return -1;
        }

        const rear = this.getPrevIndex(this.toPush);
        return this.array[rear];
    }

    isEmpty(): boolean {
        return this.toPush === this.toPop;
    }

    isFull(): boolean {
        return this.getNextIndex(this.toPush) === this.toPop;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
