// Accepted: 92ms (78.86%), 48.25MB (57.50%)

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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let l1Head = l1;
    let l2Head = l2;

    // swap if l2 is longer
    while (l1 !== null && l2 !== null) {
        l1 = l1.next;
        l2 = l2.next;
    }
    if (l1 === null && l2 !== null) {
        let temp = l1Head;
        l1Head = l2Head;
        l2Head = temp;
    }

    l1 = l1Head;
    l2 = l2Head;

    // add l2 numbers to l1 numbers
    let carry = 0;
    while (l1 !== null || l2 !== null) {
        // add
        let added = 0;
        added += l1!.val;
        if (l2 !== null) {
            added += l2.val;
        }
        added += carry;
        carry = 0;

        // update node and carry
        l1!.val = added % 10;
        carry = Math.floor(added / 10);

        // advance
        l1 = l1!.next;
        if (l2 !== null) {
            l2 = l2.next;
        }
    }

    if (carry === 0) {
        return l1Head;
    }

    // append carry node if nonzery carry
    l1 = l1Head;
    while (l1 !== null && l1.next !== null) {
        l1 = l1.next;
    }
    l1!.next = new ListNode(carry);

    return l1Head;
};
