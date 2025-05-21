/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function (isConnected) {
    let visited = []
    let count = 0
    for (let x = 0; x < isConnected.length; x++) {
        if (!visited.includes(x)) {
            let toVisit = [x]
            count++;
            while (toVisit.length != 0) {
                let curRoom = toVisit.shift()
                if (!visited.includes(curRoom)) {
                    visited.push(curRoom)
                }
                for (let y = 0; y < isConnected.length; y++) {
                    if (isConnected[curRoom][y] == 1
                        && !toVisit.includes(y)
                        && !visited.includes(y)) {
                        toVisit.push(y)
                    }
                }
            }
        }
    }
    return count;
};
