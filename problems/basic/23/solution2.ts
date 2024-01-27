// Accepted: 82ms (87.38%), 56.67MB (11.46%)

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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    function go(left: number = 0, right: number = lists.length): ListNode | null {
        const diff = right - left;
        if (diff === 0) {
            return null;
        }
        if (diff === 1) {
            return lists[left];
        }

        const mid = left + Math.floor(diff / 2);
        const mergedLeft = go(left, mid);
        const mergedRight = go(mid, right);

        return merge(mergedLeft, mergedRight);
    }

    function merge(left: ListNode | null, right: ListNode | null): ListNode | null {
        if (left === null) {
            return right;
        }
        if (right === null) {
            return left;
        }

        if (left.val < right.val) {
            left.next = merge(left.next, right);
            return left;
        } else {
            right.next = merge(left, right.next);
            return right;
        }
    }

    return go();
};
