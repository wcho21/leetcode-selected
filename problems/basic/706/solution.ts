// Accepted: 167ms (46.41%), 62.70MB (19.89%)

class Node {
    public key: number;
    public value: number;
    public next: Node | null;
    constructor(key: number = 0, value: number = 0, next: Node | null = null) {
        this.key = key;
        this.value = value;
        this.next = next;
    }
}

class MyHashMap {
    private static readonly size: number = 2047;
    private map: Node[];

    constructor() {
        this.map = Array(MyHashMap.size);
        for (let i = 0; i < MyHashMap.size; ++i) {
            this.map[i] = new Node();
        }
    }

    private getHash(key: number): number {
        return key % MyHashMap.size;
    }

    put(key: number, value: number): void {
        const keyHash = this.getHash(key);
        let node = this.map[keyHash];

        while (node.next !== null) {
            if (key === node.next.key) {
                node.next.value = value;
                return;
            }

            node = node.next;
        }

        node.next = new Node(key, value);
    }

    get(key: number): number {
        const keyHash = this.getHash(key);
        let node = this.map[keyHash];

        while (node.next !== null) {
            if (key === node.next.key) {
                return node.next.value;
            }

            node = node.next;
        }

        return -1;
    }

    remove(key: number): void {
        const keyHash = this.getHash(key);
        let node = this.map[keyHash];

        while (node.next !== null) {
            if (key === node.next.key) {
                node.next = node.next.next;
                return;
            }

            node = node.next;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
