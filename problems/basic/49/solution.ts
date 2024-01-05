// Accepted: 108ms (73.65%), 53.46MB (69.90%)

function groupAnagrams(strs: string[]): string[][] {
    const sortedStrs = strs.map(s => Array.from(s).sort().join(""));

    const anagramMap = new Map<string, string[]>();
    for (let i = 0; i < strs.length; ++i) {
        const mapKey = sortedStrs[i];
        const mapValue = strs[i];

        if (!anagramMap.has(mapKey)) {
            anagramMap.set(mapKey, []);
        }
        anagramMap.get(mapKey)!.push(mapValue);
    }

    const anagramGroups = [...anagramMap.values()];
    return anagramGroups;
};
