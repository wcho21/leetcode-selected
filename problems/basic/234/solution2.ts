// Accepted: 101ms (87.63%), 63.32MB (99.46%)

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
    let prev: ListNode | null, slow: ListNode | null, fast: ListNode | null;
    prev = null;
    slow = fast = head;

    // place slow runner at the middle and reverse the first half
    while (fast !== null && fast.next !== null) {
        const oldSlow = slow!;

        // advance
        slow = slow!.next;
        fast = fast.next.next;

        oldSlow.next = prev; // reverse
        prev = oldSlow;
    }

    // advance slow if odd number of nodes
    if (fast !== null) {
        slow = slow!.next;
    }

    let reverse: ListNode, forward: ListNode;
    reverse = prev!;
    forward = slow!;

    // return false if not palindrome; true otherwise
    while (reverse !== null && forward !== null) {
        if (reverse.val !== forward.val) {
            return false;
        }

        reverse = reverse.next!;
        forward = forward.next!;
    }
    return true;
};
