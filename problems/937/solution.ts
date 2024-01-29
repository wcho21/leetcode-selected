// Accepted: 68ms (72.73%), 45.45MB (81.82%)

function reorderLogFiles(logs: string[]): string[] {
    const keys = new Map<string, [number, string, string]>();
    const getKey = (log: string): [number, string, string] => {
        if (keys.has(log)) {
            return keys.get(log)!;
        }

        const firstSpace = log.indexOf(" ");
        const identifier = log.slice(0, firstSpace);
        const content = log.slice(firstSpace+1);

        const key: [number, string, string] = /^[0-9]$/.test(content[0]) ? [1, "", ""] : [0, content, identifier];
        keys.set(log, key);
        return key;
    };

    const compareArray = <T>(arr1: T[], arr2: T[]): number => {
        if (arr1.length !== arr2.length) {
            return arr1.length - arr2.length;
        }

        for (let i = 0; i < arr1.length; ++i) {
            if (arr1[i] !== arr2[i]) {
                return (arr1[i] < arr2[i]) ? -1 : 1;
            }
        }
        return 0;
    }

    logs.sort((log1: string, log2: string) => {
        const key1 = getKey(log1);
        const key2 = getKey(log2);
        return compareArray(key1, key2);
    });

    return logs;
};
