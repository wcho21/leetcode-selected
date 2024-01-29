// Accepted: 53ms (94.88%), 44.85MB (62.25%)

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
    const mergedDummyHead = new ListNode();
    let merged = mergedDummyHead;

    while (list1 !== null && list2 !== null) {
        if (list1.val < list2.val) {
            merged.next = list1;
            merged = merged.next;
            list1 = list1.next;
        } else {
            merged.next = list2;
            merged = merged.next;
            list2 = list2.next;
        }
    }

    while (list1 !== null) {
        merged.next = list1;
        merged = merged.next;
        list1 = list1.next;
    }
    while (list2 !== null) {
        merged.next = list2;
        merged = merged.next;
        list2 = list2.next;
    }

    return mergedDummyHead.next;
};
