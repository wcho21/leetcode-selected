// Accepted: 50ms (88.69%), 44.82MB (7.04%)

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

function swapPairs(head: ListNode | null): ListNode | null {
    if (head === null || head.next === null) {
        return head;
    }

    const dummyHead = new ListNode(0, head);

    let prev = dummyHead;
    let left = head;
    let right = head.next;

    while (true) {
        // swap
        const oldRightNext = right.next;
        prev.next = right;
        right.next = left;
        left.next = oldRightNext;

        if (oldRightNext === null || oldRightNext.next === null) {
            break;
        }

        // advance
        prev = left;
        left = oldRightNext;
        right = oldRightNext.next;
    }

    return dummyHead.next;
};
