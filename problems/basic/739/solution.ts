// Accepted: 190ms (98.11%), 66.53MB (63.58%)

function dailyTemperatures(temperatures: number[]): number[] {
    const daysToWait = Array(temperatures.length).fill(0);
    const stack: number[] = [];

    for (let day = 0; day < temperatures.length; ++day) {
        while (stack.length > 0) {
            const pastDay = stack[stack.length-1];
            const pastTemp = temperatures[pastDay];
            const curTemp = temperatures[day];

            if (pastTemp >= curTemp) {
                break;
            }

            daysToWait[pastDay] = day - pastDay;
            stack.pop();
        }

        stack.push(day);
    }

    return daysToWait;
};
