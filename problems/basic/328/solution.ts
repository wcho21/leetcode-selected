// Accepted: 61ms (84.94%), 45.06MB (74.52%)

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

function oddEvenList(head: ListNode | null): ListNode | null {
    if (head === null || head.next === null) {
        return head;
    }

    const oddHead = head;
    const evenHead = head.next;
    let oddNode = oddHead;
    let evenNode = evenHead;

    while (evenNode !== null && evenNode.next !== null) {
        // reorder
        oddNode.next = evenNode.next;
        evenNode.next = evenNode.next.next;

        // advance
        oddNode = oddNode.next;
        evenNode = evenNode.next;
    }

    // append even-index nodes to odd-index ones
    oddNode.next = evenHead;

    return oddHead;
};
