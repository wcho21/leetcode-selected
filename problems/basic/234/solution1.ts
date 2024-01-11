// Accepted: 119ms (45.53%), 85.15MB (46.34%)

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

function isPalindrome(head: ListNode | null): boolean {
    const vals: number[] = [];
    for (let node = head; node !== null; node = node.next) {
        vals.push(node.val);
    }

    for (let i = 0; i < Math.floor(vals.length/2); ++i) {
        if (vals[i] !== vals[vals.length-i-1]) {
            return false;
        }
    }
    return true;
};
