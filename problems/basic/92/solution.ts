// Accepted: 64ms (24.02%), 44.40MB (50.65%)

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

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if (head === null || left === right) {
        return head;
    }

    const dummyHead = new ListNode(0, head);

    // find the first node to reverse, which becomes the last node in the reversed list
    let prev: ListNode | null = dummyHead;
    let node: ListNode | null = head;

    for (let i = 0; i < left-1; ++i) {
        prev = node;
        node = node.next!;
    }

    // keep the node just before the reversed list, and the last node in the reversed list
    const reversedFirstPrev = prev;
    const reversedLast = node;

    // reverse the given interval
    prev = node;
    node = node.next;
    for (let i = 0; i < right - left; ++i) {
        const oldNext = node!.next;

        // reverse
        node!.next = prev;

        // advance
        prev = node;
        node = oldNext;
    }

    // keep the first node in the reversed list, and the node just after the reversed list
    const reversedFirst = prev;
    const reversedLastNext = node;

    // complete the list
    reversedFirstPrev.next = reversedFirst;
    reversedLast.next = reversedLastNext;

    return dummyHead.next;
};
