// Accepted: 57ms (94.74%), 52.51MB (5.26%)

function removeDuplicateLetters(s: string): string {
    const lastOccurIndex = new Map<string, number>(Array.from(s).map((ch, i) => [ch, i]));

    const visited = new Set<string>();
    const ordered: string[] = [];

    for (let i = 0; i < s.length; ++i) {
        const ch = s[i];

        if (visited.has(ch)) {
            continue;
        }

        while (ordered.length > 0) {
            const top = ordered[ordered.length-1];
            if (i > lastOccurIndex.get(top)!) { // top is last occurrence
                break;
            }
            if (ch > top) { // in order
                break;
            }

            visited.delete(top);
            ordered.pop();
        }

        visited.add(ch);
        ordered.push(ch);
    }

    return ordered.join("");
};
