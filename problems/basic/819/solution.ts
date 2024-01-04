// Accepted: 66ms (58.46%), 45.90MB (30.77%)

function mostCommonWord(paragraph: string, banned: string[]): string {
    const bannedSet = new Set(banned);
    const matches = Array.from(paragraph.toLowerCase().matchAll(/[a-z]+/g), ([match]) => match);

    const counts = new Map<string, number>();
    for (const match of matches) {
        counts.set(match, (counts.get(match) ?? 0) + 1);
    }

    let mostCommonWord: string;
    let mostCommonCount = 0;
    for (const [word, count] of counts.entries()) {
        if (bannedSet.has(word)) {
            continue;
        }
        if (count <= mostCommonCount) {
            continue;
        }

        mostCommonWord = word;
        mostCommonCount = count;
    }

    return mostCommonWord!;
};
