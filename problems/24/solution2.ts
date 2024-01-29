// Accepted: 62ms (35.18%), 44.40MB (56.03%)

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

    const left = head;
    const right = head.next;
    left.next = swapPairs(right.next);
    right.next = left;

    return right; // as a new head
};
