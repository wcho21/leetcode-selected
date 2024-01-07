// Accepted: 56ms (88.93%), 45.01MB (83.75%)

function trap(height: number[]): number {
    const maxHeight = Math.max(...height);
    const maxHeightIndex = height.indexOf(maxHeight);

    let water = 0;

    // from left to the peak
    let maxHeightSoFar = 0;
    for (let i = 0; i < maxHeightIndex; ++i) {
        maxHeightSoFar = Math.max(maxHeightSoFar, height[i]);
        water += maxHeightSoFar - height[i];
    }

    // from right to the peak
    maxHeightSoFar = 0;
    for (let i = height.length-1; i > maxHeightIndex; --i) {
        maxHeightSoFar = Math.max(maxHeightSoFar, height[i]);
        water += maxHeightSoFar - height[i];
    }

    return water;
};
