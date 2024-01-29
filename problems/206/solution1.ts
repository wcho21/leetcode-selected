// Accepted: 52ms (90.52%), 45.53MB (10.71%)

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

function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    let cur: ListNode | null = head;

    while (cur !== null) {
        const oldPrev = prev;

        prev = cur;
        cur = cur.next;

        prev.next = oldPrev;
    }

    return prev;
};
