// Accepted: 120ms (58.02%), 61.35MB (5.41%)

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    const queue = new MinPriorityQueue();

    for (let node of lists) {
        while (node !== null) {
            queue.enqueue(node.val);
            node = node.next;
        }
    }

    const mergedHead = new ListNode();
    let cur = mergedHead;
    while (!queue.isEmpty()) {
        const val = queue.dequeue().element;
        cur.next = new ListNode(val);
        cur = cur.next;
    }

    return mergedHead.next;
};
