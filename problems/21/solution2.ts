// Accepted: 70ms (31.05%), 45.51MB (10.59%)

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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    // base cases
    if (list1 === null) {
        return list2;
    }
    if (list2 === null) {
        return list1;
    }

    if (list1.val < list2.val) {
        list1.next = mergeTwoLists(list1.next, list2);

        return list1;
    } else {
        list2.next = mergeTwoLists(list2.next, list1);

        return list2;
    }
};
