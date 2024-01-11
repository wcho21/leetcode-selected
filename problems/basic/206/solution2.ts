// Accepted: 52ms (90.61%), 45.70MB (7.22%)

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
    const reverse = (node: ListNode | null, prev: ListNode | null = null) => {
        if (node === null) {
            return prev;
        }

        const oldNext = node.next;

        node.next = prev; // reverse

        // return the head of the reversed list
        return reverse(oldNext, node);
    }

    return reverse(head);
};
